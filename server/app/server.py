from fastapi import FastAPI
from lr_model import lr_model
import numpy as np

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