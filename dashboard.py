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
</style>
"""

# Data fetching via API
api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/birdwood%2C%20south%20australia?unitGroup=metric&include=days&key=CBWQ6NTRW2GUF443E4WZ7XLGM&contentType=csv"

def fetch_data(api_url):
    response = requests.get(api_url)
    csv_data = response.content
    df = pd.read_csv(io.BytesIO(csv_data))
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['interpreted_date'] = df['datetime'].dt.strftime('%d %B, %Y')
    return df

df = fetch_data(api_url)
# Display today
first_datetime = df.loc[0, 'interpreted_date']


# Create Streamlit app and display dashboard
def show_dashboard():
    st.markdown(custom_css, unsafe_allow_html=True)
    st.title('🍇Vineyard Dashboard')
    st.write(f"Today: {first_datetime}")

    col1, col2 = st.columns(2)

    # Rainfall Over Time chart
    with col1:
        st.subheader('🌧️Rainfall Over Time')
        st.area_chart(data=df, x='datetime', y='precip', use_container_width=True)

    # Temperature Over Time chart
    with col2:
        st.subheader('☀️Temperature Over Time')
        st.line_chart(data=df, x='datetime', y='temp', use_container_width=True)



    