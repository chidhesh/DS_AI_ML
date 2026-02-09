def calc_rectangle(length, width):
    area= length * width
    perimeter= 2 * (length + width)
    return area, perimeter

user_length = int(input("Enter the length of the rectangle: "))
user_width = int(input("Enter the width of the rectangle: "))
result = calc_rectangle(user_length, user_width)
print("Area:", result[0],", Perimeter:", result[1])


