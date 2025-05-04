<p align="center">
  <!-- Optional: include a project logo here -->
  <!-- <img src="./figures/logo.png" alt="Logo" width="120"/> -->
  <h1>Smoke-Aware City Forecasting</h1>
  <strong>A lightweight ML pipeline to forecast next-day PM₂.₅ in Reno, NV</strong>
</p>

<p align="center">
  <a href="#-project-overview">Overview</a> •
  <a href="#-repository-structure">Structure</a> •
  <a href="#%EF%B8%8F-quickstart">Quickstart</a> •
  <a href="#%F0%9F%93%88-results">Results</a> •
  <a href="#%F0%9F%94%A7-next-steps">Next Steps</a> •
  <a href="#%F0%9F%93%84-license">License</a>
</p>

---

## 🔍 Project Overview

Wildfire smoke is Reno’s major air-quality threat, driving dangerous PM₂.₅ spikes.  
This repo demonstrates a simple, end-to-end workflow:

1. **Ingest** hourly PM₂.₅ via OpenAQ v3 API (2015–2025)  
2. **Download** daily MODIS fire-pixel counts (2021–2025)  
3. **Explore** data with line plots & boxplots  
4. **Baseline**: “tomorrow = yesterday” → MAE ≈ 3.91 µg/m³  
5. **Model**: Random Forest (fire pixels + yesterday’s PM₂.₅) → MAE ≈ 1.72 µg/m³  

---

## 📂 Repository Structure

```text
smoke-aware-city/
├── data/                   # Raw & processed CSVs
│   ├── pm25_Reno_2024-07-01.csv
│   └── fires_Reno_2025.csv
├── notebooks/              # Jupyter notebooks
│   ├── 01_download.ipynb   # Data ingestion
│   ├── 02_eda.ipynb        # EDA plots
│   ├── 03_baseline.ipynb   # Baseline MAE
│   └── 05_model.ipynb      # Random Forest model
├── figures/                # Exported chart images
├── environment.yml         # Conda environment spec
├── README.md               # This file
└── LICENSE                 # MIT License


🚀 # 1. Clone
git clone https://github.com/<your-username>/smoke-aware-city.git
cd smoke-aware-city

# 2. Setup environment
conda env create -f environment.yml
conda activate smoke-aware-env

# 3. Launch notebooks
jupyter lab
# Run in order: 01_download → 02_eda → 03_baseline → 05_model

📈 Results

Baseline MAE (yesterday → tomorrow): 3.91 µg/m³

Random Forest MAE (with fire-pixels + previous PM₂.₅): 1.72 µg/m³

These results illustrate that satellite-detected fire activity is a strong predictor of next-day PM₂.₅.
