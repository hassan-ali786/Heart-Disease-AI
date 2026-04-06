# Heart Disease Prediction System

A production-ready web application that predicts the likelihood of heart disease using Machine Learning and presents results through a structured and user-friendly dashboard.

This project is suitable for data science portfolios, machine learning demonstrations, and healthcare analytics prototypes.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-purple?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-blue?logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-orange?logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-Styling-blue?logo=css3)

---

## Key Features

- Machine Learning-based heart disease prediction using Random Forest Classifier  
- Risk probability displayed as a percentage  
- Categorized risk levels:
  - Low Risk  
  - Medium Risk  
  - High Risk  
- Interactive dashboard for patient vitals visualization  
- Optional PDF report generation  
- Clean and responsive user interface  

---

## Project Structure

```
HeartDiseaseAI/
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

### 1. Clone the Repository

```bash
git clone https://github.com/hassan-ali786/Heart-Disease-AI.git
cd HeartDiseaseDashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Step 1: Train the Model

```bash
python train_model.py
```

### Step 2: Run the Application

```bash
python app.py
```

### Step 3: Access the Application

```
http://127.0.0.1:5000/
```

---

## Example Input

| Parameter        | Value |
|-----------------|------|
| Age             | 52   |
| Blood Pressure  | 130  |
| Cholesterol     | 250  |
| Max Heart Rate  | 150  |
| Oldpeak         | 1.5  |

---

## How It Works

1. User inputs medical data through the web interface  
2. Data is sent to the Flask backend  
3. The trained model processes the input  
4. The system returns:
   - Risk percentage  
   - Risk category  
   - Visual representation of patient metrics  

---

## Machine Learning Details

- Algorithm: Random Forest Classifier  
- Dataset: Heart Disease Dataset (CSV format)  
- Workflow:
  - Data preprocessing  
  - Feature selection  
  - Model training  
  - Model serialization using `.pkl`  

---

## Requirements

```
flask
pandas
numpy
scikit-learn
matplotlib
pdfkit
```

---

## Notes

- Ensure the dataset is placed inside the `dataset/` directory  
- The trained model will be saved in the `models/` directory  
- Python 3.8 or higher is recommended  
- For PDF functionality, install `wkhtmltopdf`  

---

## Screenshots

Add application screenshots here to enhance presentation.

---

## Use Cases

- Data Science portfolio project  
- Machine Learning demonstration  
- Healthcare analytics prototype  
- Flask and Machine Learning integration example  

---

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository  
2. Create a new branch  
3. Submit a pull request  

---

## License

This project is open-source and available under the MIT License.

---

## Author

Hassan Ali  
Data Science and Machine Learning Enthusiast  

---

## Future Improvements

- Deployment on cloud platforms such as AWS, Render, or Heroku  
- User authentication system  
- Integration of advanced models such as XGBoost  
- Real-time health data integration  
