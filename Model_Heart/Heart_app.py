import streamlit as st
import pandas as pd
import joblib

# Load saved model and columns
model = joblib.load('C:\\Users\\batul\\OneDrive\\Desktop\\ITR_Projects\\Model_Heart\\heart_model.pkl')
columns = joblib.load('C:\\Users\\batul\\OneDrive\\Desktop\\ITR_Projects\\Model_Heart\\columns.pkl')

st.set_page_config(
    page_title = "Heart Disease Prediction App",
    layout = "centered",
)

st.title("Heart Disease Prediction")
st.write("Enter patient details below:")

# Input fields
age = st.number_input(
    "Age of patient", 
    min_value=1, 
    max_value=120, 
    value=45
    )
resting_bp = st.number_input(
    "Resting Blood Pressure",
    min_value=80,
    max_value=200, 
    value=120)
cholesterol = st.number_input(
    "Cholesterol", 
    min_value=0, 
    max_value=600, 
    value=200)
max_hr = st.number_input(
    "Max Heart Rate", 
    min_value=50, 
    max_value=250, 
    value=150)
oldpeak = st.number_input(
    "Oldpeak",
    min_value=0.0,
    max_value=10.0,
    value=1.0)

sex = st.selectbox("Sex", 
                   ["M", "F"])

chest_pain = st.selectbox("Chest Pain Type", 
                          ["TA", "ATA", "NAP", "ASY"])

fasting_bs = st.selectbox("Fasting Blood Sugar", 
                          [0, 1])

resting_ecg = st.selectbox("Resting ECG", 
                           ["Normal", "ST", "LVH"])

exercise_angina = st.selectbox("Exercise Induced Angina", 
                               ["Y", "N"])

st_slope = st.selectbox("ST Slope", 
                        ["Up", "Flat", "Down"])

# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame([{
        "Age": age,
        "Sex": sex,
        "ChestPainType": chest_pain,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "RestingECG": resting_ecg,
        "MaxHR": max_hr,
        "ExerciseAngina": exercise_angina,
        "Oldpeak": oldpeak,
        "ST_Slope": st_slope
    }])

    # Encode input
    input_encoded = pd.get_dummies(input_data)

    # Match training columns
    input_encoded = input_encoded.reindex(columns=columns, fill_value=0)

    # Prediction
    prediction = model.predict(input_encoded)

    # Output result
    if prediction[0] == 1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease!!")
