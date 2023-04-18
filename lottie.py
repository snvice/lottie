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
lottie_url_hello = "https://assets7.lottiefiles.com/private_files/lf30_kbu3mkpv.json"
lottie_hello = load_lottieurl(lottie_url_hello)

# Display the animation with reduced dimensions
st_lottie(lottie_hello, speed=1, width=200, height=200, key="hello")
