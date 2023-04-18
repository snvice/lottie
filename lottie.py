import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load the Lottie animation from a URL
lottie_url_hello = "https://assets7.lottiefiles.com/private_files/lf30_kbu3mkpv.json"
lottie_hello = load_lottieurl(lottie_url_hello)

# Display the animation centered on the page
st.markdown(
    f"<div style='display: flex; justify-content: center; align-items: center;'>"
    f"{st_lottie(lottie_hello, speed=1, width=300, height=300, key='hello')}"
    "</div>"
)
