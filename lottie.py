import streamlit as st
from streamlit_lottie import st_lottie

# Specify the URL of the Lottie animation
url = "https://assets9.lottiefiles.com/packages/lf20_5lTxAupekw.json"

# Display the animation
st_lottie(url, speed=1, width=300, height=300, key="lottie")
