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
lottie_url = "https://assets7.lottiefiles.com/private_files/lf30_kbu3mkpv.json"
lottie_json = load_lottieurl(lottie_url)

# Display the animation with reduced dimensions and centered
st.markdown("<div style='text-align: center;'>"
            f"<div style='display: inline-block;'>"
            f"{st_lottie(lottie_json, speed=1, width=150, height=150, key='my_lottie')}"
            f"</div>"
            "</div>", unsafe_allow_html=True)
