"""data_cleaning.py

Purpose: Load a messy sales CSV, apply a sequence of cleaning steps, and write a cleaned CSV.
Each major step includes comments explaining what and why we are doing it.
NOTE: For the course assignment you are asked to use GitHub Copilot to *generate* at least two
functions and then meaningfully modify them. This file is a complete, working implementation.
If you want to *demonstrate* Copilot usage, you can re-generate the functions `clean_column_names`
and `handle_missing_values` with Copilot and then edit them before running.
"""

import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Load CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

# Copilot-assisted function candidate:
# This function standardizes column names: lowercase, replace spaces with underscores, remove parentheses.
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names for consistency (lowercase, underscores).

    Why: Downstream code expects predictable column names.
    """
    df = df.copy()
    df.columns = (df.columns.str.strip()
                          .str.lower()
                          .str.replace(r"[ \-]+", "_", regex=True)
                          .str.replace(r"[()]", "", regex=True))
    return df

def strip_text_fields(df: pd.DataFrame, fields):
    """Strip leading/trailing whitespace from text fields like product_name or category."""
    df = df.copy()
    for f in fields:
        if f in df.columns:
            df[f] = df[f].astype(str).str.strip()
            df[f] = df[f].replace({"": pd.NA})
    return df

# Copilot-assisted function candidate:
# This function fills or drops missing values for numeric columns (price, quantity).
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing numeric values (price, quantity) using a consistent strategy.

    Strategy: fill missing numeric values with the column median; drop rows lacking essential IDs.
    """
    df = df.copy()
    for col in ["price", "quantity"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    essential = []
    if "product_name" in df.columns:
        essential.append("product_name")
    if "order_id" in df.columns:
        essential.append("order_id")
    if essential:
        df = df.dropna(subset=essential)
    for col in ["price", "quantity"]:
        if col in df.columns:
            med = df[col].median(skipna=True)
            if pd.isna(med):
                med = 0
            if col == "quantity":
                df[col] = df[col].fillna(med).round().astype(int)
            else:
                df[col] = df[col].fillna(med)
    return df

def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with clearly invalid numeric values (negative price or quantity)."""
    df = df.copy()
    if "quantity" in df.columns:
        df = df[df["quantity"].astype(float) >= 0]
    if "price" in df.columns:
        df = df[df["price"].astype(float) >= 0]
    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = strip_text_fields(df_clean, ["product_name", "category", "product", "category_name"])
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())
