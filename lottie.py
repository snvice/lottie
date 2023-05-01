import streamlit as st
import re

# Define a function to remove date and sender names from text using regex
def clean_text(text):
    pattern = r'^\d{2}/\d{2}/\d{4}, \d{2}:\d{2} - .*?:\s'
    return re.sub(pattern, '', text, flags=re.MULTILINE)

# Define the Streamlit app
def app():
    st.title("Text File Uploader")
    st.write("Upload a text file to clean its contents.")

    # Create a file uploader component
    file = st.file_uploader("Choose a text file", type=["txt"])

    # If a file is uploaded, clean its contents and display them
    if file is not None:
        text = file.read().decode('utf-8')
        cleaned_text = clean_text(text)
        st.code(text)
        st.write("Cleaned text:")
        st.code(cleaned_text)

# Run the Streamlit app
if __name__ == "__main__":
    app()
