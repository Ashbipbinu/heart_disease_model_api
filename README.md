# Heart Disease Prediction API


This project provides a RESTful API for predicting the likelihood of heart disease based on user input parameters. It utilizes a pre-trained machine learning model to make predictions.

# Features

Predicts the presence of heart disease using input health parameters.

Built with Flask for the API framework.

Includes a trained machine learning model (trained_model.sav).

Ready for deployment on platforms like Heroku (includes Procfile.txt and runtime.txt).

# Getting Started
## Prerequisites
Python 3.x installed on your machine.

pip package manager.

## Installation
### 1.Clone the repository:

```
git clone https://github.com/Ashbipbinu/heart_disease_model_api.git 
cd heart_disease_model_api

```
### 2.Create and activate a virtual environment (optional but recommended):

```python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3.Install the required packages:

```pip install -r requirements.txt```

### 4.Running the Application
Start the Flask server:
```python Heart_API.py```

The API will be accessible at http://127.0.0.1:5000/.

## API Usage
Endpoint: /heart_disease_pred

Method: POST

## Description: 

Predicts the likelihood of heart disease based on input parameters.

## Parameters:

age: Age of the individual

sex: Gender (1 = male; 0 = female)

cp: Chest pain type (0–3)

trestbps: Resting blood pressure

chol: Serum cholesterol in mg/dl

fbs: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)

restecg: Resting electrocardiographic results (0–2)

thalach: Maximum heart rate achieved

exang: Exercise-induced angina (1 = yes; 0 = no)

oldpeak: ST depression induced by exercise

slope: Slope of the peak exercise ST segment (0–2)

ca: Number of major vessels (0–3) colored by fluoroscopy

thal: Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)
