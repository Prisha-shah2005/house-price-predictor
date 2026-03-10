import streamlit as st
from app.predict import predict_price

st.set_page_config(page_title="House Price Predictor")

st.title("🏠 Bangalore House Price Predictor")

location = st.text_input("Location")

sqft = st.number_input("Square Feet", min_value=0)

bath = st.number_input("Bathrooms", min_value=0)

bhk = st.number_input("BHK", min_value=0)

if st.button("Predict Price"):

    if location == "":
        st.warning("Please enter location")

    else:
        price = predict_price(location, sqft, bath, bhk)
        st.success(f"Estimated Price: ₹ {price} Lakhs")