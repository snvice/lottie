import streamlit as st

st.markdown(
    """
    <style>
    @keyframes pulse {
        0% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.1);
        }
        100% {
            transform: scale(1);
        }
    }
    .title {
        animation: pulse 2s ease-in-out infinite;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Pulsing Title")
