age=23
height=5.8
name ="Chidhesh"
is_student=True
print(type(age))
print(type(height))
print(type(is_student))
print(type(name))


print("\n")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choice = input("Enter your choice: ")

if choice == '+':
    print("Result:", num1 + num2)

elif choice == '-':
    print("Result:", num1 - num2)

elif choice == '*':
    print("Result:", num1 * num2)

elif choice == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid choice")

print("\n")

name=input("Enter the name:")
print("Welcome,",name+"!")

print("\n")

name = "Chidhesh"
age = 23
message = (f"My name is {name} and I am {age} years old.")
print(message)

print("\n")

integer_value = 9.2
complex_number = complex(integer_value)
print(complex_number)

