#Dictionaries in Python
a={
    "name":"chidhesh",
   "age":23,
   "city":"mangalore",
   "profession":"Student",
    "hobbies":["reading","coding","travelling"]
   }

print(a["name"])
print(a["hobbies"][1])
print(a.keys())
print(a.values())
print(a.items())
a["age"]=24
a["hobbies"].append("gaming")
print(a)

marks={
    "maths":90,
    "science":85,
    "english":88
}
print(marks.get("maths"))
print(marks.get("history","0"))
for(subject,score) in marks.items():
    print(subject,score)

marks.update({"science":89})
marks.update({"social":92})
print(marks)
marks.pop("social")
print(marks)
marks.popitem()



# for(name,amount) in purchases.items():
#     print(f"{name} spent ₹{amount}")

n=int(input("Enter number of customer: "))
user_purchases={}

for i in range(n):
    name=input("Enter customer name: ")
    amount=int(input(f"Enter purchase amount for {name}: ₹"))
    user_purchases[name]=amount

print("Customer Purchases Data:", user_purchases)
#Using max()
top_customer = max(user_purchases, key=user_purchases.get)
print("Maximum spending customer:", top_customer)