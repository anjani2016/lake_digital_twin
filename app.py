import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
# Modular Imports
from models.hydrology_engine import calculate_nutrient_loading, get_runoff_coefficient, build_3d_mesh
from models.chemical_engine import calculate_saturation_index, simulate_lake_stability
from PIL import Image
import os


# # --- 2. ACCESSING SECRETS --- when data pipeline is integrated
# # This looks for the values you just saved in .streamlit/secrets.toml 
#
# try:
#     db_user = st.secrets["database"]["user"]
#     db_pass = st.secrets["database"]["password"]
#     weather_key = st.secrets["api_keys"]["weather_api_key"]
# except KeyError as e:
#     st.error(f"Missing secret: {e}. Please check your .streamlit/secrets.toml file.")
#     st.stop() # Stops the app if secrets are missing
#
# # --- REST OF YOUR CODE ---


st.set_page_config(page_title="🌊 Lake Health Digital Twin", layout="wide")

# Define your pages organized by section
pages = {
    "Overview": [
        st.Page("views/0_Main_Dashboard.py", title="Main Dashboard", icon=":material/dashboard:", default=True),
        st.Page("views/1_Project_Charter.py", title="Project Charter", icon=":material/description:"),
    ],
    "Field Operations": [
        st.Page("views/2_Field_Entry.py", title="Volunteer Field Entry", icon=":material/edit_location:")
    ],
    "Risk Analysis": [
        st.Page("views/3_Monte_Carlo_Sim.py", title="Predictive Risk Model", icon=":material/analytics:")
    ]
}

# Configure Navigation and Global Logo
pg = st.navigation(pages)

#  for logo - Verbatim file path as requested
LOGO_PATH = os.path.join(os.path.dirname(__file__), "data/assets/CR_logo.png")

# Renders logo in the upper-left corner of the app and sidebar
try:
    if os.path.exists(LOGO_PATH):
        logo_img = Image.open(LOGO_PATH)
        st.logo(logo_img, size="large") 
    else:
        st.warning(f"Logo not found at {LOGO_PATH}")
except Exception as e:
    st.error(f"Error loading logo: {e}")

pg.run()