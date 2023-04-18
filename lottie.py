import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Download the Lottie animation from a URL
url = 'https://assets9.lottiefiles.com/packages/lf20_5lTxAupekw.json'
response = requests.get(url)
animation_data = response.text

# Display the animation
st_lottie(animation_data, speed=1, width=300, height=300, key="lottie")
