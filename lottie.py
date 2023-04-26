import streamlit as st
import styled

# Define the styled component for the title
StyledTitle = styled.h1`
  font-size: 3rem;
  font-weight: bold;
  color: #333;
  animation: pulse 2s infinite;
  
  @keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
  }
`

# Render the styled title component in Streamlit
st.markdown(StyledTitle("My Animated Title"))
