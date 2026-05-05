import streamlit as st
import streamlit.components.v1 as components
import os

# Set page for iPad wide-view
st.set_page_config(
    page_title="NAVASTRA-81 TACTICAL",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Military System Sidebar
with st.sidebar:
    st.markdown("<h2 style='color: #ff0033;'>TACTICAL CONSOLE</h2>", unsafe_allow_html=True)
    st.divider()
    st.subheader("System Telemetry")
    st.metric(label="COMBAT AUW", value="38 KG", delta="READY") #
    st.metric(label="PAYLOAD MAX", value="10 KG", delta="NOMINAL") #
    st.metric(label="PROPULSION", value="12.67 KG/M", delta="STABLE") #
    st.divider()
    st.warning("RESTRICTED DATA: Access Logged at USI Delhi Command.") #

# Remove Streamlit default padding
st.markdown("<style>.block-container {padding: 0; background: #010409;}</style>", unsafe_allow_html=True)

def load_html():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h3>CRITICAL ERROR: HUD DATA MISSING</h3>"

html_code = load_html()
components.html(html_code, height=1050)
