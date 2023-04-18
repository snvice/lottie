import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Download the Lottie animation from a URL
url = 'https://raw.githubusercontent.com/snvice/lottie/main/giraffe.json'
response = requests.get(url)
animation_data = response.text

# Display the animation
st_lottie(animation_data, speed=1, width=300, height=300, key="lottie")
