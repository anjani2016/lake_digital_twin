import numpy as np
from scipy.interpolate import griddata
import pandas as pd


"""
HYDROLOGY ENGINE
Logic: 
1. Rational Method (Q=CiA) for runoff estimation.
2. Cubic Spline Interpolation for 3D Bathymetry mesh generation.
Reference: Ontario 'Large Inland Lakes' dataset protocols.
"""

def calculate_nutrient_loading(rainfall_mm, catchment_area_km2, runoff_coeff):
    """Calculates 'Influent' volume (m3) based on rainfall and land use."""
    # (mm to m) * (km2 to m2) * coefficient
    inflow_volume = (rainfall_mm * 0.001) * (catchment_area_km2 * 1000000) * runoff_coeff
    return inflow_volume

def get_runoff_coefficient(agri_percent):
    """Weights the C-factor based on land-use types."""
    return (agri_percent / 100) * 0.5 + ((100 - agri_percent) / 100) * 0.1

def build_3d_mesh(df):
    """
    Converts 2D point data (x, y, depth) into a 3D surface mesh.
    Used for visualizing 'Dead Zones' and calculating lake volume.
    """
    # Create grid for interpolation
    grid_x, grid_y = np.mgrid[df.x.min():df.x.max():100j, df.y.min():df.y.max():100j]
    
    # Interpolate depth (z) values using cubic interpolation for smoothness
    grid_z = griddata((df.x, df.y), df.depth, (grid_x, grid_y), method='cubic')
    
    return grid_x, grid_y, grid_z


# real data


def ingest_ontario_csv(file_path):
    """
    Standardizes Ontario GeoHub 'Bathymetry Point' CSVs.
    Expected Columns: 'OGF_ID', 'DEPTH', 'geometry' (or 'X'/'Y')
    """
    df = pd.read_csv(file_path)
    
    # Rename columns to match our internal mesh engine
    # Ontario usually uses 'DEPTH' for the z-axis
    if 'DEPTH' in df.columns:
        df = df.rename(columns={'DEPTH': 'depth'})
        
    # Standardize depth to negative values if they are positive in the file
    if df['depth'].min() >= 0:
        df['depth'] = -df['depth']
        
    return df