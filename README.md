# ⚡ EV Charging EDA (Global 2025)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#)
[![Notebook](https://img.shields.io/badge/Format-Jupyter%20Notebook-orange)](#)

Decision-ready exploratory analysis for **global EV charging infrastructure** + **EV models** datasets.

---

## 📌 What’s inside

- 📓 Notebooks:
  - `ev-charging-stations-eda.ipynb` (stations + country summaries + light ML table)
  - `global-ev-charging-stations-models-eda-tutorial.ipynb` (2025 refresh + models focus)
- 🧱 Lightweight repo layout: `data/raw` + `artifacts`
- 🧭 Path-safe loading (local `data/raw` + Kaggle fallback)

---

## 📁 Repo layout

```text
.
├── ev-charging-stations-eda.ipynb
├── global-ev-charging-stations-models-eda-tutorial.ipynb
├── data/
│   └── raw/               # put CSVs here locally
├── artifacts/             # saved outputs (optional)
├── repo_utils/
│   └── pathing.py         # local + Kaggle path helper
├── CASE_STUDY.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Open either notebook in Jupyter / VS Code and run top-to-bottom.

---

## 📦 Data (local + Kaggle)

**Local (recommended):**
- Put the CSV files in `data/raw/`
- The notebook loads them via:
  - `resolve_data_path("<file>.csv", kaggle_subdir_hint="global-ev-charging-stations")`

**Kaggle:**
- Works with `/kaggle/input/global-ev-charging-stations/...`

---

## 🧾 Case Study

See: **CASE_STUDY.md** (project story + decisions, without repeating run steps).

---

## 📜 License

MIT (see `LICENSE`)
