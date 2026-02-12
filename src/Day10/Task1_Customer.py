import pandas as pd

# Load dataset
df = pd.read_csv("customer_orders.csv")

# Shape before cleaning
print("Shape Before Cleaning:", df.shape)

# Missing values report
print("\nMissing Values Report:")
print(df.isna().sum())

# Fill missing numeric values with median
numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Remove duplicate rows
df = df.drop_duplicates()

# Shape after cleaning
print("\nShape After Cleaning:", df.shape)
