import numpy as np
import pandas as pd

def run_lake_simulation(base_rain, base_si, iterations=1000):
    si_values = []
    risk_count = 0
    
    for _ in range(iterations):
        # Randomize variables based on normal distribution
        sim_rain = np.random.normal(base_rain, base_rain * 0.1)
        sim_si = np.random.normal(base_si, abs(base_si * 0.1))
        
        si_values.append(sim_si)
        if sim_rain > 45 and sim_si < 0:
            risk_count += 1
            
    risk_prob = (risk_count / iterations) * 100
    df_results = pd.DataFrame({"Simulated_SI": si_values})
    
    return risk_prob, df_results

# helper function to interpret the results

def interpret_simulation(risk_prob, sim_data):
    """
    Analyzes Monte Carlo results and returns a summary and status level.
    """
    mean_si = sim_data["Simulated_SI"].mean()
    std_si = sim_data["Simulated_SI"].std()
    
    if risk_prob == 0:
        status = "Excellent"
        summary = f"The system is highly resilient. With a mean SI of {mean_si:.2f}, the lake remains far above the risk threshold (SI=0) even under simulated weather stress."
    elif risk_prob < 5:
        status = "Stable"
        summary = f"The system is generally stable. However, {risk_prob:.2f}% of simulations suggest a minor risk under extreme precipitation outliers."
    elif risk_prob < 15:
        status = "Caution"
        summary = "Warning: Environmental buffering is reaching capacity. Significant rainfall may trigger a phosphorus precipitation event."
    else:
        status = "High Risk"
        summary = "Immediate Action Recommended: The majority of simulated scenarios predict chemical instability leading to potential algae blooms."
        
    return status, summary