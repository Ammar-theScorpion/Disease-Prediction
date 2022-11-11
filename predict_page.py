import streamlit as st
import pickle
import numpy as np
import altair as alt
from PIL import Image



image = Image.open('heart.jpeg')



class ML:
    def __init__(self, path) -> None:
        self.path = path
        self.start()
    
    def load_model(self):
        with open('saved_m.pkl', 'rb') as file:
            self.data = pickle.load(file)
 
    def start(self):
        st.title('Heart Prediction')

        st.write('''### we need some information to predict you state''')

BMI = [
    'Normal weight BMI (18.5-25)',
    'Underweight BMI (< 18.5)',
    'Overweight BMI (25-30)',
    'Obese BMI (> 30)'
]
AGE = [
    '18-24',
    '25-29',
    '30-34',
    '35-39',
    '40-44',
    '45-49',
    '50-54',
    '55-59',
    '60-64'
]
RACE = [
    'Asian',
    'Black',
    'Hispanic',
    'American Indian/Alaskan Native',
    'White',
    'Other'
]
GENDER =[
    'Female',
    'Male'
]
YN=[
    'YES',
    'NO'
]
PH=[
    'Good',
    'Excellent',
    'Fair',
    'Very good',
    'Poor'
]
st.image(image, caption='Enter any caption here')
st.write('''### In just a few seconds, you can calculate your risk of developing heart disease!''')
st.write('''### To predict your heart disease status:\n
##1- Enter the parameters that best describe you.\n
##2- Press the "Predict" button and wait for the result.''')
st.selectbox('Select your BMI', BMI)
st.selectbox('Select your Age', AGE)
st.selectbox('Select your Race', RACE)
st.selectbox('Select your Gender', GENDER)
st.selectbox('Have you smoked more than 100 cigarettes in your entire life ?)', YN)
st.selectbox('How many drinks of alcohol do you have in a week?', YN)
st.selectbox('Did you have a stroke?', YN)
st.selectbox('Hours of sleep per 24h', PH)
st.selectbox('Physical activity in the past month', YN)
st.selectbox('Do you have serious difficulty walking or climbing stairs?', YN)
st.selectbox('Have you ever had diabetes?', YN)
st.selectbox('Do you have asthma?', YN)
st.selectbox('Do you have kidney disease?', YN)
st.selectbox('Do you have skin cancer?', YN)
