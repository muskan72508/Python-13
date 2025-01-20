# Unordered Collection

s={2,4,2,6}

print(s)


# In set order of items are not maintained
# When we print order might change
info={"sarthak",19,False,5.9,19}
print(info)

# We cannot define an empty 
# set with curly braces unlike a list
# If we do so it will be dictionary


# This will declare an empty set
harry=set()

for value in info:
    print(value)


# Set Methods

s1={1,2,5,6}
s2={3,6,7}


# Merge two set
# Returns a new set but do not manipulate
# s1
print(s1.union(s2))


# To change s1 we can use update function
print(s1,s2)
s1.update(s2)
print(s1,s2)


s3={1,2,5,6}
s4={3,6,7}


# We also have intersection and intersection_update
# intersection returns new set
# intersection_update update the existing set


print(s3.intersection(s4))
s3.intersection_update(s4)
print(s3)

# symmetric_difference
# Returns item not similar to both the set

# symmetric_difference_update
# Updates the existing set with
# item not similar to both the set

s5={1,2,5,6}
s6={3,6,7}

print(s5.symmetric_difference(s6))
s5.symmetric_difference_update(s6)
print(s5)



# difference
# Returns item present in the original set and 
# not in both the sets

# difference_update
# Updates the existing set with
# item present in the original set and 
# not in both the sets

s7={1,2,5,6}
s8={3,6,7}

print(s7.difference(s8))
s7.difference_update(s8)
print(s7)


# set Methods

# 1- isDisjoin()
# set which do not have any intersection

s9={1,2,5,6}
s10={3,6,7}

print(s9.isdisjoint(s10))

# 2- isSuperset()
# Items of one set are present in another set

s11={1,2,5,6}
s12={6}

print(s12.issuperset(s11))
print(s11.issuperset(s12))

# 3- isSubset()
# Items of one set are present in another set
# Reverse of superset

s11={1,2,5,6}
s12={6}

print(s12.issubset(s11))
print(s11.issubset(s12))

# 4- add()
# Want to add an item in the set

s13={1,2,3}
s13.add(4)

print(s13)


# 5- remove() discard()
s14={1,2,3,4,5}

s14.remove(1)
s14.discard(2)

# Difference between remove and discard is
# if we try to delete an item which is not 
# present in the set remove() raises an error
# while discard do not

# 6- clear()
# Delete all the items from the set 

s14.clear()

print(s14)


