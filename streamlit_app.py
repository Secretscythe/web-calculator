"""Streamlit entrypoint for the Scientific, Graphing & Calculus Suite."""

import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Advanced Calculator & Graphing Suite",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit default chrome/margins for an immersive app feel
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }
        iframe {
            width: 100% !important;
            min-height: 100vh !important;
            border: none;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Load web_calculator.html
current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "web_calculator.html")

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        calculator_html = f.read()
    
    # Render full app
    components.html(calculator_html, height=1000, scrolling=True)
else:
    st.error("web_calculator.html not found.")
