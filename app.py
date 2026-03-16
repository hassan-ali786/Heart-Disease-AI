from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model & scaler
model = joblib.load("models/heart_model.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Collect form data
    values = [
        float(request.form["age"]),
        int(request.form["sex"]),
        int(request.form["cp"]),
        float(request.form["trestbps"]),
        float(request.form["chol"]),
        int(request.form["fbs"]),
        int(request.form["restecg"]),
        float(request.form["thalach"]),
        int(request.form["exang"]),
        float(request.form["oldpeak"]),
        int(request.form["slope"]),
        int(request.form["ca"]),
        int(request.form["thal"])
    ]

    X = np.array(values).reshape(1, -1)
    X_scaled = scaler.transform(X)
    prob = model.predict_proba(X_scaled)[0][1] * 100

    if prob >= 70:
        risk = "High Risk"
    elif prob >= 40:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    data = {
        "age": values[0],
        "sex": values[1],
        "cp": values[2],
        "trestbps": values[3],
        "chol": values[4],
        "fbs": values[5],
        "restecg": values[6],
        "thalach": values[7],
        "exang": values[8],
        "oldpeak": values[9],
        "slope": values[10],
        "ca": values[11],
        "thal": values[12],
        "prediction": risk,
        "probability": round(prob, 1)
    }

    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)