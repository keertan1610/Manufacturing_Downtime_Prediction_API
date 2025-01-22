import os
from fastapi import UploadFile

def save_file(file: UploadFile):
    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file_path

def load_model(path="data/model.pkl"):
    if os.path.exists(path):
        return joblib.load(path)
    return None