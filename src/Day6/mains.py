
# Import the custom module
import math_operations

# Calculate 2^10 using the power function from the module
base_num = 2
exponent = 10
power_result = math_operations.power(base_num, exponent)
print(f"{base_num}^{exponent} is: {power_result}")

# Calculate the average of [10, 20, 30, 40] using the average function
numbers_list = [10, 20, 30, 40]
average_result = math_operations.average(numbers_list)
print(f"The average of {numbers_list} is: {average_result}")
