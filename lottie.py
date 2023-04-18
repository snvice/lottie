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
lottie_url_hello = "https://assets3.lottiefiles.com/packages/lf20_C67qsN3hAk.json"
lottie_hello = load_lottieurl(lottie_url_hello)

# Create a centered container and place the animation inside it
container = st.beta_container()
with container:
    st_lottie(lottie_hello, speed=1, width=150, height=150, key="hello")
