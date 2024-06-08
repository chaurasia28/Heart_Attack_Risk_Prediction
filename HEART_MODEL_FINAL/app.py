import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.write("""
# Heart disease Prediction App

This app predicts If a patient has a heart disease

Data obtained from Kaggle: https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset.
""")

st.sidebar.header('User Input Features')

heart_disease_model = pickle.load(open('heart_model_final.sav','rb'))

# Collects user input features into dataframe

age = st.sidebar.number_input('Enter your age: ')
sex  = st.sidebar.selectbox('Sex',(0,1))
cp = st.sidebar.selectbox('Chest pain type',(0,1,2,3))
tres = st.sidebar.number_input('Resting blood pressure: ')
chol = st.sidebar.number_input('Serum cholestoral in mg/dl: ')
fbs = st.sidebar.selectbox('Fasting blood sugar',(0,1))
res = st.sidebar.number_input('Resting electrocardiographic results: ')
tha = st.sidebar.number_input('Maximum heart rate achieved: ')
exa = st.sidebar.selectbox('Exercise induced angina: ',(0,1))
old = st.sidebar.number_input('oldpeak ')
slope = st.sidebar.number_input('The slope of the peak exercise ST segmen: ')
ca = st.sidebar.selectbox('number of major vessels',(0,1,2,3))
thal = st.sidebar.selectbox('thal',(0,1,2))

heart_diagnosis = ''

    # creating a button for Prediction

if st.button('Heart Disease Test Result'):

    user_input = [age, sex, cp, tres, chol, fbs, res, tha, exa, old, slope, ca, thal]

    user_input = [float(x) for x in user_input]

    heart_prediction = heart_disease_model.predict([user_input])

    if heart_prediction[0] == 1:
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person does not have any heart disease'

st.success(heart_diagnosis)

# streamlit run app.py