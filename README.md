
# Manufacturing Downtime Prediction API

## Description
This project provides an API to predict manufacturing machine downtime based on input features such as hydraulic oil temperature and spindle speed. It uses a machine learning model trained with a Decision Tree Classifier to classify downtime events. 

The API is built with FastAPI, providing endpoints for training the model and making predictions.

---

## Features
- **Train Endpoint**: Trains the model on historical data and saves it for future predictions.
- **Predict Endpoint**: Accepts input data and returns a prediction with confidence.

---

## Installation

### Prerequisites
- Python 3.8+
- Pipenv or Python Virtual Environment

### Steps
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # For Linux/Mac
   .venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your training data file:
   - Place the `Machine_Downtime.csv` file in the `data/` directory.

---

## Usage

### 1. Start the API Server
Run the server locally:
```bash
uvicorn app.main:app --reload
```
By default, the API will be accessible at `http://127.0.0.1:8000`.

---

### 2. Endpoints

#### **Train Model**
- **URL**: `POST /train`
- **Description**: Trains the model using the dataset and saves the trained model as `model.pkl`.
- **Response**:
  ```json
  {
    "accuracy": 0.85,
    "f1_score": 0.88
  }
  ```
- **cURL**:
  ```bash
  curl -X POST http://127.0.0.1:8000/train
  ```

---

#### **Predict Downtime**
- **URL**: `POST /predict`
- **Description**: Predicts if a machine will experience downtime based on input data.
- **Request Body**:
  ```json
  {
    "Hydraulic_Oil_Temperature(?C)": 75,
    "Spindle_Speed(RPM)": 1200
  }
  ```
- **Response**:
  ```json
  {
    "Downtime": "Yes",
    "Confidence": 0.92
  }
  ```
- **cURL**:
  ```bash
  curl -X POST http://127.0.0.1:8000/predict   -H "Content-Type: application/json"   -d '{
    "Hydraulic_Oil_Temperature(?C)": 75,
    "Spindle_Speed(RPM)": 1200
  }'
  ```

---

## File Structure
```
├── app/
│   ├── main.py           # FastAPI app with endpoint definitions
│   ├── model.py          # Model training and prediction logic
├── data/
│   ├── Machine_Downtime.csv  # Input dataset
│   ├── model.pkl         # Trained model (generated after training)
├── .venv/                # Virtual environment (ignored in .gitignore)
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

---

## Dependencies
- `fastapi`: Framework for building APIs.
- `scikit-learn`: Library for machine learning algorithms.
- `joblib`: For model serialization.
- `pandas`: Data manipulation and analysis.
- `uvicorn`: ASGI server for FastAPI.

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Testing
1. Ensure the server is running (`uvicorn app.main:app --reload`).
2. Use tools like `Postman`, `cURL`, or browser-based testing (e.g., Swagger UI at `http://127.0.0.1:8000/docs`).

---

## Author
SAI KEERTAN K  
saikeertan2003@gmail.com 


https://www.linkedin.com/in/sai-keertan-08aab2244/

--- 
