name=input("Enter the name:")
goal=input("Enter the daily goal:")

with open("journal.txt","a") as file:
    file.write(f"Name: {name}, Daily_Goal:{goal}\n")
