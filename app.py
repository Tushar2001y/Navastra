import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Page Configuration for iPad View
st.set_page_config(
    page_title="NAVASTRA-81 Briefing",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hide Streamlit UI elements for a custom app feel
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# 3. Load the index.html content
def load_html():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h3>Error: index.html not found. Check repository file structure.</h3>"

# 4. Sidebar Content for the Dignitary
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/ffffff/drone.png", width=50)
    st.title("Project NAVASTRA-81")
    st.divider()
    st.subheader("Tactical Specifications")
    st.metric(label="All-Up Weight (AUW)", value="38 kg")
    st.metric(label="Payload Capacity", value="10 kg")
    st.metric(label="Individual Motor Thrust", value="12.67 kg")
    st.divider()
    st.write("**Atmanirbhar Bharat Mission**")
    st.caption("Focus: Local Fabrication & High-Fidelity Innovation")

# 5. Render the 3D Viewer
html_content = load_html()
# Adjust height to match typical iPad Pro resolution
components.html(html_content, height=1000, scrolling=False)
 
