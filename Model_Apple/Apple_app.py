import streamlit as st
import pandas as pd
import joblib

model = joblib.load('C:\\Users\\batul\\OneDrive\\Desktop\\ITR_Projects\\Model_Apple\\model.pkl')
scaler = joblib.load('C:\\Users\\batul\\OneDrive\\Desktop\\ITR_Projects\\Model_Apple\\scaler.pkl')
columns = joblib.load('C:\\Users\\batul\\OneDrive\\Desktop\\ITR_Projects\\Model_Apple\\columns.pkl')

st.set_page_config(
    page_title = "Apple Product Price Predictor",
    layout = "centered")
st.title("Apple Product Price Prediction")
st.write("Enter the Apple product details below to predict its current price :")

# Numerical Features
review = st.number_input(
    "Enter the number of reviews for the product:", 
    min_value=0,
    max_value=10000, 
    step=1)
rating = st.number_input(
    "Enter the rating of the product (0-5):", 
    min_value=0.0, 
    max_value=5.0, 
    step=0.1)
discount = st.number_input(
    "Enter the discount percentage for the product:", 
    min_value=0.0, 
    max_value=100.0, 
    step=0.1)

# Categorical Features
plat = st.selectbox(
    "Select Platform:",
    ['Amazon', 'Flipkart']
)
product = st.selectbox(
    "Select Product:",
    ['iPhone', 'iPad', 'Watch', 'Mac']
)
apple_model = st.selectbox(
    "Select Apple Model:",
    [     'Apple Watch Series 6 (44mm)',          'iPad Air (4th Gen) 64GB',
                   'iPhone 12 64GB',              'iPhone 12 Pro 128GB',
             'MacBook Air M1 256GB',      'iPad Pro 11-inch (M1) 128GB',
                  'iPhone 13 128GB',          'iPhone 13 Pro Max 256GB',
              'iPad (9th Gen) 64GB',      'Apple Watch Series 7 (45mm)',
 'MacBook Pro 14-inch M1 Pro 512GB',          'iPad Air (5th Gen) 64GB',
             'MacBook Air M2 256GB',      'Apple Watch Series 8 (45mm)',
                  'iPhone 14 128GB',              'iPhone 14 Pro 128GB',
                'Apple Watch Ultra',    'iPad Pro 12.9-inch (M2) 256GB',
 'MacBook Pro 14-inch M2 Pro 512GB',      'Apple Watch Series 9 (45mm)',
              'Apple Watch Ultra 2',                  'iPhone 15 128GB',
          'iPhone 15 Pro Max 256GB', 'MacBook Pro 14-inch M3 Pro 512GB',
             'MacBook Air M3 256GB',      'iPad Pro 11-inch (M4) 256GB',
                  'iPhone 16 128GB',              'iPhone 16 Pro 256GB',
      'Apple Watch Series X (45mm)', 'MacBook Pro 14-inch M4 Pro 512GB',
                  'iPhone 17 128GB']
)

con = st.selectbox(
    "Select Condition:",    
    ['New', 'Renewed/Refurbished']
)
stock = st.selectbox(
    "Select Stock Status:",
    ['In Stock', 'Out of Stock', 'Low Stock']
)
if (st.button("Predict")):
    input_df = pd.DataFrame({
        "Reviews_Count":[review],
        "Rating":[rating],
        "Discount_Pct":[discount],
        "Platform":[plat],
        "Product":[product],
        "Model":[apple_model],
        "Condition":[con],
        "Stock_Status":[stock]
        
    })

    # Encode
    input_df = pd.get_dummies(input_df)

    # Match training columns
    input_df = input_df.reindex(columns=columns, fill_value=0)

    input_df = input_df[columns]

    numerical_columns = ['Reviews_Count', 'Rating', 'Discount_Pct']
    num_scaled = scaler.transform(input_df[numerical_columns].values)
    input_df[numerical_columns] = num_scaled

    # Predict
    prediction = model.predict(input_df)

    st.success(f"The predicted price of the Apple product is: ${prediction[0]:.2f}")