# Define a tuple
tup=(1,5,6)


# If we want to define tuple of one element

tup1=(1,)


# Will give error
# Because tuples are immutable
# tup[2]=0


# Slicing a tuple 
tup2=(1,2,3,4,5,6,7,8,9)

print(tup2[1:5])



# Opeartions on Tuple

tupleTT=(1,2,3,4,5)
temp=list(tupleTT)

temp.append(8) #Add Item
temp.pop(0) #Remove Item
temp[2]=19

tupleTT=tuple(temp)

print(tupleTT)



# Count the occurance

tup3=(0,1,2,3,4,5,6,7,8)

res=tup3.count(1)

# To get the index

resIndex=tup3.index(3)

# We can also pass start and end as a param
# tuple.index(element,start,end)

resIndex=tup3(3,1,4)

# To get length of tuple

resLen=len(tup3)



# Very Very Imp Not Below
# Best way to make any tuple is to 
# make a list from it make the changes
# and make it back to a tuple