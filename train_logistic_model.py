# train_logistic_model.py

import pandas as pd
import joblib
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import accuracy_score, classification_report, f1_score, roc_auc_score
from imblearn.over_sampling import RandomOverSampler

def train_and_save_model(X, y, model_path='logistic_model.pkl'):
    # Split before oversampling
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, stratify=y, test_size=0.2, random_state=10
    )

    print("Before oversampling:", Counter(y_train))
    ros = RandomOverSampler(random_state=10)
    X_resampled, y_resampled = ros.fit_resample(X_train, y_train)
    print("After oversampling: ", Counter(y_resampled))

    model = LogisticRegressionCV(
        cv=5,
        penalty='l2',
        solver='liblinear',
        scoring='accuracy',
        class_weight='balanced',  # optional now, but safe
        max_iter=1000
    )
    model.fit(X_resampled, y_resampled)

    print("Best C:", model.C_[0])
    
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print("F1 score:", f1_score(y_test, y_pred))
    print("ROC AUC:", roc_auc_score(y_test, y_pred))

    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

    return model, X_test, y_test

if __name__ == "__main__":
    # Example placeholder (replace with actual data loading)
    df = pd.read_csv("your_dataset.csv")
    X = df.drop("target", axis=1)
    y = df["target"]
    train_and_save_model(X, y)
