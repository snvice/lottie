
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.markdown(
    """
    <style>
    .title {
        position: relative;
        animation: moveTitle 2s linear infinite alternate;
    }

    @keyframes moveTitle {
        from { left: 0px; }
        to { left: 10px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Animated Title")

