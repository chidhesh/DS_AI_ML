user_length = int(input("Enter the length of the rectangle: "))
user_width = int(input("Enter the width of the rectangle: "))

rectangle_area, rectangle_perimeter = calc_rectangle(user_length, user_width)
print(f"Area: {rectangle_area}, Perimeter: {rectangle_perimeter}")