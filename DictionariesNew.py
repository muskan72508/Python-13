# Difference between list and dict


# listArr=[1,2,3,4,5]

# index -> 0,1,2,3,4,
# value-> 1,2,3,4,5


# valDict={
#     0:1,
#     1:2,
#     2:3,
#     3:4,
#     4:5
# }
# We have power to create our own key

# vvimp To create a dict we need two things key and value 
# index->key  0,1,2,3,4
# value-> 1,2,3,4,5


# Both give values  [In this case both are same]
# listArr[3]->val
# valDict[3]->val


# We cannot run loop on dict

valDict={
    0:1,
    1:2,
    2:3,
    3:4,
    4:5,
    5:6
}

# # How to access the element


# To get the value pass the key 
# valDict[key]
# But there is one issue if key does not exit gives error


# The best solution is to use get()
# print(valDict.get(keys))
print(valDict.get(10))

key=0
if(valDict.get(key)):
    print("Key Exist")
else:
    print("Key does not Exist")



# How i will loop through


# # To get all the keys
# print(dic.keys())  # Returns a tuple


valList=valDict.keys()
# [key1,key2,key3,key4,key5]

for val in valList:
    print("key is",val)
    print("value is",valDict.get(val))




# We can only get values and there is no way to get key
valList=valDict.values()

for val in valList:
    print("value is",val)



itemLIst=valDict.items()
# [(key1,value1),(key1,value1),(key1,value1),(key1,value1)]


for valTup in itemLIst:

    # (key1,value1)
    key=valTup[0]
    val=valTup[1]
    print("key is",key)
    print("value is",val)
    






# # To remove all items from dictionary
# clear()


sar={
    1:2,
    2:3,
    4:5,
}
# sar.clear()
# print(sar)

# # pop()
# # If we want to remove a sepicific key 

# sar.pop(key)

sar.pop(4)
print(sar)



temp={
    0:"muskan",
    1:"truly",
    2:"dushmans",
    3:"a",
    4:"gandu",
    5:"guy",
    6:"named",
    7:"preeti"
}
# ["MUSKAN","TRULY","dushmanS","A","GANDU"---,"preeti"]
# [(key,valu),(),()]
listitem = temp.items()
ansList=[]
for valTup in listitem:
    valStr = valTup[1]
    newStr=valStr.upper()
    ansList.append(valStr.upper())

print(ansList)  



    