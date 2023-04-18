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
lottie_url = "https://assets3.lottiefiles.com/packages/lf20_W5U2ua.json"
lottie_json = load_lottieurl(lottie_url)

# Display the animation with reduced dimensions and centered
st.markdown("<div style='text-align: center;'>"
            f"{st_lottie(lottie_json, speed=1, width=300, height=300, key='my_lottie')}"
            "</div>", unsafe_allow_html=True)
