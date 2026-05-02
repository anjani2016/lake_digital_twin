import numpy as np

"""
CHEMICAL ENGINE
Logic:
1. Stumm-Morgan Equilibrium for Hydroxyapatite precipitation.
2. Saturation Index (SI) calculation to predict phosphorus bioavailability.
Reference: Stumm, W., & Morgan, J. J. (1996). Aquatic Chemistry.
"""

def calculate_saturation_index(ph, ca_mg_l, po4_mg_l):
    """
    Determines if P will precipitate (Natural Coagulation).
    SI > 0: Precipitation likely (Self-cleansing).
    SI < 0: Nutrients stay soluble (Algae risk).
    """
    # Convert mg/L to Molarity (Approximate for P.Eng validation)
    molar_ca = ca_mg_l / 40078  
    molar_po4 = po4_mg_l / 94970
    
    # Thermodynamic constants (at 25C)
    log_ksp = -58.0 
    oh_conc = 10**(ph - 14)
    
    # Ion Activity Product (IAP)
    # Equation: {Ca}^5 * {PO4}^3 * {OH}
    log_iap = (5 * np.log10(molar_ca)) + (3 * np.log10(molar_po4)) + np.log10(oh_conc)
    
    si = log_iap - log_ksp
    return round(si, 2)

def simulate_lake_stability(tp_mg_l, ca_mg_l):
    """Quick empirical check for P:Ca ratios."""
    ratio = ca_mg_l / (tp_mg_l + 0.001)
    if ratio > 50:
        return "Stable (Self-Buffering)", "green"
    elif 20 < ratio <= 50:
        return "Sensitive", "orange"
    else:
        return "Unstable (High Bloom Risk)", "red"
    

# virtual jar test - "what if simulator"

def virtual_jar_test(initial_tp, calcium_dose, ph_level):
    """
    Simulates a chemical precipitation event.
    Formula: Ca5OH(PO4)3 formation is pH dependent.
    """
    # Efficiency factor based on pH (ideal range 10-12 for lime)
    # For natural lakes (pH 7-8), efficiency is lower but still present.
    efficiency = 0.05 * (ph_level - 6) if ph_level > 6 else 0
    
    # Calculate precipitated Phosphorus (mg/L)
    precipitated_p = initial_tp * (calcium_dose / 100) * efficiency
    
    # Ensure we don't remove more than exists
    final_tp = max(0, initial_tp - precipitated_p)
    removal_rate = ((initial_tp - final_tp) / initial_tp) * 100
    
    return final_tp, removal_rate