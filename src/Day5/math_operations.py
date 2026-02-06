def calc_rectangle(length, width):
    area= length * width
    perimeter= 2 * (length + width)
    return area, perimeter

result= calc_rectangle(5, 10)
print("Area:", result[0]," Perimeter:", result[1])
