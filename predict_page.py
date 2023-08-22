import streamlit as st
import pickle
import numpy as np
from PIL import Image, ImageEnhance


# Custom CSS styles
custom_css = """
<style>
    .stApp {
        background-color: #f8f8f8;
    }
</style>
"""

def load_model():
    with open('vineyard.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
melbourne_model = data['model']

def show_pred():
    st.markdown(custom_css, unsafe_allow_html=True)
    st.title("Vineyard Evaporation Prediction Model🧠")
    max_temp = st.slider("Maximum temperature",5,35,15)
    rainfall = st.slider("Rainfall",0,16,5)
    windgust = st.slider("Windgust",15,60,35)
    humidity = st.slider("Relative humidity",40,100,70)
    ok = st.button("Calculate Evaporation")
    if ok:
        X = np.array([[max_temp, rainfall, windgust, humidity]])
        X = X.astype(float)
        
        evaporation = melbourne_model.predict(X)
        st.subheader(f"The estimated evaporation is {evaporation[0]:.2f}")
