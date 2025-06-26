import gradio as gr
import joblib
import numpy as np

# Load the trained model
model = joblib.load("aqi_model.pkl")

# Define prediction function
def predict_aqi(pm25, pm10, no, no2, benzene, hour, month, dayofweek, is_weekend):
    features = np.array([[pm25, pm10, no, no2, benzene, hour, month, dayofweek, is_weekend]])
    prediction = model.predict(features)[0]
    return round(prediction, 2)

# Build Gradio interface
interface = gr.Interface(
    fn=predict_aqi,
    inputs=[
        gr.Number(label="PM2.5"),
        gr.Number(label="PM10"),
        gr.Number(label="NO"),
        gr.Number(label="NO2"),
        gr.Number(label="Benzene"),
        gr.Slider(0, 23, step=1, label="Hour of Day"),
        gr.Slider(1, 12, step=1, label="Month"),
        gr.Slider(0, 6, step=1, label="Day of Week (0=Mon)"),
        gr.Radio([0, 1], label="Weekend (1=Yes, 0=No)")
    ],
    outputs=gr.Number(label="Predicted AQI"),
    title="🌫️ Delhi AQI Prediction",
    description="Enter pollution and time values to predict the Air Quality Index using a trained machine learning model."
)

# Launch the app
interface.launch()
