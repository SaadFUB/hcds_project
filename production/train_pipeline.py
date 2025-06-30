import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import classification_report, accuracy_score
import shap
import joblib
import cloudpickle
import os

# ---------------------------- Configurations ---------------------------
NUM_FEATURES = [
    'Age', 'BMI', 'AlcoholConsumption', 'PhysicalActivity', 'DietQuality', 'SleepQuality',
    'SystolicBP', 'DiastolicBP',
    'CholesterolTotal', 'CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides',
    'MMSE', 'FunctionalAssessment', 'ADL'
]

CAT_FEATURES = [
    'Gender', 'Ethnicity', 'EducationLevel',
    'Smoking', 'FamilyHistoryAlzheimers', 'CardiovascularDisease', 'Diabetes', 'Depression',
    'HeadInjury', 'Hypertension',
    'MemoryComplaints', 'BehavioralProblems', 'Confusion', 'Disorientation',
    'PersonalityChanges', 'DifficultyCompletingTasks', 'Forgetfulness'
]

DROP_FEATURES = ['PatientID', 'DoctorInCharge']
TARGET = 'Diagnosis'

SAVE_DIR = 'model_artifacts'
os.makedirs(SAVE_DIR, exist_ok=True)

# ----------------------------- Data Loading and Processing -----------------
df = pd.read_csv("production/alzheimers_disease_data.csv")
X = df.drop(columns=[TARGET] + DROP_FEATURES)
y = df[TARGET]


X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=10)

ros = RandomOverSampler(random_state=10)
X_resampled, y_resampled = ros.fit_resample(X_train, y_train)

preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), NUM_FEATURES),
    ('cat', 'passthrough', CAT_FEATURES)
])

preprocessing_pipeline = Pipeline(steps=[('preprocessor', preprocessor)])

X_resampled_transformed = preprocessing_pipeline.fit_transform(X_resampled)
X_test_transformed = preprocessing_pipeline.transform(X_test)

# joblib.dump(preprocessing_pipeline, os.path.join(SAVE_DIR, 'preprocessor.pkl'))
with open(os.path.join(SAVE_DIR, 'pre_processor.pkl'), 'wb') as f:
    cloudpickle.dump(preprocessing_pipeline, f)

# ----------------------------- Training Models -----------------

# Logistic Regression
logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(X_resampled_transformed, y_resampled)
joblib.dump(logistic_model, os.path.join(SAVE_DIR, 'logistic_model.pkl'))

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_resampled_transformed, y_resampled)
joblib.dump(rf_model, os.path.join(SAVE_DIR, 'rf_model.pkl'))

# Neural Network (MLP)
nn_model = MLPClassifier(hidden_layer_sizes=(25, 50), max_iter=500, random_state=42, activation='relu',            
    solver='adam',                 
    alpha=1e-4,)
nn_model.fit(X_resampled_transformed, y_resampled)
joblib.dump(nn_model, os.path.join(SAVE_DIR, 'nn_model.pkl'))

# ----------------------------- Explainers -----------------

# Logistic Regression SHAP
logistic_explainer = shap.LinearExplainer(logistic_model, X_resampled_transformed, feature_perturbation="interventional")
joblib.dump(logistic_explainer, os.path.join(SAVE_DIR, 'logistic_explainer.pkl'))

# Random Forest SHAP
rf_explainer = shap.TreeExplainer(rf_model)
joblib.dump(rf_explainer, os.path.join(SAVE_DIR, 'rf_explainer.pkl'))

# Neural Network SHAP
background_data = shap.sample(X_resampled_transformed, 100)
nn_explainer = shap.KernelExplainer(nn_model.predict_proba, background_data)
joblib.dump(nn_explainer, os.path.join(SAVE_DIR, 'nn_explainer.pkl'))

np.save(os.path.join(SAVE_DIR, 'background_data.npy'), background_data)

# ----------------------------- Logs -----------------

lr_y_pred = logistic_model.predict(X_test_transformed)
rf_y_pred = rf_model.predict(X_test_transformed)
nn_y_pred = nn_model.predict(X_test_transformed)

print("Logistic Regression")
print(classification_report(y_test, lr_y_pred))

print("Random Forest")
print(classification_report(y_test, rf_y_pred))

print("Neural Network")
print(classification_report(y_test, nn_y_pred))


print("Training pipeline completed.")
print(f"Artifacts saved in: {SAVE_DIR}")
print("Saved:")
