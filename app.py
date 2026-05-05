import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Page Configuration for iPad Standalone View
st.set_page_config(
    page_title="NAVASTRA-81 Briefing",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Sidebar HUD with Technical Parameters
with st.sidebar:
    st.header("Project NAVASTRA-81")
    st.divider()
    st.subheader("Key Mission Specs")
    st.metric(label="All-Up Weight (AUW)", value="38 kg") #
    st.metric(label="Payload Capacity", value="10 kg") #
    st.metric(label="Individual Motor Thrust", value="12.67 kg") #
    st.divider()
    st.caption("Strategic Focus: Drone Fabrication & loitering munitions integration.") #

# 3. UI Styling - Remove Streamlit padding for full-screen effect
st.markdown("<style>.block-container {padding: 0;}</style>", unsafe_allow_html=True)

# 4. Load and Render HTML
def load_html():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h3>Error: index.html not found. Check repository.</h3>"

html_code = load_html()
components.html(html_code, height=1000, scrolling=False)
