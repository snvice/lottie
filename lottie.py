import streamlit as st
import re
import string
import nltk
from nltk.corpus import stopwords
from collections import Counter

# Define a function to clean text and count word frequency
def clean_text(text):
    # Remove date and sender names using regex
    pattern = r'^\d{2}/\d{2}/\d{4}, \d{2}:\d{2} - .*?:\s'
    text = re.sub(pattern, '', text, flags=re.MULTILINE)
    
    # Remove file attachment lines using regex
    pattern = r'^IMG-\d{8}-WA\d{4}\.jpg \(file attached\)\n'
    text = re.sub(pattern, '', text, flags=re.MULTILINE)
    
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    # Split the text into individual words
    words = text.split()

    # Define custom stop words
    custom_stop_words = {'file', 'attached'}

    # Combine custom stop words with NLTK stop words
    stop_words = set(stopwords.words('english')).union(custom_stop_words)

    # Remove stop words
    words = [word for word in words if word not in stop_words]

    # Count the frequency of each word
    word_counts = Counter(words)

    # Print the results in a table format
    st.write("Top 5 words by frequency:")
    table_data = [["Word", "Frequency"]]
    for word, count in word_counts.most_common(5):
        table_data.append([word, count])
    st.table(table_data)

    # Return the cleaned text
    return text

# Define the Streamlit app
def app():
    st.title("Text File Uploader")
    st.write("Upload a text file to clean its contents and count word frequency.")

    # Create a file uploader component
    file = st.file_uploader("Choose a text file", type=["txt"])

    # If a file is uploaded, clean its contents and display them
    if file is not None:
        text = file.read().decode('utf-8')
        cleaned_text = clean_text(text)
        st.write("Cleaned text:")
        st.code(cleaned_text)

# Run the Streamlit app
if __name__ == "__main__":
    app()
