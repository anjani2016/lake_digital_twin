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