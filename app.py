import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go



# Modular Imports
from models.hydrology_engine import calculate_nutrient_loading, get_runoff_coefficient, build_3d_mesh
from models.chemical_engine import calculate_saturation_index, simulate_lake_stability

st.set_page_config(page_title="Hydro-Chemical Twin", layout="wide")

st.title("🌊 Lake Health Digital Twin")
st.markdown("---")

# Sidebar for Project Inputs
with st.sidebar:
    st.header("Project Parameters")
    rainfall = st.slider("Rainfall Event (mm)", 0, 150, 25)
    agri_land = st.slider("Agricultural Land (%)", 0, 100, 30)
    
    st.subheader("Water Chemistry")
    ph = st.slider("pH Level", 6.5, 9.5, 8.1)
    ca = st.number_input("Calcium (mg/L)", value=40.0)
    tp = st.number_input("Total Phosphorus (mg/L)", value=0.025, format="%.3f")

# --- EXECUTION LOGIC ---
c_factor = get_runoff_coefficient(agri_land)
influent_vol = calculate_nutrient_loading(rainfall, 50, c_factor)
si_result = calculate_saturation_index(ph, ca, tp)
status, color = simulate_lake_stability(tp, ca)

# --- DISPLAY UI ---
col1, col2 = st.columns([1, 2])

with col1:
    st.metric("Estimated Influent Volume", f"{influent_vol:,.0f} m³")
    st.subheader("Stability Analysis")
    st.markdown(f"**State:** :{color}[{status}]")
    st.markdown(f"**Saturation Index (SI):** {si_result}")
    
    if si_result > 0:
        st.success("Chemistry suggests natural phosphorus precipitation.")
    else:
        st.error("Chemistry suggests phosphorus remains bioavailable for algae.")

with col2:
    # Synthetic Bathymetry Data (Replace with CSV upload in Phase 4)
    np.random.seed(42)
    obs_data = pd.DataFrame({
        'x': np.random.uniform(0, 100, 50),
        'y': np.random.uniform(0, 100, 50),
        'depth': -np.random.uniform(5, 40, 50)
    })
    
    gx, gy, gz = build_3d_mesh(obs_data)
    
    fig = go.Figure(data=[go.Surface(z=gz, x=gx, y=gy, colorscale='Viridis')])
    
    # Visualization of the Hypoxic "Dead Zone" (e.g., depths > 25m)
    fig.add_trace(go.Surface(z=np.full_like(gz, -25), x=gx, y=gy, 
                             showscale=False, opacity=0.3, colorscale='Reds'))
    
    fig.update_layout(title="3D Bathymetry & Hypoxia Model", margin=dict(l=0, r=0, b=0, t=40))
    st.plotly_chart(fig, use_container_width=True)

st.info("**P.Eng Validation:** This model applies Mass Balance and Stumm-Morgan equilibrium for real-time environmental assessment.")