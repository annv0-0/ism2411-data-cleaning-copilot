# ism2411-data-cleaning-copilot

Small project to clean a messy sales CSV for ISM2411 assignment. The repo contains a script
`src/data_cleaning.py` that performs column standardization, text stripping, missing value handling,
and removal of invalid rows. Run from the project root:

```bash
python src/data_cleaning.py
```

Input (raw): `data/raw/sales_data_raw.csv`
Output (clean): `data/processed/sales_data_clean.csv`
