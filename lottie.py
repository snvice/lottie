import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load the Lottie animation from a URL
lottie_url_hello = "https://assets9.lottiefiles.com/packages/lf20_5lTxAupekw.json"
lottie_hello = load_lottieurl(lottie_url_hello)

# Set up the title with a larger font size and a custom color
title = "<h1 style='text-align: center; color: #fc6203; font-size: 48px;'>Scan Squad</h1>"
st.markdown(title, unsafe_allow_html=True)

# Display the title and animation in a 2-column layout
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown(title, unsafe_allow_html=True)
with col2:
    st_lottie(lottie_hello, speed=1, width=200, height=200, key="hello")
