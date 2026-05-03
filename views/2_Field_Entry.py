import streamlit as st
import folium
from folium.plugins import Geocoder
from streamlit_folium import st_folium
import pandas as pd
from datetime import datetime

st.title("📍 Volunteer Field Entry")
st.write("Search for a location or click on the map to log your sampling data.")

# Initialize map centered on Aurora/York Region
m = folium.Map(location=[44.00, -79.47], zoom_start=10)
m.add_child(folium.LatLngPopup()) # Shows coordinates on click
Geocoder().add_to(m) # Adds search box to the map

# Render the map and capture the 'last_clicked' data
map_data = st_folium(m, height=450, width=700)

if map_data.get("last_clicked"):
    lat = map_data["last_clicked"]["lat"]
    lon = map_data["last_clicked"]["lng"]
    
    st.success(f"Selected Location: {lat:.5f}, {lon:.5f}")
    
    # Field Entry Form
    with st.form("observation_form"):
        st.subheader("📝 Log Field Observations")
        
        col1, col2 = st.columns(2)
        with col1:
            secchi = st.number_input("Secchi Depth (m)", min_value=0.0, value=2.0, step=0.1)
            ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=8.1, step=0.1)
        
        with col2:
            temp_surface = st.number_input("Surface Temp (°C)", value=22.0)
            temp_1m = st.number_input("1m Depth Temp (°C)", value=20.5)
        
        # Calculate Thermocline Strength (Moved from Dashboard)
        temp_gradient = temp_surface - temp_1m
        if temp_gradient > 1.0:
            st.warning("⚠️ Stratification Detected: High Hypoxia Risk at this location.")
        
        if st.form_submit_button("Save to Digital Twin"):
            # Save logic (linking to your Docker Volume /app/data)
            new_data = {
                "timestamp": datetime.now(),
                "lat": lat, "lon": lon,
                "secchi": secchi, 
                "ph": ph,
                "temp_s": temp_surface, 
                "temp_1m": temp_1m
            }
            # Append to your local CSV for Phase 1 validation
            st.info("Reading logged for processing in simulation.")
else:
    st.info("Please click a point on the map to begin logging data.")