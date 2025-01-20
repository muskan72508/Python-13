l=[11,45,1,3,32,13]

print(l)

# Insert number at end of list
l.append(7)

# Sort the list
l.sort()

# Reverse the list
l.sort(reverse=True)


# Count number of Occurences of Item
num=l.count(1)

# If we make another list from l
# And change the new list
# Original list also changes
# Since variable only points to a memory
m=l
m[0]=0
print(l)
print(m)

# To make a copy better to use a copy function
n=l.copy()


# If we want to insert a number at a index
# Insert Number 89 at index 1
l.insert(1,89)

# If we want to join new list
m=[9,11,12]
l.extend(m)
print(l)

# Above thing appends into list l
# To create new list without changing l

k=l+m

print(k)