import pandas as pd

products = pd.Series(
    [700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard']
)

laptop_price=products['Laptop']
first_two=products[:2]

print("ALl Products:",products)
print("Laptop Price:",laptop_price)
print("First Two :",first_two)
