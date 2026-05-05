import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="NAVASTRA TACTICAL HUD", layout="wide", initial_sidebar_state="collapsed")

with st.sidebar:
    st.markdown("<h2 style='color: #ff0033;'>TACTICAL OPS</h2>", unsafe_allow_html=True)
    st.divider()
    st.metric(label="COMBAT AUW", value="38 KG", delta="NOMINAL")
    st.metric(label="PAYLOAD MAX", value="10 KG", delta="READY")
    st.divider()
    st.subheader("Comms Protocol")
    st.info("Primary: 5G Internet-Based\nSecondary: RF Ground Control") #
    st.divider()
    st.caption("Strategic Focus: Drone Fabrication & Innovation Phase")

st.markdown("<style>.block-container {padding: 0; background: #010409;}</style>", unsafe_allow_html=True)

def load_html():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h3>HUD CRITICAL FAILURE: DATA FILE NOT FOUND</h3>"

components.html(load_html(), height=1100)
