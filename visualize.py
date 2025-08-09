import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    df = pd.read_csv("data/processed/pricing_cleaned.csv")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])

    plt.figure(figsize=(10, 5))
    for provider in sorted(df["provider"].unique()):
        subset = df[df["provider"] == provider].sort_values("date")
        plt.plot(subset["date"], subset["price_1k_tokens"], label=provider)

    plt.xlabel("Date")
    plt.ylabel("Price per 1k tokens ($)")
    plt.title("AI Model Pricing Over Time")
    plt.legend()
    os.makedirs("data/processed", exist_ok=True)
    out = "data/processed/pricing_trend.png"
    plt.savefig(out, bbox_inches="tight")
    print(f"[ok] Saved figure: {out}")

if __name__ == "__main__":
    main()
