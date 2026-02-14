import matplotlib.pyplot as plt

# Data
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

trend_values = [100, 200, 350, 300, 500]

# First subplot → Bar Chart
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# Second subplot → Line Plot
plt.subplot(1, 2, 2)
plt.plot(trend_values)
plt.title("Sales Trend")
plt.xlabel("Time")
plt.ylabel("Sales")

# Prevent overlapping
plt.tight_layout()

# Show dashboard
plt.show()
