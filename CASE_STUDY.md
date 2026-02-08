# 🧠 Case Study — EV Charging EDA (Global 2025)

## Problem
Turn raw “one row per station / one row per model” datasets into **decision-ready signals**:
- Where is charging infrastructure dense vs. sparse?
- How does infrastructure relate to country-level EV adoption?
- Which manufacturers dominate model diversity and specs?

## Data
Expected files (place locally under `data/raw/`):
- `charging_station.csv`
- `country_summary.csv`
- `ev_models.csv`
- `world_summary.csv`
- `charging_station_ml.csv`
- `charging_stations_2025_world.csv`
- `country_summary_2025.csv`
- `ev_models_2025.csv`
- `world_summary_2025.csv`

Kaggle fallback is supported via `repo_utils/pathing.py`.

## Approach
- **EDA:** coverage, missingness, duplicates, distributions, and cross-country comparisons.
- **Comparisons:** adoption vs. charging density, fast-DC share, power distribution.
- **Models:** range / battery / manufacturer mix, and market concentration.
- **Light ML (where applicable):** quick baselines for illustrative segmentation / scoring.

## Outputs
- Notebook visuals (charts + tables)
- Reusable path helper: local `data/raw` + Kaggle `/kaggle/input` fallback
- Clean repo layout with `artifacts/` reserved for saved outputs (optional)

## Decisions & Takeaways
- Identify **underserved regions** (adoption rising, charging density lagging)
- Highlight **infrastructure gaps** for policy / investment planning
- Benchmark manufacturers by **model diversity** and spec distribution

## Next Steps
- Add utilization / pricing signals (demand vs. capacity)
- Add time-series snapshots to measure growth and forecast needs
