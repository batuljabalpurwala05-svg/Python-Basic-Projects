import streamlit as st
import joblib
import pandas as pd

# Load saved model and columns
model = joblib.load('C:\\Users\\batul\\OneDrive\\Desktop\\ITR_Projects\\Model_Student\\student_model.pkl')
columns = joblib.load('C:\\Users\\batul\\OneDrive\\Desktop\\ITR_Projects\\Model_Student\\columns.pkl')
scaler = joblib.load('C:\\Users\\batul\\OneDrive\\Desktop\\ITR_Projects\\Model_Student\\scaler.pkl')

st.set_page_config(
    page_title = "Student dropout Prediction App",
    layout = "centered",
)

st.title("Student dropout Prediction")
st.write("Enter student details below:")
age = st.number_input(
    "Enter age :",
    min_value=1,
    max_value=100,
    value=50)

gender = st.selectbox(
    "Gender :",
    ['Male','Female'])

income = st.number_input(
    "Family Income :",
    min_value=25000,
    max_value=330000,
    value = 100000)

study_hours = st.number_input(
    "Student's study hours per day",
    min_value=0,
    max_value=10,
    value=5)

attendance = st.number_input(
    "Attendance Rate",
    min_value=30,
    max_value=100,
    value=75)

part_time = st.selectbox(
    "Part Time Job",
    ['Yes','No'])

scholar = st.selectbox(
    "Scholarship",
    ['Yes','No'])

dept = st.selectbox(
    "Department",
    ['Arts', 'Engineering', 'CS', 'Business', 'Science'])

parent_ed = st.selectbox(
    "Parental Education",
    ['High School', 'Bachelor', 'Master', 'PhD'])

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Family Income": income,
        "Study Hours": study_hours,
        "Attendance Rate": attendance,
        "Part Time Job": part_time,
        "Scholarship": scholar,
        "Department": dept,
        "Parental Education": parent_ed,
    }])
    # Encode input
    input_encoded = pd.get_dummies(input_data)
    
    # Match training columns
    input_encoded = input_encoded.reindex(columns=columns, fill_value=0)
    
    # Prediction
    prediction = model.predict(input_encoded)
    
    # Output result
    if prediction[0] == 1:
            st.error("High Chance of Dropout")
    else:
            st.success("Low Chance of Dropout")