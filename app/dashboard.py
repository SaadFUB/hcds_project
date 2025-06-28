import streamlit as st
import pandas as pd
import numpy as np


with st.container(border=True, height=500):

    for i in range(5):
        left, middle, right = st.columns([2, 1, 2])

        if i == 0:
            middle.container(height=100, border=False)
        if i == 1:
            with middle:
                st.title("Welcome!")
        elif i == 2:
            with middle:
                st.write("This application helps you predict and analyze the risk of Alzheimer's.")
        elif i == 3:
            with middle:
                if st.button("Make a prediction", key="prediction_btn", use_container_width=True):
                    st.switch_page("prediction.py")
        elif i == 4:
            middle.container(height=100, border=False)

with st.container():
    left, middle = st.columns([1, 10])

    with left:
        st.write("Disclaimer")
    with middle:
        st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur')
    
