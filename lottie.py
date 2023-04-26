import streamlit as st
import styled_components as styled

# Define a styled title component using styled-components
Title = styled.h1`
  font-size: 3rem;
  font-weight: bold;
  color: #333;
  text-align: center;
  animation: fade-in 1s;

  @keyframes fade-in {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
`

# Render the styled title component in the Streamlit app
st.write(Title("My Animated Title"))
