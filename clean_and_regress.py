import pandas as pd
import numpy as np
import statsmodels.api as sm
from linearmodels.panel import PanelOLS
import os

def main():
    # Load raw data
    raw_path = "data/raw/pricing_raw.csv"
    df = pd.read_csv(raw_path)

    # Add placeholder features (replace with your true features later)
    rng = np.random.default_rng(42)
    df["competition_index"] = rng.integers(1, 5, size=len(df))
    df["regulation_index"] = rng.random(len(df))

    # --- OLS Regression: price ~ competition + regulation ---
    X = df[["competition_index", "regulation_index"]]
    X = sm.add_constant(X)  # intercept
    y = df["price_1k_tokens"]
    ols_model = sm.OLS(y, X).fit()
    print("\n=== OLS Results ===")
    print(ols_model.summary())

    # --- Panel Regression (Entity + Time FE) ---
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    if not {"provider", "date"}.issubset(df.columns):
        raise ValueError("Data must contain 'provider' and 'date' columns.")
    df_panel = df.set_index(["provider", "date"]).sort_index()

    if len(df_panel.index.get_level_values(1).unique()) < 2:
        print("\n[warn] Only one date in data; TimeEffects not estimable. Running EntityEffects only.")
        formula = "price_1k_tokens ~ competition_index + regulation_index + EntityEffects"
    else:
        formula = "price_1k_tokens ~ competition_index + regulation_index + EntityEffects + TimeEffects"

    panel_model = PanelOLS.from_formula(formula, data=df_panel)
    panel_results = panel_model.fit(cov_type="clustered", cluster_entity=True)
    print("\n=== Panel FE Results ===")
    print(panel_results.summary)

    # Save processed
    os.makedirs("data/processed", exist_ok=True)
    processed_path = "data/processed/pricing_cleaned.csv"
    df.to_csv(processed_path, index=False)
    print(f"\n[ok] Saved cleaned data: {processed_path}")

if __name__ == "__main__":
    main()
