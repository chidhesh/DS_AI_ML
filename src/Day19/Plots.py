import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# ---- Line Plot ----
plt.figure()
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# ---- Scatter Plot ----
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# ---- Bar Chart ----
plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# ---- Histogram ----
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.figure()
plt.hist(data)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()