import schemas, joblib
import numpy as np

model = joblib.load("../Backend/model/phishing_model.pkl")
scaler = joblib.load("../Backend/model/scaled_data.pkl")

def predict(features:list):
    scaled = scaler.transform([features])
    prediction = model.predict(scaled)
    return int(prediction[0])