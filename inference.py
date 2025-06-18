import joblib
import pandas as pd

# Load pre-trained model
model = joblib.load("logistic_model.pkl")

def predict_single(input_dict):
    """
    Predict a single sample.
    input_dict: a dictionary of feature_name -> value
    """
    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][1]  # probability of positive class

    return {
        "prediction": int(prediction),
        "probability": float(proba)
    }
