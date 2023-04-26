import streamlit as st
import time

st.title("Color-changing Title")

while True:
    st.markdown(
        f"""
        <style>
        .title {{
            color: {'red'};
            transition: all 1s;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    time.sleep(1)
    st.markdown(
        f"""
        <style>
        .title {{
            color: {'orange'};
            transition: all 1s;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    time.sleep(1)
    st.markdown(
        f"""
        <style>
        .title {{
            color: {'yellow'};
            transition: all 1s;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    time.sleep(1)
