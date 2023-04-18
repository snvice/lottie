import streamlit as st
from streamlit_lottie import st_lottie

# Load the Lottie animation from a file
with open('path/to/animation.json', 'r') as f:
    animation_data = f.read()

# Display the animation
st_lottie(animation_data, speed=1, width=300, height=300, key="lottie")
