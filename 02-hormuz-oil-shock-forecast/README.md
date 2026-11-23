# 02 - Hormuz Oil Shock Forecast
## Business Problem
If Hormuz is disrupted, what happens to oil price and budget? One number is dangerous. Give a range + scenarios.

## Data (Real, FRED)
- Brent (DCOILBRENTEU): 1305 daily rows, 2021-11-17 to 2026-11-17
- WTI (DCOILWTICO): same range
- Cleaning: FRED missing = holidays/weekends -> forward-fill, NOT mean-fill. Mean would flatten volatility.
- Brent Last: $92.94 | WTI Last: $89.53 | Brent Mean: $85.38 | Max $138.21 Min $59.93

## Models Compared (Last 90 days test)
- Naive Lag-7 MAE: $9.67
- MA30 Baseline MAE: $11.87
- XGBoost Lag-Engineered MAE: None
- SARIMAX (weekly) forecast: $89.31
Rule: Never trust one model. Compare, then give range.

## Monte Carlo - 10,000 paths, 90 days
- Uses daily return mu + sigma, annual vol 43.5%
- P5: $61.0 | P50 (median): $93.5 | P95: $142.9
- Meaning: 90% of paths land between P5 and P95. Budget on P50, plan for P95.

## What-if Scenarios (from current $92.94)
- Base (No shock): $94.8
- Stress (Partial disruption +35%): $125.5
- Shock (Closure +50%): $139.4
Inflation pass-through: Every $10 rise ~ +0.3-0.5pp inflation in importers (rule-of-thumb, show as sensitivity, not promise).

## Now What
1. Budget on Base, keep contingency for Stress.
2. If Brent crosses Stress, trigger fuel surcharge review in 1 week.
3. Re-run weekly - model is not one-time.

## How to Run
pip install -r requirements.txt

python src/forecast.py

Open dashboard.html for result dashboard.


## Tests
python src/test_forecast.py
