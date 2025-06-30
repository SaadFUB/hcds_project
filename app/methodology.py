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

st.markdown("### Other important concepts")

with st.container():
    left, right = st.columns(2)

    with left:
        st.markdown("<div style='font-weight: bold;'>Confusion Matrix</div>", unsafe_allow_html=True)
        st.markdown("A table that shows how well a model did at telling apart two different occurrences (binary: 0 or 1). It counts the number of correct and wrong predictions. In our model cases, it refers to how many times the Alzheimer’s diagnosis was correct and how many times it was not.", unsafe_allow_html=True)

        st.markdown("<div style='font-weight: bold;'>Model Accuracy</div>", unsafe_allow_html=True)
        st.markdown("The percentage of times a model was right when predicting if someone has Alzheimer's or not. The higher the accuracy, the better the model is at making correct predictions. The accuracy formula is correct decisions divided by all decisions.", unsafe_allow_html=True)

    with right:
        st.markdown("<div style='font-weight: bold;'>Fairness</div>", unsafe_allow_html=True)
        st.markdown("A model is fair if it treats different groups of people equally. Our models should work just as well for patients of different education levels or genders without bias. Fairness is a key pillar of ethical decision making.", unsafe_allow_html=True)

        st.markdown("<div style='font-weight: bold;'>Feature Importance</div>", unsafe_allow_html=True)
        st.markdown("Shows which factors in the data matter most for predicting Alzheimer's. For example, it might show that memory test scores or brain scan results have a big impact on the prediction.", unsafe_allow_html=True)



