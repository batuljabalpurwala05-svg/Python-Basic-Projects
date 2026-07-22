import streamlit as st
import joblib
import pandas as pd

model = joblib.load("C:\\Users\\batul\\OneDrive\\Desktop\\ITR_Projects\\Model_Bank\\model.pkl")
scaler = joblib.load("C:\\Users\\batul\\OneDrive\\Desktop\\ITR_Projects\\Model_Bank\\scaler.pkl")
columns = joblib.load("C:\\Users\\batul\\OneDrive\\Desktop\\ITR_Projects\\Model_Bank\\columns.pkl")

st.set_page_config(
    page_title = "Bank subscription Prediction App",
    layout = "centered",
)

st.title("Bank subscription Prediction")
st.write("Enter details below:")

age = st.number_input(
    "Age", 
    min_value=18, 
    max_value=100)

job = st.selectbox(
    "Job", 
    ["Admin", 
    "Technician", 
    "Services", 
    "Management"])
marital = st.selectbox(
    "Marital Status", 
    ["Single", 
    "Married"])
education = st.selectbox(
    "Education", 
    ["HighSchool", 
    "Bachelors",
    "Masters"])

housing = st.selectbox(
    "Housing Loan", 
    ["Yes", "No"])
personal = st.selectbox(
    "Personal Loan", 
    ["Yes", "No"])
contact = st.selectbox(
    "Contact Type", 
    ["Cellular", "Telephone"])

day = st.number_input(
    "Day", 
    min_value=1, 
    max_value= 31)

duration = st.number_input(
    "Duration",
    min_value=29,
    max_value=590)

if st.button("Predict"):

    input_dict = {
        "Age": age,
        "Job": job,
        "MaritalStatus": marital,
        "Education": education,
        "HousingLoan": housing,
        "PersonalLoan": personal,
        "Contact": contact,
        "Day": day,
        "Duration": duration,
        
    }
    input_df = pd.DataFrame([input_dict])
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=columns, fill_value=0)

    prediction = model.predict(input_encoded)[0]

    if prediction == 1:
        st.success("Subscribed!!")
    else:
        st.error("Not Subscribed")

