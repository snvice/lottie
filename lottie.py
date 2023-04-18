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

# Calculate the horizontal center of the page
left_margin = (st._get_report_ctx().width - 150) / 2

# Display the animation centered on the page with reduced dimensions
st_lottie(lottie_hello, speed=1, width=150, height=150, key="hello", 
          default_renderer="svg", # Use the SVG renderer to center the animation
          style={"position": "relative", "left": f"{left_margin}px"})

