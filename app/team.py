import streamlit as st
import pandas as pd
import numpy as np

# st.title("Team")

st.markdown("<h1 style='text-align: center;'>Our team</h1>", unsafe_allow_html=True)
st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)

names = ["Nino Sabella", "Saad Waseem", "Jingren Dai", "Ayse Yasemin Mutlugil", "Orkun Akyol"]
degrees = [
    "MSc Data Science",
    "MSc Data Science",
    "MSc Data Science",
    "MSc Computer Science",
    "MSc Data Science"
]
photo_paths = [
    "images/nino.jpeg",
    "images/saad.jpeg",
    "images/david.jpg",
    "images/yasemin.jpeg",
    "images/orkun.jpg"
]
linkedin_links = [
    "https://www.linkedin.com/in/nino-sabella-429046207/",
    "https://www.linkedin.com/in/saadwaseem645/",
    "",
    "https://www.linkedin.com/in/ayse-yasemin-mutlugil/",
    ""
]

# with st.container(border=True):
#     for i, name in enumerate(names):
#         cols = st.columns([1, 6])
#         with cols[0]:
#             st.image(photo_paths[i], width=95)
#         with cols[1]:
#             st.markdown(
#                 f"<br>**[{name}]({linkedin_links[i]})**  \n<small>{degrees[i]}</small>",
#                 unsafe_allow_html=True
#             )
#         if i < len(names) - 1:
#             st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)

with st.container(border=True):
    cols = st.columns(2)
    for idx in range(len(names)):
        col = cols[idx % 2]
        with col:
            inner_cols = st.columns([1, 2])
            with inner_cols[0]:
                st.image(photo_paths[idx], width=120)
            with inner_cols[1]:
                if linkedin_links[idx]:
                    st.markdown(
                        f"<b><a href='{linkedin_links[idx]}' target='_blank' style='text-decoration:none; color:inherit;'><br>{names[idx]}</a></b><br><small>{degrees[idx]}</small>",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"<br><b>{names[idx]}</b><br><small>{degrees[idx]}</small>",
                        unsafe_allow_html=True
                    )
            st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)