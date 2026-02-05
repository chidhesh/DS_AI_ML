raw_logs=["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

unique_users=set(raw_logs)

check_unique= "ID05" in unique_users

len_orignal=len(raw_logs)
len_unique=len(unique_users)

loss_logs=len_orignal - len_unique

print(raw_logs)
print("Check if ID05 is in unique users:", check_unique)
print("Length of oringal logs:", len_orignal)
print("Length of unique logs:", len_unique)
print("Loss of logs due to duplicates:", loss_logs)