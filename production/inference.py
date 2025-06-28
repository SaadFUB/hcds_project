from joblib import load
import numpy as np
import shap
import os

SAVE_DIR = 'model_artifacts'

logistic_model = load(os.path.join(SAVE_DIR, 'logistic_model.pkl'))
logistic_model = load(os.path.join(SAVE_DIR, 'rf_model.pkl'))
nn_model = load(os.path.join(SAVE_DIR, 'nn_model.pkl'))

logistic_explainer = joblib.load(os.path.join(SAVE_DIR, 'logistic_explainer.pkl'))
rf_explainer = joblib.load(os.path.join(SAVE_DIR, 'rf_explainer.pkl'))
background_data = np.load(os.path.join(SAVE_DIR, 'background_data.npy'))
nn_explainer = joblib.load(os.path.join(SAVE_DIR, 'nn_explainer.pkl'))

# TODO: Make sure the input is preprocessed
