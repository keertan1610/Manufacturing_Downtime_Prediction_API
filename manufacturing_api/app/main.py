from fastapi import FastAPI, UploadFile, File
import pandas as pd
from app.model import train_model, predict
from app.utils import save_file, load_model

app = FastAPI()

@app.post("/upload")
async def upload_data(file: UploadFile = File(...)):
    file_path = save_file(file)
    return {"message": "File uploaded successfully", "path": file_path}

@app.post("/train")
def train():
    metrics = train_model()
    return {"message": "Model trained successfully", "metrics": metrics}

@app.post("/predict")
def predict_downtime(data: dict):
    prediction = predict(data)
    return prediction