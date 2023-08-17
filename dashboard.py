import streamlit as st
import numpy as np
import pandas as pd
import requests
import io
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from PIL import Image, ImageEnhance

# Set Streamlit page configuration
st.set_page_config(
    page_title="Vineyard Dashboard",
    page_icon="🍇",
    layout="wide"
)

# Custom CSS styles
custom_css = """
<style>
    .stApp {
        background-color: #f8f8f8;
    }
    .stButton {
        background-color: #ff5722 !important;
        color: white !important;
        border: none !important;
        border-radius: 4px;
        padding: 10px 20px !important;
        cursor: pointer !important;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    .stTextInput {
        background-color: #ffffff !important;
        color: #444444 !important;
        border: 1px solid #cccccc !important;
        border-radius: 4px;
        padding: 8px !important;
    }
    .stMarkdown {
        color: #555555 !important;
        line-height: 1.6;
    }
    .stDataFrame {
        border-collapse: collapse;
        margin: 10px 0;
        font-size: 14px;
        width: 100%;
    }
    .stDataFrame th, .stDataFrame td {
        padding: 10px 15px;
        border: 1px solid #dddddd;
        text-align: left;
    }
    .stLineChart .highcharts-background {
        fill: transparent !important;
    }
    .custom-sidebar {
        position: relative;
    }
    .image-container {
        margin-left: auto;
        margin-right: 0;
        display: block;
        max-width: 100%;
        height: auto;
    }
</style>
"""

# Data fetching via API
api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/birdwood%2C%20south%20australia?unitGroup=metric&include=days&key=CBWQ6NTRW2GUF443E4WZ7XLGM&contentType=csv"
response = requests.get(api_url)
csv_data = response.content
df = pd.read_csv(io.BytesIO(csv_data))

# Correct date format
df['datetime'] = pd.to_datetime(df['datetime']).dt.strftime('%d-%m-%Y')
# Correct data type
df['datetime'] = pd.to_datetime(df['datetime'])
# Interpreted date format
df['interpreted_date'] = df['datetime'].dt.strftime('%d %B, %Y')
# Display today
first_datetime = df.loc[0, 'interpreted_date']

image_path = "DTA Logo.png"
logo = Image.open(image_path)
new_size = (150, 100)
logo = logo.resize(new_size)

# Create Streamlit app and display dashboard
def show_dashboard():
    st.markdown(custom_css, unsafe_allow_html=True)
    st.title('🍇Vineyard Dashboard')
    st.write(f"Today: {first_datetime}")

    col1, col2 = st.columns(2)

    # Rainfall Over Time chart
    with col1:
        st.subheader('🌧️Rainfall Over Time')
        st.line_chart(df.set_index('datetime')['precip'], use_container_width=True)

    # Temperature Over Time chart
    with col2:
        st.subheader('☀️Temperature Over Time')
        st.line_chart(df.set_index('datetime')['temp'], use_container_width=True)

    # DTA logo
    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        st.image(logo, use_column_width=False, width=new_size[0])



    