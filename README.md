# ⚡ EV Charging EDA (Global 2025)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#)
[![Notebook](https://img.shields.io/badge/Format-Jupyter%20Notebook-orange)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Kaggle Ready](https://img.shields.io/badge/Kaggle-Ready-20BEFF)](#)

Decision-ready exploratory analysis for a **global EV charging infrastructure dataset**, with robust validation notes, country and city-level infrastructure views, EV model summaries, and a leakage-aware baseline for fast-DC signals.

---

## 📌 What’s inside

- 📓 **Main notebook**
  - `ev-charging-stations-eda.ipynb` — Kaggle-ready EDA notebook for EV charging stations, country summaries, EV model patterns, and a leakage-aware city-level baseline.
- 🧭 **Path-safe loading**
  - Local `data/raw/`
  - Kaggle input folder
  - Optional `EV_CHARGING_DATA_DIR` environment variable
- 🛡️ **Analysis safeguards**
  - Raw records are preserved.
  - Robust aggregate metrics are used where high-end reported values could dominate rankings or clustering.
- 🧾 **Case study**
  - `CASE_STUDY.md` summarizes the project story, decisions, limitations, and next steps.
- 🧱 **Lightweight repo layout**
  - Simple structure for GitHub, Kaggle, and local notebook runs.

---

## 📁 Repo layout

```text
.
├── ev-charging-stations-eda.ipynb
├── CASE_STUDY.md
├── LICENSE
├── README.md
├── requirements.txt
├── .gitignore
├── .gitattributes
├── data/
│   └── raw/
│       └── .gitkeep
├── artifacts/
│   └── .gitkeep
└── repo_utils/
    ├── __init__.py
    └── pathing.py
```

---

## 📦 Dataset files

The notebook expects these CSV files, either from the attached Kaggle dataset or from `data/raw/` when running locally:

```text
charging_station.csv
country_summary.csv
ev_models.csv
world_summary.csv
charging_station_ml.csv
```

Raw data files are intentionally **not committed** to this repository.

Use one of these options:

- Put the CSV files under `data/raw/`
- Attach the dataset to the Kaggle notebook
- Set `EV_CHARGING_DATA_DIR` to the dataset folder path

---

## 🚀 Run locally

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Jupyter:

```bash
jupyter lab
```

Then open:

```text
ev-charging-stations-eda.ipynb
```

---

## 🧭 Data loading behavior

The notebook uses `repo_utils/pathing.py` to resolve dataset files safely.

It checks:

1. `EV_CHARGING_DATA_DIR`
2. Local `data/raw/`
3. Kaggle input path:
   - `/kaggle/input/global-ev-charging-stations/`
4. A light Kaggle input search if the attached dataset folder name differs

This keeps the notebook reproducible across local development, GitHub review, and Kaggle execution.

---

## 🔍 What the notebook does

- 📊 Reviews table shapes, schema, missing metadata, duplicates, and location placeholder buckets.
- 🛡️ Preserves raw records while creating analysis-safe columns for robust aggregate metrics.
- 🌍 Builds country-level infrastructure summaries.
- 🏙️ Builds city-level infrastructure views while separating known city labels from placeholder city labels.
- ⚡ Compares fast-DC coverage, power distributions, port availability, and country typologies.
- 🚘 Summarizes EV model patterns from the companion models table.
- 🧠 Includes a leakage-aware city-level baseline that avoids power-derived features when modeling fast-DC presence.
- 📌 Ends with practical takeaways for dashboards, planning tools, and future modeling experiments.

---

## 📈 Notebook focus

This is an **exploratory and decision-support notebook**, not a production forecasting system.

The goal is to make the dataset easier to inspect, explain, and reuse for:

- Infrastructure dashboards
- Country and city comparison views
- Fast-charging coverage analysis
- EV market summaries
- Future modeling experiments with external demand signals

---

## 🧾 Case study

For the project story, methodology notes, decisions, and next steps, see:

```text
CASE_STUDY.md
```

---

## 📤 Optional artifacts

The notebook can be extended to save generated outputs under:

```text
artifacts/
```

Examples:

- summary tables
- chart exports
- cleaned analysis snapshots
- model diagnostics

The folder is kept in the repository with `.gitkeep`.

---

## 📜 License

MIT. See [`LICENSE`](LICENSE).
