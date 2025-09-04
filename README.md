# ⚡ Global EV Charging & Models 2025 — EDA Tutorial

## 📌 Project Overview  
This project explores **global EV adoption** by analyzing charging station availability and electric vehicle (EV) models worldwide in 2025.  

By combining infrastructure data with EV model specifications, the analysis uncovers **regional gaps, adoption trends, and manufacturer dynamics**.  
The notebook is designed as a **tutorial-style walkthrough** for structured Exploratory Data Analysis (EDA).  

---

## 📊 Dataset  

- **`charging_stations_2025_world.csv`** → EV charging stations (location, type, ports, power).  
- **`country_summary_2025.csv`** → Country-level adoption and infrastructure metrics.  
- **`ev_models_2025.csv`** → EV models and specifications (range, battery, manufacturer).  
- **`world_summary_2025.csv`** → Aggregated global-level EV adoption statistics.  

> 📌 Note: This repo focuses purely on **analysis & visualization**.   

---

## 🔧 Methodology (Step-by-Step)  

1) **Data Cleaning & Prep**  
   - Inspect shapes, dtypes, missing values.  
   - Standardize column naming for consistency.  
   - Merge summaries for cross-country comparisons.  

2) **Exploratory Analysis**  
   - Global charging station distribution.  
   - Country-level adoption vs. infrastructure ratio.  
   - EV model trends: ranges, battery sizes, and availability.  

3) **Visualization & Storytelling**  
   - Comparative plots for regions and manufacturers.  
   - Heatmaps, scatter plots, and bar charts for adoption insights.  
   - Highlight infrastructure gaps vs. adoption demand.  

4) **Insight Extraction**  
   - Identify top EV markets by charging density.  
   - Spot underserved regions.  
   - Track how manufacturers contribute to model diversity.  

---

## 🧠 Features Examined  
- **Infrastructure:** station count, ports, charging power.  
- **Adoption:** EV counts per country.  
- **Models:** battery capacity, range, release year, manufacturer.  
- **Ratios:** adoption-to-station, power per station, models per country.  

---

## 📈 Results & Insights (Typical Findings)  
- **Charging hubs**: Europe, China, and the US dominate, but with very different adoption/station ratios.  
- **Emerging markets**: South America and Africa show adoption growth but lack charging density.  
- **Manufacturers**: Tesla, BYD, and VW lead with model diversity; luxury brands offer high-range but niche models.  
- **Infrastructure vs. Adoption**: Some countries have high EV penetration but lagging infrastructure — a critical gap for policy and investment.  

---

## 🗺️ Visual Gallery  
- 🌐 **Global heatmap** of charging stations.  
- 📊 **Country-level bar plots**: adoption vs. charging ratio.  
- 🚗 **Top manufacturers** by model count.  
- 📉 **Distribution plots**: range, battery capacity, ports per station.  
- 🧭 **Comparative scatterplots**: EV adoption vs. infrastructure density.  

---

## 💡 Policy & Market Implications  
- **Infrastructure investment** needed in adoption-heavy but station-light countries.  
- **Policy incentives** can accelerate balanced EV ecosystem growth.  
- **Market opportunities** for new entrants in underserved regions.  
- **Manufacturers** should align EV rollouts with infrastructure availability to avoid adoption bottlenecks.  

---

## ⚠️ Limitations  
- External datasets — quality depends on original compilers.  
- Limited scope: does not include real-time charging utilization or price signals.  
- Analysis is descriptive, not predictive.  

---

## 🔭 Future Work  
- Add **time-series data** to capture adoption growth.  
- Integrate **real-world usage metrics** (charging demand vs. capacity).  
- Expand to **policy datasets** for richer cross-country comparisons.  
- Build **forecasting models** for EV adoption and infrastructure needs.  

---

