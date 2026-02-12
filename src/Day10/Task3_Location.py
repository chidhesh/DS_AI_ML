import pandas as pd

# Example dataset
df = pd.DataFrame({
    "Location": [" New York", "new york", "NEW YORK ", "Boston", " boston "]
})

# Before cleaning
print("Before Cleaning:")
print(df["Location"].unique())

# Normalize text
df["Location"] = df["Location"].str.strip().str.title()

# After cleaning
print("\nAfter Cleaning:")
print(df["Location"].unique())
