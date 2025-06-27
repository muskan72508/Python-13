
# Major Operations
# Define
# Loop
# Insert
# Delete
# Find
# Count
# Replace
# Sort
# Copying
# Assigment





# 1- Define

dict={
    "key":"value",
    "1":"lkdngf",
    23:"dgn",
    "jdfgn":567
}

# 2- Loops->>> keys() values() items()

# When loop is on key
for index in dict.keys():
    print("key is: ",index)
    print("Value is: ",dict[index])


# When loop is on value
for value in dict.values():
    print("Value is: ",value)

# When loop is on Both together

for key,value in dict.items():
    print("key is: ",key)
    print("Value is: ",value)


# 3- How to find a value

dict["key"]
# If not present above code gives error
# Better to use get function

print(dict.get("key"))
# If not present returns null


# 4- Insert 

# dict["key"]="value"


# Delete


if(dict.get("Pass the key")):
    dict.pop("Pass the key")

# dict.pop(3)
# dict.pop("muskan")




# Replace

# If key is present value got overide
# Else new key value got created
dict={
    "key":"value",
    "1":"lkdngf",
    23:"dgn",
    "jdfgn":567
}

dict[23]="fklgnkldgnh"

dict={
    "key":"value",
    "1":"lkdngf",
    23:"fklgnkldgnh",
    "jdfgn":567
}

dict["23"]="fklh"


#  Direct Assigment is possble because dic are mutable

dict[23]=45
