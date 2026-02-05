friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

union= friend_a & friend_b
print("Common interests:", union)

intersection= friend_a | friend_b
print("All interests:", intersection)
difference= friend_a - friend_b
print("Interests only friend_a has:", difference)