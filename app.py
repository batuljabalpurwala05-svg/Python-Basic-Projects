import streamlit as st
import pandas as pd
import joblib
# Model Fetching
model = joblib.load('C:\\Users\\batul\\OneDrive\\Desktop\\ITR_Projects\\model.pkl')
scaler = joblib.load('C:\\Users\\batul\\OneDrive\\Desktop\\ITR_Projects\\scaler.pkl')
columns = joblib.load('C:\\Users\\batul\\OneDrive\\Desktop\\ITR_Projects\\columns.pkl')
# User Interface
st.set_page_config(
	page_title = "Ford Car Price Predictor",
	layout = "centered"
)
st.title("Ford Car Price Prediction")
st.write("Enter the car details below to predict its selling price :")
# Creating numerical input fields
year = st.number_input(
    "Manufacturing Year", 
    min_value=1990, 
    max_value=2026, 
    value=2020)
mileage = st.number_input(
    "Mileage",
    min_value=0,
    max_value=500000,   
    value=10000)
tax = st.number_input(
    "Tax",
    min_value=0,    
    max_value=10000,
    value=150)
mpg = st.number_input(
    "Miles per Gallon (MPG)",
    min_value=0.0,
    max_value=100.0,
    value=30.0)
engineSize = st.number_input(
    "Engine Size (L)",
    min_value=0.0,
    max_value=10.0,
    value=2.0)

# Creating categorical input fields
transmission = st.selectbox(
    "Transmission Type",
    options=["Manual", "Automatic"]
)
fuel = st.selectbox(
    "Fuel Type",
    options=["Petrol", "Diesel", "Hybrid", "Electric"]
)
car_models = st.text_input(
    "Car Model",
    value="Focus"
)
if st.button("Predict"):

    input_df = pd.DataFrame({
        "year":[year],
        "mileage":[mileage],
        "tax":[tax],
        "mpg":[mpg],
        "engineSize":[engineSize],
        "transmission":[transmission],
        "fuelType":[fuel],
        "model":[car_models]
    })

    # Encode
    input_df = pd.get_dummies(input_df)

    # Match columns
    input_df = input_df.reindex(columns=columns, fill_value=0)

    # Scale
    numeric_feat = ["year", "mileage", "tax", "mpg", "engineSize"]
    input_df[numeric_feat] = scaler.transform(input_df[numeric_feat])

    # Predict
    prediction = model.predict(input_df)

    st.success(f"Predicted Price: £{prediction[0]:,.2f}")