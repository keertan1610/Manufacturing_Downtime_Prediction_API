import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
import joblib

# Define paths
MODEL_PATH = "data/model.pkl"
DATA_PATH = "data/Machine_Downtime.csv"

def train_model():
    """
    Trains a Decision Tree Classifier on the provided dataset and saves the model.
    Returns training metrics.
    """
    try:
        # Load dataset
        data = pd.read_csv(DATA_PATH)
        
        # Feature selection
        X = data[["Hydraulic_Oil_Temperature(?C)", "Spindle_Speed(RPM)"]]  # Adjust as per your dataset
        y = data["Downtime"]  # Target column
        
        # Split dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Initialize and train the model
        model = DecisionTreeClassifier(random_state=42)
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "f1_score": f1_score(y_test, y_pred, average="weighted"),
        }

        # Save the trained model
        joblib.dump(model, MODEL_PATH)
        print(f"Model saved to {MODEL_PATH}")
        
        return metrics
    except KeyError as e:
        return {"status": "error", "message": f"KeyError: {e}"}
    except Exception as e:
        return {"status": "error", "message": f"An error occurred: {e}"}


def predict(data):
    """
    Predicts downtime based on input data using the trained model.
    Returns the prediction and confidence score.
    """
    try:
        # Load the trained model
        model = joblib.load(MODEL_PATH)

        # Convert input data to DataFrame
        input_df = pd.DataFrame([data])

        # Predict downtime and probabilities
        pred = model.predict(input_df)
        proba = model.predict_proba(input_df)

        return {
            "Downtime": "Yes" if pred[0] == 1 else "No",
            "Confidence": round(max(proba[0]), 2),
        }
    except FileNotFoundError:
        return {"status": "error", "message": "Trained model not found. Please train the model first."}
    except Exception as e:
        return {"status": "error", "message": f"An error occurred: {e}"}