list = []
listarr = [1,2,3,4,56,6]
for val in listarr:
    print(val)


for i in range(0,len(listarr)):
    print("Index is",i)
    print("Value is",listarr[i])




# List of list


mainList = [[1,2],[3,4],[1,2,44]]




for index in range(0,len(mainList)):
    subList=mainList[index]
    sum=0
    for val in subList:
        sum=sum+val

    print(sum)



listStr=["preeti","muskan","naina","mansi"]

for valStr in listStr:
    a=valStr.upper()
    print(a)
    b=valStr.lower()
    print(b)
    c=valStr.capitalize()
    print(c)
    d=valStr.count("a")
    print(d)
    e=valStr.find("a")
    print(e)


listDict=[
    {
        "a":"preeti"
    },
    {
         "a":"muskan"

    },
    {
         "a":"masni"

    }

]

for valDict in listDict:
    print(valDict.get("a"))


listArr=[1,2,4,4,5]

sum=0

for val in listarr:
    sum=sum+val

print(sum)


# Find max and min element in the list

listarr=[3,5,21,2,1,99,32,100,34,87]


#  mx=max(mx,val)








mx = -1
mn=999999999999999
sum=0
count=0
average=-1
for val in listarr:
    sum=sum+val
    count=count+1
    mx=max(mx,val)
    mn=min(mn,val)
    if(val>mx):
        mx=val

    if(val<mn):
        mn=val

print("Maximum is",mx)
print("Minimum is",mn)
print("Sum is",sum)
print("Count is",count)
print("Average is",sum/count)


# Sorting a list 

listarr=[3,5,21,2,1,99,32,100,34,87]


# Method1

sortedlist  = sorted(listarr)
print(sortedlist)

# Method 2

listarr.sort()
print(listarr)



# Methods in the list

# Adding elements to a end of list
listArr=[1,2,3]

listArr.append(5)

print(listArr)

# Inserting at a specific position
# (index,value)
listArr.insert(2,12)
listArr.insert(2,12)
listArr.insert(2,12)
listArr.insert(2,12)

print(listArr)


# Remove first occurance of value

listArr.remove(12)

print(listArr)

# Reverse a lsit

listArr.reverse()

print(listArr)



# List functions to remember

# Sort
# Appemd
# Insert
# Remove
# Reverse



listDict=[
    {
        "a":"preeti",
        "b":"muskan"
    },
    {
        "a":"preeti1",
        "b":"muskan1"
    },
    {
        "a":"preeti2",
        "b":"muskan2"
    }
]


# ['preeti','muskan','preeti1',---,'muskan2']


# [('a', 'preeti'), ('b', 'muskan')]
ansList=[]
for valDict in listDict:
    valList=valDict.items()
    for valTup in valList:

        # ('a', 'preeti')
        key=valTup[0]
        value=valTup[1]
        ansList.append(value)

print(ansList)





# emptyList
# list of numbers
# list of string
# list of list
# list of tuples
# list of dict



