import pandas as pd
import shap
import joblib

# Load model and training data used for SHAP explainer
model = joblib.load("logistic_model.pkl")

# You must also save and load the same X used during training (after column ordering etc.)
X_train_resampled = pd.read_csv("X_train_resampled.csv")  # You should save this during training

# Build SHAP explainer
explainer = shap.LinearExplainer(model, X_train_resampled, feature_dependence="independent")

def explain_prediction(input_dict):
    """
    Computes SHAP values for a single prediction.
    Returns base value, SHAP values, and feature contributions.
    """
    input_df = pd.DataFrame([input_dict])

    # Compute SHAP values for the input
    shap_values = explainer.shap_values(input_df)[0]  # single row
    base_value = explainer.expected_value
    feature_names = input_df.columns

    # Combine into a list of explanations
    explanation = [
        {
            "feature": feature,
            "value": float(input_dict[feature]),
            "shap_value": float(shap_val)
        }
        for feature, shap_val in zip(feature_names, shap_values)
    ]

    # Sort by absolute impact
    explanation_sorted = sorted(explanation, key=lambda x: abs(x["shap_value"]), reverse=True)

    return {
        "base_value": float(base_value),
        "prediction": float(model.predict_proba(input_df)[0][1]),  # probability of class 1
        "explanation": explanation_sorted
    }
