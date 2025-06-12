from fastapi import FastAPI
import numpy as np
import os
import joblib

lr_model_path = os.path.join(os.path.dirname(__file__), 'lr_model.joblib')
lr_model = joblib.load(lr_model_path)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "HCDS Project API"}

@app.post("/predict")
async def predict(data: dict):
    features = np.array(list(data['features'].reshape(1, -1)))
    prediction = lr_model.predict(features)
    class_name = 'Has Alzheimer\'s' if prediction == 1 else 'No Alzheimer\'s'
    return {'prediction': class_name}