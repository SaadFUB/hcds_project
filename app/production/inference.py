from joblib import load
import pandas as pd
import numpy as np
import shap
import os
from pathlib import Path
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from sklearn.inspection import partial_dependence
from google import genai
from google.genai import types
from fileloader import find_file
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix, classification_report
import seaborn as sns


shap.initjs()

print("Sklearn version:", sklearn.__version__)


SAVE_DIR = 'model_artifacts'
REQUIRED_FEATURES = [
    'Age', 'Gender', 'Ethnicity', 'EducationLevel', 'BMI', 'Smoking',
    'AlcoholConsumption', 'PhysicalActivity', 'DietQuality', 'SleepQuality',
    'FamilyHistoryAlzheimers', 'CardiovascularDisease', 'Diabetes', 'Depression',
    'HeadInjury', 'Hypertension', 'SystolicBP', 'DiastolicBP', 'CholesterolTotal',
    'CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides', 'MMSE',
    'FunctionalAssessment', 'MemoryComplaints', 'BehavioralProblems', 'ADL',
    'Confusion', 'Disorientation', 'PersonalityChanges',
    'DifficultyCompletingTasks', 'Forgetfulness'
]

categorical_mappings = {
        'Gender': {'Male': 1, 'Female': 0},
        'Ethnicity': {'Caucasian': 0, 'African American': 1, 'Asian': 2, 'Other': 3},
        'EducationLevel': {'None': 0, 'High School': 1, 'Bachelor\'s': 2, 'Higher': 3},
        'Smoking': {'No': 0, 'Yes': 1},
        'FamilyHistoryAlzheimers': {'No': 0, 'Yes': 1},
        'CardiovascularDisease': {'No': 0, 'Yes': 1},
        'Diabetes': {'No': 0, 'Yes': 1},
        'Depression': {'No': 0, 'Yes': 1},
        'HeadInjury': {'No': 0, 'Yes': 1},
        'Hypertension': {'No': 0, 'Yes': 1},
        'MemoryComplaints': {'No': 0, 'Yes': 1},
        'BehavioralProblems': {'No': 0, 'Yes': 1},
        'Confusion': {'No': 0, 'Yes': 1},
        'Disorientation': {'No': 0, 'Yes': 1},
        'PersonalityChanges': {'No': 0, 'Yes': 1},
        'DifficultyCompletingTasks': {'No': 0, 'Yes': 1},
        'Forgetfulness': {'No': 0, 'Yes': 1}
    }

df = pd.read_csv(find_file("production/alzheimers_disease_data.csv"))
X = df.drop(columns=["Diagnosis", "DoctorInCharge", "PatientID"])
y = df["Diagnosis"]

# with open(os.path.join(SAVE_DIR, 'pre_processor.pkl'), 'rb') as f:
#     preprocessing_pipeline  = load(f)

logistic_model = load(find_file('logistic_model.pkl'))
rf_model = load(find_file('rf_model.pkl'))
nn_model = load(find_file('nn_model.pkl'))

models = {
    "Logistic Regression": logistic_model,
    "Random Forest": rf_model,
    "Neural Network": nn_model
}

logistic_explainer = load(find_file('logistic_explainer.pkl'))
rf_explainer = load(find_file('rf_explainer.pkl'))
background_data = np.load(find_file('background_data.npy'))
nn_explainer = load(find_file('nn_explainer.pkl'))

def get_feature_values(input_features):
    return [
            categorical_mappings[feature].get(input_features[feature], input_features[feature]) 
            if feature in categorical_mappings 
            else input_features[feature] 
            for feature in REQUIRED_FEATURES
        ]

def predict(input_features, model_name):

    feature_values = get_feature_values(input_features)
    
    features = np.array(feature_values)
    features = pd.DataFrame([features], columns=REQUIRED_FEATURES)

    # features = preprocessing_pipeline.transform(features)
    # print(type(preprocessing_pipeline ))
    print(features)

    if model_name == 'Logistic Regression':
        prediction = {"prediction": logistic_model.predict(features), "probability": logistic_model.predict_proba(features)}
    elif model_name == 'Random Forest':
        prediction = {"prediction": rf_model.predict(features), "probability": rf_model.predict_proba(features)}
    elif model_name == 'Neural Network':
        prediction = {"prediction": nn_model.predict(features), "probability": nn_model.predict_proba(features)}


    print(f"Prediction {model_name}:", prediction)
    
    return prediction

