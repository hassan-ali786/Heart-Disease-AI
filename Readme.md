# Heart Disease Prediction Dashboard

A professional **Heart Disease Prediction Web Application** using **Python, Flask, and Machine Learning**.  
This project predicts heart disease risk based on patient medical data and displays a modern, interactive dashboard with charts.

## Features

- Predict **heart disease risk** using a trained **Random Forest Classifier**.
- Displays **risk probability (%)**.
- **Color-coded risk meter**: Green (Low), Yellow (Medium), Red (High).
- Interactive **patient vitals chart** (BP, Cholesterol, Max Heart Rate, Oldpeak).
- Responsive **modern dashboard UI**.
- Fully **portfolio-ready** for LinkedIn / GitHub.
- Optional **downloadable patient report** (PDF) with pdfkit.

## Folder Structure
HeartDiseaseDashboard/
│
├── dataset/
│ └── heart.csv
├── models/
│ └── heart_model.pkl
├── templates/
│ ├── index.html
│ ├── dashboard.html
│ └── result.html
├── static/
│ ├── style.css
├── train_model.py
├── app.py
└── run_project.bat


## Installation

1. Clone the repository:

```bash
git clone <repository-url>

2.Navigate to the project folder:

cd HeartDiseaseDashboard

3.Install dependencies:

pip install -r requirements.txt


Usage

Run the project:

python train_model.py
python app.py