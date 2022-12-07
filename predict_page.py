import streamlit as st
import pickle
import numpy as np
import altair as alt
from PIL import Image
import subprocess
import os

image = Image.open('heart.jpeg')

def predict(input_data):
    input_array = np.asarray(input_data)
    input_array = input_array.reshape(1, -1)
    pickle_in = open("best.pickle", 'rb')
    clf = pickle.load(pickle_in)
    prediction = clf.predict(input_array)
    if(prediction[0] == 0):
        return 'Good'
    else:
        return 'Bad'


class ML:
    def __init__(self, path) -> None:
        self.path = path
        self.start()
    
    def load_model(self):
        with open('saved_m.pkl', 'rb') as file:
            self.data = pickle.load(file)
 
    def start(self):
        st.sidebar.title('Heart Prediction')

        st.sidebar.write('''### we need some information to predict you state''')

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
s=[
    '5',
    '6',
    '7',
    '8',
    'more than 8'
]
st.image(image, caption='Enter any caption here')
st.write('''### In just a few seconds, you can calculate your risk of developing heart disease!''')
st.write('''### To predict your heart disease status''') 
st.write('''## 1- Enter the parameters that best describe you.''')
st.write('''## 2- Press the "Predict" button and wait for the result.''')
clicked_game = st.button('Play Game')
clicked_Predict = st.button('Predict')
BMI = st.sidebar.selectbox('Select your BMI', BMI)
AGE =st.sidebar.selectbox('Select your Age', AGE)
RACE =st.sidebar.selectbox('Select your Race', RACE)
GENDER =st.sidebar.selectbox('Select your Gender', GENDER)
SMIKE =st.sidebar.selectbox('Have you smoked more than 100 cigarettes in your entire life ?)', YN)
heal  = st.sidebar.select_slider(
    'Select a color of the rainbow',
    options=['0', '1', '2', '3', '4', '5', '6'])
SLEEP = st.sidebar.write('Hours of sleep per 24h', sleep)
DRINK =st.sidebar.selectbox('How many drinks of alcohol do you have in a week?', YN)
Physical =st.sidebar.slider('Physical health in the past month (Excelent: 0 - Very bad: 30)', 0, 30, 2)
Mental =st.sidebar.slider('Mental health in the past month (Excelent: 0 - Very bad: 30)', 0, 30, 2)
STROKE = st.sidebar.selectbox('Did you have a stroke?', YN)
Physicalactivity = st.sidebar.selectbox('Physical activity in the past month', YN)
WALK = st.sidebar.selectbox('Do you have serious difficulty walking or climbing stairs?', YN)
diabetes = st.sidebar.selectbox('Have you ever had diabetes?', YN)
asthma = st.sidebar.selectbox('Do you have asthma?', YN)
kidney = st.sidebar.selectbox('Do you have kidney disease?', YN)
skin = st.sidebar.selectbox('Do you have skin cancer?', YN)

if clicked_game:
    os.system(os.path.join('.', 'main.exe'))
data = ''
if clicked_Predict:
    data = predict([BMI, SMIKE, DRINK, STROKE, Physical, Mental, WALK, GENDER, AGE, RACE, diabetes, Physicalactivity, heal, SLEEP, asthma, kidney, skin])
st.success(data)


