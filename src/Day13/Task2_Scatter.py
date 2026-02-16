import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("housing_data.csv")

# Scatter Plot (Numerical vs Numerical) 
plt.subplot(1,2,1)
sns.scatterplot(x=df["Area_sqft"], y=df["Price"])
plt.title("House Size vs Price")
plt.xlabel("Area (sqft)")
plt.ylabel("Price")
plt.tight_layout()

# Boxplot (Categorical vs Numerical) 
plt.subplot(1,2,2)
sns.boxplot(x=df["City"], y=df["Price"])
plt.title("City vs Price Distribution")
plt.xlabel("City")
plt.ylabel("Price")
plt.show()
