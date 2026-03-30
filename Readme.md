# Heart Disease Prediction Dashboard

A professional Heart Disease Prediction Web Application built using Python, Flask, and Machine Learning.

This project predicts the risk of heart disease based on patient medical data and presents results in a clean, modern dashboard.

---

## Features

* Predict heart disease risk using Random Forest Classifier
* Displays risk probability (%)
* Color-coded risk indicator:

  * Low Risk
  * Medium Risk
  * High Risk
* Interactive patient vitals chart
* Clean and responsive UI dashboard
* PDF report download (optional)
* Fully portfolio-ready project

---

## Project Structure

```
HeartDiseaseDashboard/
│
├── dataset/
│   └── heart.csv
├── models/
│   └── heart_model.pkl
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── result.html
├── static/
│   └── style.css
├── train_model.py
├── app.py
└── run_project.bat
```

---

## Installation

### 1. Clone Repository

```
git clone <your-repo-link>
cd HeartDiseaseDashboard
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## Usage

### Step 1: Train Model

```
python train_model.py
```

### Step 2: Run Application

```
python app.py
```

### Step 3: Open in Browser

```
http://127.0.0.1:5000/
```

---

## Example Input

Use this sample data for testing:

```
Age: 52
BP: 130
Cholesterol: 250
Max Heart Rate: 150
Oldpeak: 1.5
```

---

## How It Works

1. User enters medical details
2. Data is sent to Flask backend
3. Model predicts heart disease risk
4. Result is displayed with:

   * Risk percentage
   * Risk level
   * Chart visualization

---

## Machine Learning

* Algorithm: Random Forest Classifier
* Dataset: Heart Disease Dataset (CSV)
* Libraries:

  * scikit-learn
  * pandas
  * numpy

---

## Requirements

```
flask
pandas
numpy
scikit-learn
matplotlib
pdfkit (optional)
```

---

## Notes

* Ensure dataset is inside dataset/ folder
* Model file will be saved in models/
* Python 3.8+ recommended
* If PDF not working, install wkhtmltopdf

---

## Screenshots (Optional)

Add your UI screenshots here for better presentation.

---

## Use Cases

* Medical prediction demo project
* Portfolio project for Data Science or Machine Learning roles
* Learning Flask with Machine Learning integration

---

## Contributing

Feel free to fork this repo and improve the project.

---

## License

This project is open-source and free to use.

---

## Support

If you like this project:

* Give it a star on GitHub
* Share on LinkedIn

---

## Author

Hassan Ali
Data Science and Machine Learning Enthusiast

---

Built using Python and Machine Learning

