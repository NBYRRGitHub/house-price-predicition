import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Sample training data (replace with your dataset)
data = pd.DataFrame({
    "area": [1000, 1500, 2000],
    "bedrooms": [2, 3, 4],
    "location_Urban": [1, 0, 1],
    "location_Suburban": [0, 1, 0],
    "price": [50, 70, 90]
})

X = data.drop("price", axis=1)
y = data["price"]

model = RandomForestRegressor()
model.fit(X, y)

# UI
st.title("🏠 House Price Prediction")

area = st.slider("Area (sq ft)", 500, 5000, 1000)
bedrooms = st.slider("Bedrooms", 1, 5, 2)
location = st.selectbox("Location", ["Urban", "Suburban"])

# Encoding
loc_urban = 1 if location == "Urban" else 0
loc_suburban = 1 if location == "Suburban" else 0

input_data = pd.DataFrame([[area, bedrooms, loc_urban, loc_suburban]],
                          columns=X.columns)

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Price: ₹ {prediction[0]} Lakhs")
