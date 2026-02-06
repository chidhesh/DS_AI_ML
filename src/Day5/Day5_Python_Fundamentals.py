#Functions
def greet():
    print("Hello, welcome to Python Fundamentals!")
greet()

#Argumentats and return values
def add(a, b):
    return a + b
result = add(5, 3)
print("The sum of 5 and 3 is:", result)

#Variable scope
x=10
def value_x():
    x=5
    print("Inside the function, x =", x)
value_x()
print("Outside the function, x =", x)


#
company="TechCorp"
def display_company():
    global company
    company="InnoTech"
    print("Inside the function, company =", company)

display_company()
print("Outside the function, company =", company)   

#importing function modules
import math
import random

print(math.sqrt(16))
print(random.randint(1, 100))
print(random.uniform(1.0, 100.0))