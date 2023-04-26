import streamlit as st
from streamlit.hashing import _CodeHasher
import SessionState

# Home page
def home():
    st.title("Welcome to my Streamlit app!")
    # Add your content for the home page here

# Second page
def second_page():
    st.title("This is the second page!")
    # Add your content for the second page here

# Initialize SessionState
state = SessionState.get(page_name="Home")

# Sidebar navigation
menu = ["Home", "Second Page"]
choice = st.sidebar.selectbox("Select a page", menu)

# Display the selected page
if choice == "Home":
    state.page_name = "Home"
elif choice == "Second Page":
    state.page_name = "Second Page"

if state.page_name == "Home":
    home()
elif state.page_name == "Second Page":
    second_page()
