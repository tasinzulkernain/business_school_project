📊 Smoke-Aware City Forecasting
A lightweight ML pipeline to forecast next-day PM₂.₅ in Reno, NV, using  
satellite fire-hotspot counts and historical air-quality readings.

🔍 Project Overview

Wildfire smoke is Reno’s major air-quality threat, driving spikes in fine particulate matter (PM₂.₅) that harm public health. This repository demonstrates a simple, reproducible workflow that:

1. **Ingests** hourly PM₂.₅ via the OpenAQ v3 API (2015–2025)  
2. **Downloads** daily fire-pixel counts from NASA’s MODIS archive (2021–2025)  
3. **Explores** data with line plots & daily boxplots  
4. **Baselines** forecast: “tomorrow = yesterday” → MAE ≈ 3.91 µg/m³  
5. **Models** with Random Forest (fire + PM₂.₅ₜ₋₁) → MAE ≈ 1.72 µg/m³


📂 Repository Structure

smoke-aware-city/
├── data/
├── notebooks/
├── figures/
├── environment.yml
├── README.md
└── LICENSE


🚀 Quickstart

```bash
git clone https://github.com/you/smoke-aware-city.git
cd smoke-aware-city
conda env create -f environment.yml
conda activate smoke-aware-env
jupyter lab

📈 Results
Model	MAE (µg/m³)
Baseline	3.91
Random Forest	1.72
