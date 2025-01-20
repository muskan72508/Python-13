# Always remember unlike set
# dictionary are always alphabetic
# sorted order of key 


dic={
    "Harry":"Human Being",
    "Spoon":"Object"
}

# How to access the element

# Throws error if key doen not exist
print(dic["Spoon"])

# Throws null if key doen not exist
print(dic.get("Spoon"))

# To get all the keys
print(dic.keys())  # Returns a tuple

# To get all the values
print(dic.values())  # Returns a tuple

for key in dic.keys():
    print(f"The value of coresponding to the key {key} is {dic[key]}")


# To get key value pair
print(dic.items())  # Returns a tuple

for key,value in dic.items():
    print(f"The value of coresponding to the key {key} is {value}")


# Methods on Dictionaries

# 1- Update a dictionary
# Update the values of the key if present
# else create a new key value pair

ep1 ={
    122:45,
    123:89,
    567:69,
    670:69,
}
ep2 ={
   222:67,
   122:90
}

ep1.update(ep2)

print(ep1)


# 2- clear()
# To remove all items from dictionary

# 3- pop()
# If we want to remove a sepicific key 
ep1.pop(122)
print(ep1)

# If we want to remove last element from dictionary 
ep1.popitem()
print(ep1)

