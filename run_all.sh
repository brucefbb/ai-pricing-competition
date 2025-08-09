#!/bin/bash
set -e

# Activate venv if present (optional)
if [ -d "venv" ]; then
  source venv/bin/activate 2>/dev/null || true
fi

python3 src/scrape_pricing.py
python3 src/clean_and_regress.py
python3 src/visualize.py
