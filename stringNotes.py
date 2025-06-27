
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





# String
# 0- How to input a string
# str11=input()

# 1- How to define a string
str11="kjnkj"

# 2- How to run a loop [on value,by index]

# 1- Method1 [On value]
# for val in str11:
#     print(val)

# 2- Method2 [On index]
# for index in range(0,len(str11)):
#     print("Index is: ",index)
#     print("Value is: ",str11[index])

# 3- Functions
# len
str11="kjdzfn"

# Pass the string as argement
len(str11)


# upper 
str12=str11.upper()

# lower
str12=str11.lower()

# capitalize
str12=str11.capitalize()

# find

# If we the string is found returns index
# First Occurance
# If string is not found return -1

res=str11.find("jfn")

# replace

res=str11.replace("What to replace","New Item to come")

# count

res=str11.count("Which item to count")

# split
# Breaks the string and return the list

resArr=str11.split("a")


# 4- Converting a string to list

# If we want to make a list 
#1- by breaking it from a some parts

# str11="preeti is not a jdf"
# If we want to break on space

# listArr=str11.split(" ")
# ["preeti",'is',"not","a",'jdg']

# str11="preetiisnotisaisjdf"
# If we want to break on "is"

# listArr=str11.split("is")
# ["preeti","not","a",'jdg']

# 2- When we don't want to break 
# and want every character

# listArr=[]

# for val in str1:
#     listArr.append(val)




# 5- Convering a list to string

# ans=""
# for val in list:
#     ans=ans+val



#6- Slincing

str="kdlflknfg"

# str[start:end:jump]

# Default
# start->0
# end-> Till ending not stop anywhere
# jump->1

# For negartive value of start and end
# add length to the value

# 7- Insertion
ans=""

ans=ans+"kjsngkj"

# 8-Deletion [Same as list]

ans=""

for val in str12:
    if(val!="Item to delete"):
        ans=ans+val

#9- Sorting
# 1-Convert to list
# 2- Then  sort
# 3- Again list to string


temp=[]

for val in str11:
    temp.append(val)

temp.sort()

ans=""

for val in temp:
    ans=ans+val

print(ans)

# 10- Direct assigment not possible because strings are immutable


sar="sdlkfgnk"

# Not possible even we can another variable because 
# it points a same address
# sar[0] = "a"
# mus=sar
# mus[0]="a"

# print(mus)

ans=""

for index in range(0,len(sar)):
    if(index==5):
        ans=ans+"z"
    else:
        ans=ans+sar[index]

print(ans)