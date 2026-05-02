import streamlit as st
import plotly.express as px
from models.simulation_engine import run_lake_simulation
from models.simulation_engine import interpret_simulation

# Title

st.title("🛡️ Predictive Risk Simulation")

# Educational Note for Page 1
st.info("""
**What are we measuring?**  
This simulation calculates the **Probability of an Algae Bloom**. We use Monte Carlo methods to vary 
weather and chemical inputs by ±10% to see how often they result in a 'Negative Saturation Index' 
during high rainfall. The graph below displays the distribution of these outcomes.
""")

# Simulation Controls
n_sims = st.sidebar.slider("Number of Simulations", 100, 5000, 1000)
rain_forecast = st.sidebar.number_input("Forecasted Rain (mm)", value=25.0)
current_si = st.sidebar.number_input("Baseline SI", value=17.36)

if st.button("Run Simulation"):
    # Run simulation and get detailed results for plotting
    risk_prob, sim_data = run_lake_simulation(rain_forecast, current_si, iterations=n_sims)
    
    # 1. Result Metric
    st.metric("Bloom Risk Probability", f"{risk_prob:.2f}%")
    
    # 2. Results Graph
    # We plot the simulated Saturation Index values to show the stability spread
    fig = px.histogram(sim_data, x="Simulated_SI", 
                       title="Distribution of Chemical Stability Outcomes",
                       labels={'Simulated_SI': 'Saturation Index (SI)'},
                       color_discrete_sequence=['#00CC96'])
    
    # Highlight the 'Risk Zone' (SI < 0)
    fig.add_vline(x=0, line_dash="dash", line_color="red", annotation_text="Risk Threshold")
    
    st.plotly_chart(fig, use_container_width=True)


    # ... after plotting the chart



    
    # Run the interpreter logic
    status, summary = interpret_simulation(risk_prob, sim_data)
    
    # Display the Analysis
    st.markdown("---")
    st.subheader("System Analysis")
    
    # Dynamic styling based on status
    color = {"Excellent": "green", "Stable": "blue", "Caution": "orange", "High Risk": "red"}[status]
    
    st.markdown(f"**Status:** :{color}[{status}]")
    st.write(summary)
    
    # P.Eng specific insight
    st.caption(f"Statistical Confidence: Based on {n_sims} iterations with a standard deviation of {sim_data['Simulated_SI'].std():.2f}.")