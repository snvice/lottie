import streamlit as st
from streamlit.components.v1 import components

# Home page
def home():
    st.title("Welcome to my Streamlit app!")
    # Add your content for the home page here

# Second page
def second_page():
    st.title("This is the second page!")
    # Add your content for the second page here

# Sidebar navigation
menu = ["Home", "Second Page"]
choice = st.sidebar.selectbox("Select a page", menu)

# Display the selected page
if choice == "Home":
    home()
elif choice == "Second Page":
    second_page()
