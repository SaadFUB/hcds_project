import streamlit as st
import pandas as pd
import numpy as np

# st.title("How does our tool work?")
st.markdown("<h2 style='text-align: center;'>How does our tool work?</h2>", unsafe_allow_html=True)
st.markdown("---")

# st.markdown("#### Models", unsafe_allow_html=True)

st.title("Models used")
with st.container(border=True):

    left, middle, right = st.columns([1, 2, 1])

    # with middle: 
    #     st.title("How does our tool work?")
    
    # st.markdown("#### Models", unsafe_allow_html=True)

    left, middle, right = st.columns([1, 1, 1])

    with left:
        st.markdown("<div style='text-align: center; font-weight: bold;'>Logistic Regression</div><br>", unsafe_allow_html=True)
        st.markdown("""<div style='text-align: center;'> A statistical model that predicts the probability of a binary outcome (like "at risk" or "not at risk") based on input features. It’s simple, fast, and works well when the relationship between features and outcome is mostly linear. </div>""", unsafe_allow_html=True)
    with middle: 
        st.markdown("<div style='text-align: center; font-weight: bold;'>Random Forest</div><br>", unsafe_allow_html=True)
        st.markdown("""<div style='text-align: center;'> An ensemble learning method that builds many decision trees and combines their results to make a more accurate and robust prediction. It’s good at handling complex data and reducing overfitting. </div>""", unsafe_allow_html=True)
    with right:
        st.markdown("<div style='text-align: center; font-weight: bold;'>Neural Network</div><br>", unsafe_allow_html=True)
        st.markdown("""<div style='text-align: center;'>A machine learning model inspired by the human brain, made up of layers of interconnected nodes (“neurons”). It can learn complex patterns in data, making it powerful for capturing subtle relationships between features. </div>""", unsafe_allow_html=True)

    left, middle, right = st.columns([1, 1, 1])

# st.markdown("#### Training dataset and metadata", unsafe_allow_html=True)

# Reading and displaying metadata from Git repo
with open("../metadata.md", "r") as f:
    metadata_content = f.read()
st.markdown(metadata_content, unsafe_allow_html=True)




