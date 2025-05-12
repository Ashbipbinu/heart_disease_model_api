# -*- coding: utf-8 -*-
"""
Created on Mon May 12 12:00:53 2025

@author: LENOVO
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origin = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Model_Input(BaseModel):
    age         :int
    sex         :int
    cp          :int
    trestbps    :int
    chol        :int
    fbs         :int
    restecg     :int
    thalach     :int
    exang       :int
    oldpeak     :float
    slope       :int
    ca          :int
    thal        :int
    
    
# Loading the trained model

heart_disease_model = pickle.load(open('trained_model.sav', 'rb'))

model, std = heart_disease_model


@app.post('/heart_disease_pred')

def heart_disease(input_parameter: Model_Input):
    
    input_parameter = input_parameter.json()
    input_dictionary = json.loads(input_parameter)
    
    age         = input_dictionary['age']
    sex         = input_dictionary['sex']
    cp          = input_dictionary['cp']
    trestbps    = input_dictionary['trestbps']
    chol        = input_dictionary['chol']
    fbs         = input_dictionary['fbs']
    restecg     = input_dictionary['restecg']
    thalach     = input_dictionary['thalach']
    exang       = input_dictionary['exang']
    oldpeak     = input_dictionary['oldpeak']
    slope       = input_dictionary['slope']
    ca          = input_dictionary['ca']
    thal        = input_dictionary['thal']

    
    input_data =  [ age, sex, cp, trestbps, chol, fbs, restecg,thalach, exang, oldpeak, slope, ca, thal]
    
    prediction = model.predict([input_data])
     
    if prediction[0] == 1:
         return "This patient is likely to become a heart patient"
    else:
         return "This patient is healthy" 







