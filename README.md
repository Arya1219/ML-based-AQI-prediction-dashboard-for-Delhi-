# Delhi AQI Prediction Dashboard (Machine Learning Based)

This project is a machine learning-powered web application designed to predict the **Air Quality Index (AQI)** in Delhi based on real-time pollutant data. The goal is to make AQI predictions accessible and understandable through an interactive Streamlit dashboard.

## Project Overview

Delhi is known to experience hazardous levels of air pollution. Real-time AQI prediction can help raise awareness, inform residents, and contribute to better environmental decision-making. This tool uses trained machine learning models to predict AQI from key pollutant levels and time-based features like hour and month.

## Features

- **AQI prediction** using trained Random Forest model.
- Inputs include: PM2.5, PM10, NO, NO2, Benzene, hour, month, day of week, and weekend flag.
- Categorizes predicted AQI into **Good, Moderate, Poor**, etc. based on Indian AQI standards.
- Clean and responsive user interface using **Streamlit**.
- Model loaded externally via **Google Drive** due to GitHub size limits.

##  Technologies Used

- Python (Pandas, NumPy, Scikit-learn, Joblib)
- Streamlit (for the web app interface)
- gdown (to download model from Google Drive)
- Matplotlib/Seaborn (for EDA and feature importance — used in Jupyter Notebook)
- Jupyter Notebook (for training, evaluation, and experimentation)

 Folder Structure
.devcontainer
delhi_project_clean : aqi_app.py ,requirements.txt
project1.ipynb


## Model Hosting

Since GitHub restricts file sizes to 100MB, the `.pkl` file (approx. 315MB) is hosted on **Google Drive** and downloaded programmatically at runtime.

```python
import gdown
gdown.download("https://drive.google.com/uc?id=1h5ruo8AJjFx3-XqJ2tt0LZmPN1CVl5lj", "aqi_model.pkl", quiet=False)

🌐 Hosted Web App
The application is publicly available at:
https://delhiaqipredictor.streamlit.app/

##Model Performance

Final model: Random Forest Regressor with engineered time-based features.
Mean Absolute Error (MAE): ~36.30
R² Score: ~0.83
Performance improved after adding temporal context (hour, month, weekend).

👨‍💻 Author
Arya Giri
Sophomore, B.Tech Biomedical Engineering
Indian Institute of Technology (BHU), Varanasi
Email: iriarya72@gmail.com]
GitHub: https://github.com/Arya1219

