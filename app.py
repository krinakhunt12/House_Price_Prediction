import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load("house_price_model.joblib")

# Page settings
st.set_page_config(page_title="🏡 House Price Predictor", page_icon="💰", layout="centered")

# Title
st.title("🏡 House Price Prediction App")
st.markdown("### Predict the price of a house based on its features")

# Sidebar for user inputs
st.sidebar.header("Enter House Features")

# Numeric inputs (arranged in two columns)
col1, col2 = st.sidebar.columns(2)

area = col1.number_input("Area (sqft)", min_value=500, max_value=10000, value=1500, step=50)
bedrooms = col2.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = col1.number_input("Bathrooms", min_value=1, max_value=10, value=2)
stories = col2.number_input("Stories", min_value=1, max_value=5, value=1)
parking = col1.number_input("Parking Spaces", min_value=0, max_value=5, value=1)

# Categorical inputs
st.sidebar.subheader("Other Features")
mainroad = st.sidebar.selectbox("Main Road", ["yes", "no"])
guestroom = st.sidebar.selectbox("Guest Room", ["yes", "no"])
basement = st.sidebar.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.sidebar.selectbox("Hot Water Heating", ["yes", "no"])
airconditioning = st.sidebar.selectbox("Air Conditioning", ["yes", "no"])
prefarea = st.sidebar.selectbox("Preferred Area", ["yes", "no"]) 
furnishingstatus = st.sidebar.selectbox("Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])

# Collect input into DataFrame
input_data = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "stories": [stories],
    "parking": [parking],
    "mainroad": [mainroad],
    "guestroom": [guestroom],
    "basement": [basement],
    "hotwaterheating": [hotwaterheating],
    "airconditioning": [airconditioning],
    "prefarea": [prefarea],
    "furnishingstatus": [furnishingstatus]
})

# Prediction section
st.subheader("📊 Prediction Result")

if st.button("🔮 Predict House Price"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"🏷️ Estimated Price: **₹ {prediction:,.0f}**")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")

# Info section
st.markdown("---")
st.markdown("✅ This app uses a **Random Forest Regressor** trained on housing data to estimate property prices. \n"
            "👉 Enter details in the sidebar and click **Predict** to see the estimated value.")