def explain_waterfall(input_features, model_name):
    
    feature_values = get_feature_values(input_features)

    features = np.array(feature_values)
    features = pd.DataFrame([features], columns=REQUIRED_FEATURES)

    if model_name == 'Logistic Regression':
        explainer = logistic_explainer
        expected_value = explainer.expected_value
    elif model_name == 'Random Forest':
        explainer = rf_explainer
        expected_value = explainer.expected_value
    elif model_name == 'Neural Network':
        explainer = nn_explainer
        expected_value = explainer.expected_value[1]

    shap_values = explainer.shap_values(features)

    if model_name == 'Neural Network':
        shap_values = shap_values[:,:,1]
    
    print("Waterfall Explainer:", explainer.expected_value)
    
    explanation = shap.Explanation(
        values=shap_values,
        base_values=expected_value,
        data=features
    )

    print("Waterfall explanation:", explanation.shape, "shap_values:", shap_values.shape)

    if model_name == 'Logistic Regression':
        waterfall_explanation = explanation[0]
    elif model_name == 'Random Forest':
        waterfall_explanation = explanation[0,:,1]
    elif model_name == 'Neural Network':
        waterfall_explanation = explanation[0]
    
    plt.figure(figsize=(10, 6))
    shap.plots.waterfall(waterfall_explanation, show=False)
    st.pyplot(plt.gcf(), clear_figure=True)
    plt.close()

    data = dict(zip(REQUIRED_FEATURES, waterfall_explanation.values))

    return data


def explain_force(input_features, model_name):
    feature_values = get_feature_values(input_features)

    features = np.array(feature_values)
    features = pd.DataFrame([features], columns=REQUIRED_FEATURES)

    if model_name == 'Logistic Regression':
        explainer = logistic_explainer
        shap_values = explainer.shap_values(features)
        expected_value = explainer.expected_value
    elif model_name == 'Random Forest':
        explainer = rf_explainer
        shap_values = explainer.shap_values(features)[0,:,1]
        expected_value = explainer.expected_value[1]
    elif model_name == 'Neural Network':
        explainer = nn_explainer
        shap_values = explainer.shap_values(features)[0,:,1]
        expected_value = explainer.expected_value[1]

    print(model_name,"Explainer ", explainer.expected_value)

    shap.initjs()

    features_short = features.apply(lambda x: str(x)[:10])
    plot = shap.force_plot(
        expected_value,
        shap_values,
        features_short,
        matplotlib=True,
        show=False,
        figsize=(40,3)
    )

    st.pyplot(plt.gcf(), clear_figure=True)
    plt.close()

def violin_with_user_value(feature_name, input_features):

    feature_values = get_feature_values(input_features)

    fig = px.violin(df, y=feature_name, box=True, points=False)
    fig.add_trace(go.Scatter(
        y=[feature_values[REQUIRED_FEATURES.index(feature_name)]],
        x=[0],
        mode='markers',
        marker=dict(color='red', size=12),
        name="User Value"
    ))
    fig.update_layout(title=f"Distribution of {feature_name} with User's Value")

    st.plotly_chart(fig, use_container_width=True)

def pdp_with_user_value(feature_name, input_features, model_name):
    
    current_df = df.drop(columns=["Diagnosis", "DoctorInCharge", "PatientID"])

    feature_values = get_feature_values(input_features)
    current_value = feature_values[REQUIRED_FEATURES.index(feature_name)]

    if model_name == 'Logistic Regression':
        model = logistic_model
    elif model_name == 'Random Forest':
        model = rf_model
    elif model_name == 'Neural Network':
        model = nn_model

    pd_result = partial_dependence(model, current_df, [feature_name], kind='average', grid_resolution=50)
    feature_vals = pd_result['values'][0]
    pdp_values = pd_result['average'][0]

    user_pred = np.interp(current_value, feature_vals, pdp_values)

    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=feature_vals,
        y=pdp_values,
        mode='lines',
        name='Partial Dependence',
        line=dict(color='blue')
    ))

    
    fig.add_trace(go.Scatter(
        x=[current_value],
        y=[user_pred],
        mode='markers+text',
        marker=dict(color='red', size=10),
        text=[f"User: {current_value:.2f}"],
        textposition="top center",
        name='User Input'
    ))

    fig.update_layout(
        title=f"Partial Dependence of {feature_name}",
        xaxis_title=feature_name,
        yaxis_title="Model Prediction",
        showlegend=True
    )

    st.plotly_chart(fig, use_container_width=True)

    
    

def load_random_row():
    
    random_index = np.random.randint(0, len(df))
    
    random_row = df.iloc[random_index]
    
    
    row_dict = {}
    for column, value in random_row.items():
        if pd.isna(value):
            row_dict[column] = ""
        else:
            row_dict[column] = value
    
    print(row_dict)
    return row_dict
    
