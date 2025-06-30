import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path


def find_file(filename):
    root = Path(__file__).parent 
    matches = list(root.rglob(filename))

    if matches:
        file_path = matches[0]
        print("Found:", file_path)
        return file_path.resolve()
    else:
        print("File not found")
        return None



# left, middle, right = st.columns([2, 6, 2])
# with middle:
# st.title("Resources")

st.markdown("<h2 style='text-align: center; margin-bottom: 0.9em'>Helpful resources</h2>", unsafe_allow_html=True)
# st.markdown("---")

left, middle, right = st.columns([5, 1, 5])

with left:
    with st.container(border=True):
        l, m, r = st.columns([2, 2.7, 2])
        with m:
            st.markdown(
                "<div style='font-size: 1.7em; font-weight: 600; margin-bottom: 0.01em; margin-top: 0.5em; text-align: center;'>For Patients</div>",
                unsafe_allow_html=True
            )
            st.divider()
        for i in range(3):
            img_col, text_col = st.columns([1, 4])
            with img_col:
                st.image(str(find_file("placeholder.svg")), width=60)
            with text_col:
                st.markdown(f"**Resource {i+1}**")
                st.write(
                    "Nullam convallis urna non leo sollicitudin, non suscipit massa molestie. "
                    "Vivamus mollis semper viverra. Integer condimentum libero et neque imperdiet, "
                    "non efficitur mi posuere. Morbi vel eros fringilla, aliquam enim ut, mollis elit. "
                    "Ut pharetra hendrerit ornare."
                )

with right:
    with st.container(border=True):
        l, m, r = st.columns([2, 2.5, 2])
        with m:
            st.markdown(
                "<div style='font-size: 1.7em; font-weight: 600; margin-bottom: 0.01em; margin-top: 0.5em; text-align: center;'>For Doctors</div>",
                unsafe_allow_html=True
            )
            st.divider()
        for i in range(3):
            img_col, text_col = st.columns([1, 4])
            with img_col:
                st.image(str(find_file("placeholder.svg")), width=60)
            with text_col:
                st.markdown(f"**Resource {i+1}**")
                st.write(
                    "Nullam convallis urna non leo sollicitudin, non suscipit massa molestie. "
                    "Vivamus mollis semper viverra. Integer condimentum libero et neque imperdiet, "
                    "non efficitur mi posuere. Morbi vel eros fringilla, aliquam enim ut, mollis elit. "
                    "Ut pharetra hendrerit ornare."
                )





