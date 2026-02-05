contacts={
    "Chidhesh":9591671253,
    "Yashwith": 9632857418,
    "Chethan": 841257693
}

print(contacts)

#Adding the contact number of shapun
contacts["Shapun"] = 9876543210
print(contacts)

#Updating the contact number of chidhesh
contacts["Chidhesh"] = 9934567890

#Fetching the contact number of chidhesh
Get_dictionary=contacts.get("Chidhesh")
print("Fetch the Dictionary data :",Get_dictionary)

#Adding defalt value 
Not_found=contacts.get("Abhilash",'Contact not found')
print("Find:",Not_found)

#fetching all contacts
for(name,phone) in contacts.items():
    print(f"Name: {name} | Phone: {phone}")