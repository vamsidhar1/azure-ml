import json
import joblib
import os

def init():
    global model
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model/model.pkl")
    model = joblib.load(model_path)

def run(raw_data):
    data = json.loads(raw_data)
    result = model.predict(data)
    return result.tolist()

