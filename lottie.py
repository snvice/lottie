import streamlit as st
import re
import string
import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import io
import requests


# Download the NLTK stop words
nltk.download('stopwords')

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

    # Display the top 5 words by frequency in a table
    st.write("Top 5 words by frequency:")
    table_data = [["Word", "Frequency"]]
    for word, count in word_counts.most_common(5):
        table_data.append([word, count])
    st.table(table_data)

    # Generate the word cloud
    wordcloud = WordCloud(background_color="black", 
                          width=800, 
                          height=800, 
                          max_words=100, 
                          colormap="Dark2",
                          stopwords=stop_words, 
                          contour_width=3, 
                          contour_color="steelblue")
    wordcloud.generate_from_frequencies(word_counts)

    # Display the word cloud
    st.write("Word cloud:")
    st.image(wordcloud.to_array(), use_column_width=True)
    st.write("")

    # Download the word cloud as a PNG file
    png_image = wordcloud.to_image()
    with io.BytesIO() as bytes_io:
        png_image.save(bytes_io, format='PNG')
        png_bytes = bytes_io.getvalue()
    st.download_button(
        label="Download word cloud",
        data=png_bytes,
        file_name="wordcloud.png",
        mime="image/png",
    )

    # Return the cleaned text
    return text

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
        return r.json()

    




# Define the Streamlit app
def app():
    st.title("ChatWiz")
    st.write("Create a unique word cloud from your chat messages!")
    
    # Load the Lottie animation from a URL
    lottie_url_hello = "https://assets8.lottiefiles.com/private_files/lf30_mjuiybtp.json"
    lottie_hello = load_lottieurl(lottie_url_hello)

    # Display the animation with reduced dimensions
    st_lottie(lottie_hello, speed=1, width=225, height=225, key="hello")

    # Create a file uploader component
    file = st.file_uploader("Choose a text file", type=["txt"])

    # If a file is uploaded, clean its contents and display them
    if file is not None:
        text = file.read().decode('utf-8')
        cleaned_text = clean_text(text)
        
    
    
# Run the app
if __name__ == '__main__':
    app()
