import streamlit as st
import pandas as pd
import numpy as np
from fileloader import find_file

# --- PAGE TITLE ---
st.markdown("<h2 style='text-align: center; margin-bottom: 0.9em'>Our team</h2>", unsafe_allow_html=True)

# --- TEAM MEMBER DATA ---
names = ["Nino Sabella", "Saad Waseem", "Jingren Dai", "Ayse Yasemin Mutlugil", "Orkun Akyol"]
degrees = [
    "MSc Data Science",
    "MSc Data Science",
    "MSc Data Science",
    "MSc Computer Science",
    "MSc Data Science"
]
photo_paths = [
    find_file("images/nino.jpeg"),
    find_file("images/saad.jpeg"),
    find_file("images/david.jpg"),
    find_file("images/yasemin.jpeg"),
    find_file("images/orkun.jpg")
]
linkedin_links = [
    "https://www.linkedin.com/in/nino-sabella-429046207/",
    "https://www.linkedin.com/in/saadwaseem645/",
    "",
    "https://www.linkedin.com/in/ayse-yasemin-mutlugil/",
    ""
]

# --- DISPLAY CONTAINER ---
with st.container(border=True):
    cols = st.columns(2)
    for idx in range(len(names)):
        col = cols[idx % 2]
        with col:
            inner_cols = st.columns([1, 2])
            with inner_cols[0]:
                # --- PHOTO ---
                st.image(str(photo_paths[idx]), width=120)
            with inner_cols[1]:
                # --- NAME & DEGREE ---
                name_html = (
                    f"<span style='background-color:#ecebe4; color:#3d3a2a; border-radius:6px; padding:4px 12px; font-weight:600;'>{names[idx]}</span>"
                )
                degree_html = (
                    f"<span style='background-color:#ecebe4; color:#3d3a2a; border-radius:6px; padding:2px 10px; font-size:0.95em;'>{degrees[idx]}</span>"
                )
                if linkedin_links[idx]:
                    st.markdown(
                        f"<b><a href='{linkedin_links[idx]}' target='_blank' style='text-decoration:none; color:inherit;'><br>{name_html}</a></b><br>{degree_html}",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"<br><b>{name_html}</b><br>{degree_html}",
                        unsafe_allow_html=True
                    )
            # --- SPACE BETWEEN EACH MEMBER ---
            st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)