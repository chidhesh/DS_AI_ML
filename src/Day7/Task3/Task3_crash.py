try:
    file_name=input("Enter the file name:")

    with open("file_name","r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("Oops! That file doesn't exist yet")