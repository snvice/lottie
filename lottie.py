import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load the Lottie animation from a URL
lottie_url = "https://assets10.lottiefiles.com/packages/lf20_OQ3q3qHR.json"
lottie_json = load_lottieurl(lottie_url)

# Display the animation with reduced dimensions and centered
st.markdown(
    f"<div style='display: flex; justify-content: center; align-items: center; width: 100%; height: 100vh;'>"
    f"<div style='width: 400px; height: 400px;'>"
    f"{st_lottie(lottie_json, speed=1, width=400, height=400, key='my_lottie')}"
    f"</div>"
    "</div>",
    unsafe_allow_html=True,
)
