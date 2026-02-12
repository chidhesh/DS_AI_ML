import pandas as pd

# Load dataset
df = pd.read_csv("customer_order.csv")

# Check initial data types
print("Initial Data Types:\n")
print(df.dtypes)

# Clean Price column (remove $ and convert to float)
df["price"] = df["price"].astype(str).str.replace("$", "", regex=False).astype(float)

print(df["price"])

# Convert Date column to datetime
df["order_date"] = pd.to_datetime(df["order_date"], format="%d-%m-%Y")

# Check updated data types
print("\nUpdated Data Types:\n")
print(df.dtypes)