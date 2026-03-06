from flask import Flask, render_template, request, send_file
import joblib
import numpy as np
import pdfkit
import os

app = Flask(__name__)
model = joblib.load("models/heart_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    values = [float(x) for x in request.form.values()]
    final = np.array(values).reshape(1, -1)

    prob = model.predict_proba(final)[0][1] * 100
    if prob >= 70:
        risk = "High Risk"
    elif prob >= 40:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    prediction_text = f"{risk} ({prob:.1f}%)"

    # Pass values and prediction to dashboard
    patient_data = {
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
        "prediction": prediction_text
    }

    return render_template("dashboard.html", data=patient_data)

@app.route("/download_report")
def download_report():
    patient_data = request.args.to_dict()
    html = render_template("report_template.html", data=patient_data)
    pdf_path = "static/patient_report.pdf"
    pdfkit.from_string(html, pdf_path)
    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)