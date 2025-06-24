import streamlit as st_module
import pandas as pd
import numpy as np
def dashboard(st: st_module):
    
    st.markdown("""
    <style>
    .welcome-container {
        background-color: #f0f2f6;
        padding: 3rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .welcome-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #262730;
        margin-bottom: 1rem;
    }
    
    .welcome-subtitle {
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 2rem;
        line-height: 1.5;
    }
    
    .prediction-button {
        background-color: #ffffff;
        border: 2px solid #ddd;
        padding: 0.75rem 2rem;
        font-size: 1rem;
        font-weight: 500;
        color: #333;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-block;
        text-decoration: none;
    }
    
    .prediction-button:hover {
        background-color: #f8f9fa;
        border-color: #999;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    
    .app-header {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        font-weight: 500;
        margin-bottom: 2rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid #eee;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="app-header">Alzheimer\'s Risk Assessment Tool</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="welcome-container">
        <h1 class="welcome-title">Welcome!</h1>
        <p class="welcome-subtitle">
            This application helps you predict and analyze the risk of Alzheimer's.
        </p>
    </div>
    """, unsafe_allow_html=True)
    

    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("Make a prediction", key="prediction_btn", use_container_width=True):
            st.session_state.current_page = "Prediction"
            st.rerun()