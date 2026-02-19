import numpy as np
import pandas as pd

np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=1000)
data = np.append(data, [150, -20, 200])

df = pd.DataFrame(data, columns=["value"])
mu = df["value"].mean()
sigma = df["value"].std()

print("\nMean (μ):", mu)
print("\nStandard Deviation (σ):", sigma)

df["z_score"] = (df["value"] - mu) / sigma
outliers = df[np.abs(df["z_score"]) > 3]

print("\nStatistical Outliers (|Z| > 3):")
print(outliers)
print("\nTotal Outliers Found:", len(outliers))