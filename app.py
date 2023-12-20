import streamlit as st
import pandas as pd
from models.dummies import *
import joblib



scaler = joblib.load('models/scaler.h5')
model = joblib.load('models/RF_model.h5')


st.title('Heart Attack Prediction')

age = st.number_input('Age', min_value=18)
cholesterol = st.number_input('Cholesterol', min_value=120)
heart_rate = st.number_input('Heart Rate', min_value=40)
exercise_hours_per_week =st.number_input('Exercise Hours Per Week', min_value=0.001)
diet = st.selectbox("Diet",['Healthy','Average','Unhealthy'])
stress_level = st.number_input('Stress Level', min_value=1,max_value=10)
sedentary_hours_per_day = st.number_input('Sedentary Hours Per Day', min_value=0.001)
income = st.number_input('Income')
bmi = st.number_input('BMI',min_value=18)
triglycerides = st.number_input('Triglycerides',min_value=30)
physical_activity_days_per_week = st.number_input('Physical Activity Days Per Week',min_value=0,max_value=7)
sleep_hours_per_day = st.number_input('Sleep Hours Per Day')
systolic  = st.number_input('Systolic',min_value=90)





data=[]
data.append(age)
data.append(cholesterol)
data.append(heart_rate)
data.append(exercise_hours_per_week)
data.append(diet_dummies [diet])
data.append(stress_level)
data.append(sedentary_hours_per_day)
data.append(income)
data.append(bmi)
data.append(triglycerides)
data.append(physical_activity_days_per_week)
data.append(sleep_hours_per_day)
data.append(systolic)



result = model.predict([data])

st.success(f'Predict Heart Attack Risk : {Heart_Attack_Risk_dummies[result[0]]}')




