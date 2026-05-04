import streamlit as st

# Set page configuration for a professional wide-screen feel
st.set_page_config(page_title="Project Charter | Lake Digital Twin", layout="wide")

# --- Title Section ---
st.title("🌊 Lake Health Digital Twin: Strategic Overview")
st.markdown("""
**An Engineering-Grade Framework for Predictive Water Management**  
*Lead Engineer: Anjani Duddukuru, P.Eng, PMP, PMI-RMP*
---
""")

# --- Project Objectives ---
st.header("🎯 Project Objectives")
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Predictive Modeling")
    st.write("""
    - Simulate nutrient flux (Phosphorus/Nitrogen) based on high-resolution rainfall events.
    - Forecast Trophic State changes to provide early warnings for harmful algae blooms.
    """)

with col2:
    st.subheader("2. Decision Support")
    st.write("""
    - Provide a 'Virtual Jar Test' environment for chemical treatment validation before deployment.
    - Optimize municipal and agricultural planning through lakeshore capacity assessment.
    """)

# --- The Technical Approach ---
st.header("🛠️ Technical Approach")
st.info("**Methodology:** A hybrid 'Waterfall-Agile' approach, ensuring rigorous engineering validation within rapid iteration cycles.")

tab1, tab2, tab3 = st.tabs(["Phase 1: Geospatial", "Phase 2: Chemical", "Phase 3: Real-Time"])

with tab1:
    st.markdown("""
    ### Foundation & Delineation
    - **Bathymetry Mapping:** Utilizing NRCan data to build 3D volumetric lake models.
    - **Catchment Delineation:** Automated watershed analysis using *WhiteboxTools* to identify primary nutrient "pour points".
    """)

with tab2:
    st.markdown("""
    ### Stoichiometric Simulation
    - **Mass Balance Engine:** Calculating nutrient accumulation vs. flushing rates.
    - **Reaction Modeling:** Simulating the Ca:P ratio and precipitation events within the water column.
    """)

with tab3:
    st.markdown("""
    ### Data Pipeline & Validation
    - **Field Integration:** Direct intake of volunteer-collected Secchi depth and thermal data.
    - **Cloud Connectivity:** Transitioning from static datasets to real-time MSC GeoMet API feeds.
    """)
    st.markdown("---")
    
    st.markdown("# Project Documentation: Ontario Lake Health Digital Twin")
    st.write("**Project Stage:** Phase 1 - Geospatial Foundation & Phase 2 - Chemical Engine Integration")
    st.write("**Last Updated:** 2024-05-22")

    st.markdown("---")

    st.subheader("1. Project Vision")
    st.write("To develop a predictive 'Living Digital Twin' of Ontario's inland lakes that treats the water body as a biological system (metabolism). The goal is to move from reactive monitoring to predictive intervention using real-time environmental transients.")

    st.subheader("2. Core Engineering Logic (Mass Balance)")
    st.write("The system operates on the principle of **Accumulation = Input - Output ± Reaction**.")
    st.write("- **Inputs:** Rainfall intensity (MSC GeoMet API), Agricultural phosphorus loading (Export coefficients), and atmospheric deposition.")
    st.write("- **Outputs:** Hydraulic flushing (Residence time) and sediment burial.")
    st.write("- **Reaction:** Chemical precipitation (Virtual Jar Test) based on the Calcium-to-Phosphorus (Ca:P) ratio.")

    # Include images from assets
    col1, col2 = st.columns(2)
    with col1:
        st.image("data/assets/schematic_lake_digital_twin.png", caption="Project Schematic: Lake Metabolism Model")
    with col2:
        st.image("data/assets/chemicalprocess_lake_digital_twin.png", caption="Chemical Process: Calcium-Phosphorus Reaction")

    st.subheader("3. Current Technical Stack")
    st.write("- **Framework:** Streamlit (UI/Frontend)")
    st.write("- **Environment:** Docker (python:3.11-slim) with `libgomp1` for parallel processing.")
    st.write("- **Geospatial Engine:** WhiteboxTools (WBT) for catchment delineation and bathymetry.")
    st.write("- **Data Management:** `.streamlit/secrets.toml` for API keys and database credentials.")
    st.write("- **Volunteer Integration:** Manual entry for Secchi Depth (turbidity) and Thermal Stratification (Surface vs 1m depth).")

    st.subheader("4. Key Components Developed")
    st.write("- **Virtual Jar Test Engine:** A 'What-If' simulator for chemical dosing (Lime/Calcium) to predict phosphorus removal efficiency.")
    st.write("- **3D Bathymetry Model:** Synthetic prototype (moving to NRCan HRDEM data) to visualize hypoxia and nutrient zones.")
    st.write("- **Project Charter Page:** A client-facing presentation of objectives and methodology.")
    st.write("- **Volunteer Mapping Page:** Folium-based coordinate capture to link field readings to specific 'Pour Points.'")

    st.subheader("5. Active Transients & Variables")
    st.write("- **Clarity/Turbidity:** Measured via Secchi Disk depth.")
    st.write("- **Thermal Gradient:** Identifying the thermocline to predict oxygen depletion.")
    st.write("- **Chemical Metabolism:** Phosphorus binding with Calcium into stable minerals (Hydroxyapatite) vs. release during hypoxia.")

    st.subheader("6. Next Milestones")
    st.markdown("""
    - [ ] Connect MSC GeoMet API for real-time Aurora rainfall data.
    - [ ] Implement Phosphorus Export Coefficients for York Region land-use types.
    - [ ] Integrate Ontario Lake Partner Program (LPP) historical CSV data for validation.
    - [ ] Transition from local CSV storage to a cloud-based database pipeline (SQL/Snowflake).
    """)

    st.markdown("---")
    st.info("*This document is a living artifact and is updated as the engineering design evolves.*")

# --- Engineering Standards ---
st.header("⚖️ Standards & Compliance")
st.write("""
This project aligns with the **CCME (Canadian Council of Ministers of the Environment)** guidance for water quality monitoring design and the **Ontario Lakeshore Capacity Assessment** handbook.
""")

# Footer call to action
st.markdown("---")
st.caption("Confidential Project Presentation - Preliminary Engineering Design")