import streamlit as st
import re
from github import Github
from github import InputFileContent

# Define GitHub credentials
github_username = "snvice"
github_password = "samngere123!!"
repository_name = "lottie"

# Authenticate to GitHub
g = Github(github_username, github_password)
repo = g.get_user().get_repo(repository_name)

# Define a function to remove date and sender names from text using regex
def clean_text(text):
    pattern = r'^\d{2}/\d{2}/\d{4}, \d{2}:\d{2} - .*?:\s'
    return re.sub(pattern, '', text, flags=re.MULTILINE)

# Define the Streamlit app
def app():
    st.title("Text File Uploader and GitHub Saver")
    st.write("Upload a text file to clean its contents and save it to GitHub.")

    # Create a file uploader component
    file = st.file_uploader("Choose a text file", type=["txt"])

    # If a file is uploaded, clean its contents, save it to GitHub, and display success message
    if file is not None:
        text = file.read().decode('utf-8')
        cleaned_text = clean_text(text)

        # Upload file to GitHub
        file_name = file.name
        file_content = InputFileContent(cleaned_text)
        repo.create_file(file_name, "commit message", file_content)

        st.write("File uploaded to GitHub!")
    
# Run the Streamlit app
if __name__ == "__main__":
    app()