def explain_shap_values(shap_dict):
    
    sorted_shap_items = sorted(shap_dict.items(), key=lambda item: abs(item[1]), reverse=True)

    top_n = min(5, len(sorted_shap_items))
    top_impact_features = sorted_shap_items[:top_n]

    top_shap_description = "\n".join([f"{feature}: {value}" for feature, value in top_impact_features])

    prompt = f"""You are an AI that explains how different features influence a model's prediction, focusing specifically on SHAP values.

            Based on the following features and their SHAP values, explain the contribution of *only* the {top_n} most impactful features to the model's prediction. Do not mention any other features, and avoid numerical scores in your explanation. For each of these features, describe in plain English whether it pushed the prediction higher or lower and why it's significant, avoiding technical jargon.

            {top_shap_description}

            Keep your explanation concise, aiming for 2 to 3 short paragraphs. Your response should *only* contain this explanation and nothing else."""

    
    client = genai.Client(
        api_key=os.getenv("gemini_key"), 
    )

    model = "gemini-2.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]

    
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain"
    )

    full_string = ""
    
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if isinstance(chunk.text, str):
            full_string += chunk.text

    return full_string


    #----------------------------- Methodology Utils ------------------

def model_performance():
    metrics_df = pd.DataFrame(columns=["Model", "Accuracy", "Precision", "Recall", "F1 Score", "AUC"])

    fig_roc, ax = plt.subplots()
    for name, model in models.items():
        y_pred = model.predict(X)
        y_proba = model.predict_proba(X)[:, 1]

        acc = np.mean(y_pred == y)
        precision = np.round((y_pred & y).sum() / max(y_pred.sum(), 1), 2)
        recall = np.round((y_pred & y).sum() / max(y.sum(), 1), 2)
        f1 = 2 * (precision * recall) / max((precision + recall), 1)
        auc = roc_auc_score(y, y_proba)

        metrics_df.loc[len(metrics_df)] = [name, acc, precision, recall, f1, auc]

        fpr, tpr, _ = roc_curve(y, y_proba)
        ax.plot(fpr, tpr, label=f"{name} (AUC = {auc:.2f})")

    ax.plot([0, 1], [0, 1], linestyle='--')
    ax.set_title("ROC Curves")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.legend()

    return fig_roc, metrics_df

def feature_importance():
    col1, col2, col3, col4 = st.columns([0.5,1,1, 0.5])
    for name, model in models.items():
        if name == "Logistic Regression":
            with col2:
                st.subheader(name)
                coefs = model.coef_[0]
                feature_df = pd.DataFrame({"Feature": X.columns, "Coefficient": coefs})
                feature_df["Odds Ratio"] = np.exp(feature_df["Coefficient"])
                feature_df = feature_df.sort_values(by="Coefficient", key=np.abs, ascending=False)
                fig, ax = plt.subplots()
                sns.barplot(x="Coefficient", y="Feature", data=feature_df.head(10), ax=ax)
                st.pyplot(fig)
        elif name == "Random Forest":
            with col2:
                st.subheader(name)
                importances = model.feature_importances_
                feature_df = pd.DataFrame({"Feature": X.columns, "Importance": importances})
                feature_df = feature_df.sort_values(by="Importance", ascending=False)
                fig, ax = plt.subplots()
                sns.barplot(x="Importance", y="Feature", data=feature_df.head(10), ax=ax)
                st.pyplot(fig)
        else:
            with col3:
                st.subheader(name)
                shap_values = np.load(find_file("background.npy"), allow_pickle=True)
                print(shap_values.shape)
                fig, ax = plt.subplots()
                shap.summary_plot(shap_values[:,:,1], X)
                st.pyplot(fig)

def data_transparency():
    col1, col2, col3 = st.columns([1,0.5,1])
    with col1:
        st.markdown("### Feature Distributions by Diagnosis")
        selected_feature = st.selectbox("Select a feature", X.columns)
        fig, ax = plt.subplots()
        sns.kdeplot(data=df, x=selected_feature, hue="Diagnosis", ax=ax)
        st.pyplot(fig)

    with col3:
        st.markdown("### Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(df.corr(), cmap="coolwarm", annot=False, ax=ax)
        st.pyplot(fig)

def fairness():
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        demographic_feature = st.selectbox("Demographic Feature:", ["Age", "Gender", "Ethnicity", "EducationLevel"])
        selected_model = st.selectbox("Select a model", list(models.keys()))
        if demographic_feature:
            fig, ax = plt.subplots()
            subgroup_data = df.copy()
            subgroup_data["prediction"] = models[selected_model].predict(X)
            bias_df = pd.crosstab(subgroup_data[demographic_feature], subgroup_data["prediction"], normalize='index')
            bias_df.plot(kind='bar', stacked=True, ax=ax, colormap="coolwarm")
            ax.set_ylabel("Prediction Distribution")
            ax.set_title(f"Prediction Bias across {demographic_feature}")
            st.pyplot(fig)

