

## Pyenv

## Docker build 
- deactivate virtual environment. go to project directory
- Build and Run Command ```docker build -t lake-digital-twin:v2 .```
- Run the Container: ```docker run -p 8501:8501 lake-digital-twin:v2```
## Folder Structure

hydro_twin_project/         <-- Root Folder
├── app.py                  # Main UI
├── setup_project.py        # Verification / Binary Check (New)
├── requirements.txt        # Dependencies
├── WBT/                    # WhiteboxTools Binaries
├── data/                   # Data storage
├── models/                 # Engineering Engines
│   ├── __init__.py
│   ├── chemical_engine.py
│   └── hydrology_engine.py
└── README.md               # Charter & Notes


## Logic for Mass Balance

Next Steps for Professional Engineering (P.Eng) Validation:
- Mass Balance: Integrate the Vollenweider Model—the industry standard for relating phosphorus loading to lake chlorophyll levels.

- Sensors: We should look at connecting the DataStream.org API directly so that when a user selects a lake, the Stumm-Morgan equilibrium is calculated automatically using the latest regional pH and Alkalinity data.


P2

or Phase 1 and 2, we will focus on the Geospatial 3D Foundation and the Thermodynamic Equilibrium Engine.

Since we are dealing with high-resolution bathymetry and chemical modeling, the logic uses Bilinear/Cubic Interpolation for the lake bed and a simplified Ion Activity Product (IAP) calculation for the chemical stability. This ensures the app is both a visual digital twin and a functional engineering tool.

P3

**Key Engineering Decisions made in this Draft:**

    - **Saturation Index (SI):** Using $SI = \log_{10}(IAP / K_{sp})$ is the standard way to communicate chemical potential to non-chemists. $SI > 0$ means the "jar test" would show solids forming.
    - **Interactive Dead-Zones:** I added a semi-transparent "Red Plane" at 20m depth. This visually demonstrates the hypoxic zone you mentioned, allowing lake associations to see exactly what percentage of the lake floor is at risk during summer stratification.
    - **Rendering:** Plotly go.Surface is used here. It handles the "Bilinear Interpolation" smoothly within the browser, avoiding the need for heavy server-side rendering.


## 1. Data Ingestion Strategy

- The Ontario GeoHub provides datasets that are significantly more structured than the historic 1940s PDFs.

| Dataset Name| Format| Best Use Case| 
|-----|-----|-----|
|Bathymetry Point |CSV / GeoJSON| Recommended. Provides raw $X, Y, Z$ (Depth) points. Perfect for our build_3d_mesh function.|
|Bathymetry Line| Shapefile / GeoJSON| Use this if points aren't available. You’ll need to "explode" the contour lines into points for interpolation.|
| Bathymetry Index| Metadata| Useful for identifying the Survey Method and Year to display in your UI (adds P.Eng credibility).|

2. Updating models/hydrology_engine.py for Real Data
To handle actual CSVs from the GeoHub, we need to modify the ingestion logic. Often, these files use UTM coordinates (meters) rather than Lat/Long, which is actually better for our 3D mesh math.

3. Visualizing the "Dead Zone"
In our app.py, we previously used a red plane to show hypoxia. For a professional engineering tool, we should define this based on the Thermocline—the layer where water temperature drops rapidly, often leading to oxygen depletion in the "Hypolimnion" (the cold bottom layer).

Primary Source: Ontario GeoHub - Bathymetry Point

Validation Logic: Interpolation assumes a continuous benthic surface; however, "Bathymetry Index" data should be checked for the SURVEY_METHOD (e.g., Echo-sounder vs. Lidar) to quantify uncertainty.


2. Measuring & Mapping Volunteer Work
- As a Lakes Canada volunteer, the data you collect is used by the Dorset Environmental Science Centre (DESC) to detect early changes in water quality. Here is how we map your specific tools to the project logic:  

    - Secchi Disk: You are measuring water clarity, which is a proxy for the concentration of suspended particles and algae. In your twin, this depth value can be used to validate the predicted "Precipitation Zone" from your chemical engine.  
    - Temperature Gradient: By taking readings at the surface and 1m, you are identifying thermal stratification. Your Digital Twin can use this "Delta T" to model the Thermocline, which is essential for the Phase 1: 3D Volumetric Modeling to determine if oxygen is being cut off from the lake floor.  
    - Protocol Alignment: Your use of weights and clean rope to sink the disk matches the official Lake Partner Program (LPP) protocols for inland lakes. 