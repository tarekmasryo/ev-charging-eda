# EV Charging Stations EDA

Decision-ready exploratory analysis for a global EV charging infrastructure dataset, with robust validation notes, country and city-level infrastructure views, EV model summaries, and a leakage-aware baseline for fast-DC signals.

## What is included

- `ev-charging-stations-eda.ipynb` — the main Kaggle-ready notebook.
- `CASE_STUDY.md` — concise project story, decisions, limitations, and next steps.
- `repo_utils/pathing.py` — optional local/Kaggle path helper for reproducible data loading.
- `data/raw/.gitkeep` — placeholder for local CSV files.
- `artifacts/.gitkeep` — placeholder for optional exported outputs.

## Repository layout

```text
.
├── ev-charging-stations-eda.ipynb
├── CASE_STUDY.md
├── LICENSE
├── README.md
├── requirements.txt
├── data/
│   └── raw/
│       └── .gitkeep
├── artifacts/
│   └── .gitkeep
└── repo_utils/
    ├── __init__.py
    └── pathing.py
```

## Dataset files

The notebook expects the following files, either from the Kaggle dataset input or from `data/raw/` when running locally:

```text
charging_station.csv
country_summary.csv
ev_models.csv
world_summary.csv
charging_station_ml.csv
```

Raw data files are intentionally not committed to this repository. Keep them under `data/raw/` locally, or attach the dataset to the Kaggle notebook.

## Run locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
jupyter lab
```

Then open:

```text
ev-charging-stations-eda.ipynb
```

If the CSV files are stored outside `data/raw/`, set:

```bash
EV_CHARGING_DATA_DIR=/path/to/dataset
```

## Kaggle usage

Attach the dataset to the notebook on Kaggle. The notebook resolves files from:

```text
/kaggle/input/global-ev-charging-stations/
```

It also falls back to a light Kaggle input search if the attached dataset folder name differs.

## What the notebook does

- Reviews table shapes, schema, missing metadata, duplicate rows, and location placeholder buckets.
- Preserves raw records while creating analysis-safe columns for robust aggregate metrics.
- Builds country-level and city-level infrastructure summaries.
- Uses minimum-count filters for fairer country rankings.
- Separates known city labels from placeholder city labels in city rankings.
- Compares fast-DC coverage, power distributions, country typologies, and EV model patterns.
- Includes a leakage-aware city-level baseline that avoids power-derived features when modeling fast-DC presence.

## Notes on interpretation

This is an exploratory and decision-support notebook. It is designed to make the dataset easier to inspect, explain, and reuse in dashboards or downstream modeling.

The notebook keeps raw values available, while robust aggregate metrics avoid letting high-end reported power values dominate rankings, clustering, or summary statistics.

## License

MIT. See `LICENSE`.
