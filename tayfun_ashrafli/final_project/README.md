📊 Smoke-Aware City Forecasting

A lightweight ML pipeline to forecast next-day PM₂.₅ in Reno, NV, using satellite fire-hotspot counts and historical air-quality readings.

🔍 Project Overview

Wildfire smoke is Reno’s major air-quality threat, driving spikes in fine particulate matter (PM₂.₅) that harm public health. This workflow:

Ingests hourly PM₂.₅ via OpenAQ v3 API (2015–2025)

Downloads daily MODIS fire-pixel counts (2021–2025)

Performs exploratory data analysis (EDA) with line plots and daily boxplots

Establishes a naïve baseline ("tomorrow = yesterday") → MAE ≈ 3.91 µg/m³

Trains a Random Forest regressor (features: fire pixels + yesterday’s PM₂.₅) → MAE ≈ 1.72 µg/m³

📂 Repository Structure

smoke-aware-city/
├── data/                   # Raw & processed CSV files
│   ├── pm25_Reno_2024-07-01.csv
│   └── fires_Reno_2025.csv
├── notebooks/              # Jupyter notebooks
│   ├── 01_download.ipynb   # Data ingestion scripts
│   ├── 02_eda.ipynb        # Exploratory data analysis
│   ├── 03_baseline.ipynb   # Baseline model & MAE
│   └── 05_model.ipynb      # Random Forest model & evaluation
├── figures/                # Exported plot images
├── environment.yml         # Conda environment specification
├── README.md               # Project overview and instructions
└── LICENSE                 # MIT License

🚀 Quickstart

# Clone the repository
git clone https://github.com/<your-username>/smoke-aware-city.git
cd smoke-aware-city

# Setup the environment
conda env create -f environment.yml
conda activate smoke-aware-env

# Launch Jupyter Lab
jupyter lab
# Run notebooks in order: 01_download → 02_eda → 03_baseline → 05_model

📈 Results

Model

MAE (µg/m³)

Baseline

3.91

Random Forest

1.72
