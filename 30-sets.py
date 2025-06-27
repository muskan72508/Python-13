
# There is no index and no key in a set
# Set is always unordered


# How to declare a set

# mySet=set()


# Hoe to insert an element in a set [add()]


# mySet.add(1)
# mySet.add(2)
# mySet.add(3)
# mySet.add(4)
# mySet.add(5)


# print(mySet)

# How to delete an element from a set [remove()]

# mySet.remove(1)


# print(mySet)


# how to access the elements in a set

# for val in mySet:
#     print("Element is: ",val)



# # Union 
# s11={1,2,3,4,5}
# s12={5,6,7,8}

# s13=s11.union(s12)
 
# print(s13)


# Intersection

# s14=s11.intersection(s12)

# print(s14)



# Disjoint

# s1={1,2,3,}
# s2={4,5,6}

# If Yes-> If the do not have anything in common
# print(s1.isdisjoint(s2))

# # Subset
# s1={1,2}
# s2={1,2,3,4}

# print(s1.issubset(s2))

# # Superset

# print(s2.issuperset(s1))


# How to convert a set into a list

# listArr=[]
# s1={1,2,3,4}

# for val in s1:
#     listArr.append(val)


# print("Now i am a list: ",listArr)



# 1️⃣ **Create a Set:** Given a list `[1, 2, 3, 4, 5, 1, 2, 3]`, convert it into a set and print the unique elements.  

listarr = [1, 2, 3, 4, 5, 1, 2, 3]
myset = set(listarr)
print(myset)



# 2️⃣ **Add Elements:** Start with an empty set. Add the numbers `5, 10, 15, 20` one by one and display the final set.
# myset = {}
# listarr1 =[]
# listarr1 = listarr.append(5)
# listarr2 = listarr.append(10)
# listarr3 = listarr.append(15)
# listarr4 = listarr.append(20)

# print(myset)


 

# 3️⃣ **Remove an Element:** Given a set `{2, 4, 6, 8, 10}`, remove  `6` and print the updated set.  

myset = {2, 4, 6, 8, 10}
myset.remove(6)
print(myset)

# 4️⃣ **Union of Sets:** Given two sets `{1, 3, 5}` and `{2, 4, 6}`, find and print their union.
s1 = {1, 3, 5}
s2 = {2, 4, 6}
s3 = s1.union(s2)
print(s3)

# 5️⃣ **Intersection of Sets:** Given two sets `{10, 20, 30, 40}` and `{30, 40, 50, 60}`, find the common elements.  
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
s3 = s1.intersection(s2)
print(s3)

# 6️⃣ **Set Difference:** Given two sets `{1, 2, 3, 4, 5}` and `{3, 4, 5, 6, 7}`, find the elements present in the first set but
#  not in the second.  
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
s3 = s1.difference(s2)
print(s3)

# 7️⃣ **Check Membership:** Given a set `{100, 200, 300, 400}`, check if `500` is present in the set and print the result.  

# 8️⃣ **Find Set Length:** Given a set `{1, 3, 5, 7, 9}`, print the total number of elements in it.  

# 9️⃣ **Convert List to Set:** Given a list `[5, 10, 10, 15, 20, 20, 25]`, convert it into a set and print the unique elements.  

# 🔟 **Check Subset:** Given two sets `{1, 2, 3}` and `{1, 2, 3, 4, 5}`, check if the first set is a subset of the second.  

# 11-Remove Duplicates from a String: Given a string "banana", remove duplicate letters and print the unique characters.