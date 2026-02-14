import pandas as pd

df = pd.DataFrame({
    "Location": [" New York", "new york", "NEW YORK ", "Boston", " boston "]
})

print("Before Cleaning:")
print(df["Location"].unique())

# Normalize text
df["Location"] = df["Location"].str.strip().str.title()


print("\nAfter Cleaning:")
print(df["Location"].unique())
