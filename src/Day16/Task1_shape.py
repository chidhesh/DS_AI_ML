import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

normal_data = np.random.normal(170, 10, 500)
right_skewed = np.random.exponential(2, 500) 
left_skewed = 100 - np.random.exponential(2, 500)

datasets = {
    "Normal": normal_data,
    "Right-Skewed": right_skewed,
    "Left-Skewed": left_skewed
}

plt.figure(figsize=(15, 4))  

for i, (name, data) in enumerate(datasets.items(), 1):
    df = pd.DataFrame({"Value": data})

    mean = df["Value"].mean()
    median = df["Value"].median()

    plt.subplot(1, 3, i)  
    sns.histplot(df["Value"], kde=True)
    plt.title(f"{name}\nMean={mean:.2f}, Median={median:.2f}")

    print(f"{name}- Mean: {mean:.2f}, Median: {median:.2f}")

plt.tight_layout()
plt.show()