import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE TITLE ---
st.markdown("<h2 style='text-align: center'>History</h2>", unsafe_allow_html=True)

# --- SEPARATOR LINE ---
st.markdown("---")

# --- PLACEHOLDER ---
st.markdown(
    "<div style='text-align: left;'><em>Prediction history will appear here.</em></div>",
    unsafe_allow_html=True,
)