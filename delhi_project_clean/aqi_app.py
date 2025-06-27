import streamlit as st
import joblib
import numpy as np
import gdown
import os

# ==================== Load model from Google Drive ====================
@st.cache_resource
def load_model_from_drive():
    file_id = "1h5ruo8AJjFx3-XqJ2tt0LZmPN1CVl5lj"
    model_path = "aqi_model.pkl"
    
    if not os.path.exists(model_path):
        gdown.download(f"https://drive.google.com/uc?id={file_id}", model_path, quiet=False)

    return joblib.load(model_path)

# Load model
model = load_model_from_drive()

# ==================== Streamlit Page Config ====================
st.set_page_config(
    page_title="Delhi AQI Predictor",
    page_icon="🌫️",
    layout="centered"
)

# ==================== Header ====================
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #1f77b4;'>🌫️ Delhi Air Quality Index Predictor</h1>
        <p style='font-size: 18px;'>Enter real-time pollutant levels and time info to predict the AQI using a trained Machine Learning model.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==================== Input Fields ====================
col1, col2 = st.columns(2)

with col1:
    pm25 = st.number_input("PM2.5 (µg/m³)", min_value=0.0, step=1.0)
    no = st.number_input("NO (µg/m³)", min_value=0.0, step=1.0)
    benzene = st.number_input(" Benzene (µg/m³)", min_value=0.0, step=0.1)
    hour = st.slider("Hour of Day", 0, 23)

with col2:
    pm10 = st.number_input("PM10 (µg/m³)", min_value=0.0, step=1.0)
    no2 = st.number_input("NO2 (µg/m³)", min_value=0.0, step=1.0)
    month = st.slider("Month", 1, 12)
    dayofweek = st.slider("Day of Week (0 = Mon)", 0, 6)

is_weekend = st.radio("Is it a weekend?", [0, 1], horizontal=True)

# ==================== Predict Button ====================
if st.button("🔍 Predict AQI"):
    input_data = np.array([[pm25, pm10, no, no2, benzene, hour, month, dayofweek, is_weekend]])
    prediction = model.predict(input_data)[0]
    rounded_prediction = round(prediction, 2)

    # Display Result
    st.markdown(f"""
    <div style='background-color: #f0f8ff; padding: 20px; border-radius: 10px; text-align: center;'>
        <h2 style='color: #d62728;'>Predicted AQI: {rounded_prediction}</h2>
    </div>
    """, unsafe_allow_html=True)

    # AQI Category
    if rounded_prediction <= 50:
        category = "Good 😊"
        color = "#2ecc71"
    elif rounded_prediction <= 100:
        category = "Satisfactory 🙂"
        color = "#27ae60"
    elif rounded_prediction <= 200:
        category = "Moderate 😐"
        color = "#f1c40f"
    elif rounded_prediction <= 300:
        category = "Poor 😷"
        color = "#e67e22"
    elif rounded_prediction <= 400:
        category = "Very Poor 🤢"
        color = "#e74c3c"
    else:
        category = "Severe 🛑"
        color = "#c0392b"

    st.markdown(f"""
        <div style='text-align:center; padding: 10px; margin-top:10px;'>
            <span style='color:{color}; font-size: 22px;'>Air Quality Category: <b>{category}</b></span>
        </div>
    """, unsafe_allow_html=True)

# ==================== Footer ====================
st.markdown("---")
st.caption("🔧 Built by Arya Giri | Sophomore, IIT BHU")
