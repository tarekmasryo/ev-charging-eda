# Case Study — EV Charging Stations EDA

## Problem

EV charging infrastructure data can quickly become hard to interpret when it spans many countries, cities, station types, port counts, and power levels.

The goal of this project is to turn the dataset into a clear analytical notebook that helps answer:

- Which countries and cities have the largest station coverage?
- Where is fast-DC infrastructure more concentrated?
- How do reported power levels and port counts vary across markets?
- Which EV model manufacturers and release years dominate the model table?
- What safeguards are needed before using this data for rankings, clustering, or baseline modeling?

## Data

The notebook uses five CSV files:

```text
charging_station.csv
country_summary.csv
ev_models.csv
world_summary.csv
charging_station_ml.csv
```

The analysis is structured around three levels:

- Station level: individual charging locations, power, ports, geography, and fast-DC labels.
- City level: aggregated infrastructure features used for rankings, clustering, and baseline modeling.
- Country/model level: country infrastructure summaries and EV model coverage.

## Approach

### 1. Validation notes and analysis safeguards

The notebook preserves raw records and adds analysis-safe columns for robust aggregate metrics.

Examples:

- `power_kw_clean`
- `power_kw_filled`
- `ports_clean`
- `ports_filled`

This prevents high-end reported power values or non-positive port-count rows from distorting summary statistics, rankings, and clustering.

### 2. Country-level infrastructure analysis

The notebook compares station coverage, fast-DC share, port counts, and robust power summaries by country.

A minimum station threshold is used for fast-share rankings, so countries with very small sample sizes do not dominate percentage-based charts.

### 3. City-level infrastructure analysis

The notebook separates known city labels from placeholder location buckets for city rankings.

This keeps the city-level charts focused on interpretable city labels while still preserving placeholder rows in the raw station-level data.

### 4. Leakage-aware baseline

The city-level baseline predicts fast-DC presence using non-power infrastructure features only.

Power-derived features such as `max_power_kw` and `median_power_kw` are intentionally excluded because they are too close to the fast-DC label definition. This makes the baseline more honest as an exploratory diagnostic rather than an inflated predictive claim.

### 5. Clustering and EV model summaries

City clustering uses robust power features and known city labels.

EV model analysis summarizes manufacturer coverage, release timelines, and body-style patterns to connect infrastructure context with the broader EV market table.

## Key decisions

- Keep raw station records intact.
- Use robust aggregate metrics for reporting and visuals.
- Avoid presenting high-end raw values as ordinary summary KPIs.
- Filter small-sample country rankings where percentages can be misleading.
- Exclude placeholder city labels from top-city rankings.
- Use leakage-aware baseline modeling instead of circular power-derived predictors.

## Outputs

The main output is a single Kaggle-ready notebook:

```text
ev-charging-stations-eda.ipynb
```

The notebook can also support future artifacts such as:

- dashboard-ready country summaries
- city infrastructure segments
- validation reports
- baseline modeling experiments

## Limitations

This notebook is an exploratory analysis, not a production forecasting system.

Stronger predictive modeling would need external demand signals such as:

- EV adoption by region
- population density
- traffic or road-network density
- pricing and utilization data
- station age and operator metadata
- policy or incentive context

## Next steps

- Convert the notebook into an interactive infrastructure dashboard.
- Add utilization or pricing data if available.
- Add time-based snapshots for growth analysis.
- Export validated country and city summary tables for downstream use.
