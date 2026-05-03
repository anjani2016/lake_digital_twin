# Changelog - Lake Digital Twin

## [v2] - 2026-05-03
### Added
- **Volunteer Field Entry**: Integrated `2_Field_Entry.py` into the main navigation sidebar.
- **Geospatial Logging**: Added interactive map support using `folium` for volunteers to log sampling locations.
- **Dependencies**: Added `streamlit-folium` and `folium` to `requirements.txt`.

### Changed
- **App Navigation**: Reorganized `app.py` into distinct sections: Lake Dashboard, Field Operations, and Risk Analysis.
- **Dependency Management**: Fixed syntax in `requirements.txt` to ensure clean Docker builds.

---

## [v1] - 2026-05-01
### Added
- **3D Bathymetry**: Initial implementation of 3D mesh rendering for lake beds.
- **Chemical Engine**: Thermodynamic equilibrium modeling and Saturation Index (SI) calculations.
- **Risk Model**: Monte Carlo simulation for predictive risk analysis.
- **Dockerization**: Initial Dockerfile setup with WhiteboxTools integration.
