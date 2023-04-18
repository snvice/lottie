import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Define a function to load the Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Specify the URL of the Lottie animation
lottie_url_hello = "https://assets9.lottiefiles.com/packages/lf20_5lTxAupekw.json"

# Load the Lottie animation
lottie_hello = load_lottieurl(lottie_url_hello)

# Set up the title with a larger font size and a custom color
st.markdown("<h1 style='text-align: center; color: #fc6203; font-size: 48px;'>Scan Squad</h1>", unsafe_allow_html=True)

# Display the Lottie animation and the title side by side
col1, col2 = st.beta_columns([1, 1])
with col1:
    st_lottie(lottie_hello, speed=1, width=200, height=200, key="hello")
with col2:
    st.write("Welcome to Scan Squad! This is a demo of how to use Lottie animations in your Streamlit app.")
