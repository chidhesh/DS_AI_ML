# file=open("Sample.txt",'w')
# file.write("Hello, this is a file handling example")
# file.close()

# file=open("Sample.txt","r")
# content=file.read()
# print(content)
# file.close()


# with open("Sample.txt","r") as file:
#     content=file.read()
# print(content)


# try:
#     with open("missing.txt","r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found, Please check the fileame")

import csv
import openpyxl

with open("Data.csv","r") as file:
    reader=csv.reader(file)

    # for row in reader:
    #     print(row)

    for row in reader:
        print(row[0], row[1],row[2])
    
table=openpyxl.load_workbook("Data.xlsx")
sheet=table.active
for row in sheet.iter_rows(values_only=True):
    print(row)