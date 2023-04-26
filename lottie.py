import streamlit as st
import styled_components as styled

# Define a styled title component using styled-components
Title = styled.h1("""
  font-size: 3rem;
  font-weight: bold;
  color: orange;
  text-align: center;
""")

# Render the styled title component in the Streamlit app
st.write(Title("My Orange Title"))
