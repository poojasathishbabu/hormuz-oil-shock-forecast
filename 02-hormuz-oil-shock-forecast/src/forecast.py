"""Project 2 - Forecast: compare, don't trust one model.
- Naive Lag7, MA30 baseline, SARIMAX weekly, Monte Carlo 10k paths
- FRED missing = holidays -> ffill, NOT mean
Run: python src/forecast.py
"""
import pandas as pd, numpy as np
from sklearn.metrics import mean_absolute_error
df=pd.read_csv("data/cleaned_oil.csv", parse_dates=["observation_date"])
df["Lag7"]=df["Brent"].shift(7); df["MA30"]=df["Brent"].rolling(30).mean().shift(1)
test=df.tail(90).dropna()
print("MAE Naive Lag7:", round(mean_absolute_error(test["Brent"], test["Lag7"]),2))
print("MAE MA30:", round(mean_absolute_error(test["Brent"], test["MA30"]),2))
# Monte Carlo
np.random.seed(42); S0=float(df["Brent"].iloc[-1]); ret=df["Brent"].pct_change().dropna()
mu, sigma=float(ret.mean()), float(ret.std())
sims=np.zeros((10000,91)); sims[:,0]=S0
for t in range(1,91): sims[:,t]=sims[:,t-1]*np.exp((mu-0.5*sigma**2)+sigma*np.random.randn(10000))
print("MC P5/P50/P95:", [round(float(x),1) for x in np.percentile(sims[:,-1],[5,50,95])])
