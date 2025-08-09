# AI Platform Pricing & Competition (GitHub-Only Workflow)

This repo scrapes AI pricing pages (placeholder selectors), cleans the data, runs OLS and panel FE regressions, and produces a pricing trend chart. It is designed to run **online** using **GitHub Actions** or **GitHub Codespaces** (no Jupyter needed).

## Folder Structure
```
ai-pricing-competition/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── scrape_pricing.py
│   ├── clean_and_regress.py
│   └── visualize.py
├── .github/workflows/run.yml     # GitHub Actions CI workflow
├── requirements.txt
├── run_all.sh
└── README.md
```

## Quick Start (GitHub Actions - 100% Online)
1. Create an empty GitHub repo and upload these files.
2. Go to the **Actions** tab.
3. If prompted, click **"I understand… enable workflows"**.
4. Click **"Run workflow"** → select **main** branch → **Run**.
5. After a minute, open the **latest workflow run** → **Artifacts** → download `outputs`:
   - `data/raw/pricing_raw.csv`
   - `data/processed/pricing_cleaned.csv`
   - `data/processed/pricing_trend.png`
6. The regression summaries are visible in the job logs under **"Run cleaning & regressions"**.

> Note: The HTML structures of pricing pages change frequently and some are JavaScript-rendered. The included scraper is intentionally simple and will **fall back to sample data** if it can't parse a page, so the pipeline always completes.

## Run in GitHub Codespaces (Interactive Shell Online)
1. On your repo page, click **Code** → **Codespaces** → **Create codespace on main**.
2. In the terminal that opens, run:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ./run_all.sh
   ```
3. Check outputs in `data/` folders and open `data/processed/pricing_trend.png` from the Explorer.

## Local Run (Optional)
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
./run_all.sh
```

## Next Steps
- Replace placeholder scraping with provider-specific selectors.
- Add region-specific pricing and regulation measures.
- Schedule nightly runs with a cron in the workflow (e.g., `on: schedule:`).
