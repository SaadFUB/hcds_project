import os
import joblib

lr_model_path = os.path.join(os.path.dirname(__file__), 'lr_model.joblib')

lr_model = joblib.load(lr_model_path)