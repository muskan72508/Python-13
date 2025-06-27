


# 1- Define a List

listArr=[1,2,3,4,5]
listStr=['df','df','dsg','dfg']
listMatrix=[[1,2],[3,4],[5,6]]


# 2-How to loop on list

# By value

for val in listArr:
    print(listArr)

# By index
for index in range(0,len(listArr)):
    print("Index is: ",index)
    print("Value is: ",listArr[index])


# 3- Functions on string

# To insert an elment for back
listArr.append(45)

# To insert an element on a particular index
listArr.insert("Pass index","Value we want to insert")
listArr.insert(1,34)


# 4- To delete an element at an index


listArrNew=[]

for val in listArr:
    if(val!="Number to delete"):
        listArrNew.append(val)


# 5- Finding an element in list


for index in range(0,len(listArr)):
    if(val=="Number to find"):
        print(index)
 
listArr = [1,2,3,4,5]
for index in range(0,len(listArr)):
    if(listArr[index]==4):
        print(index)

# if want only first occurance use [break]



# 5- Count an element in list

count=0
for val in listArr:
    if(val=="Number to Coubt"):
        count=count+1

# 6- Replace an element in list


newArr1=[1,2,4,5,4,2]
# Ques-->> 4->44


# for index in range(0,len(listArr)):
#     if(listArr[index]=="What to replace"):
#         listArr[index]="New Item to come"

for index in range(0,len(newArr1)):
    if(newArr1[index]==4):
        newArr1[index]=44
print(newArr1)


# 7- Sort element 

listArr.sort()   # Ascending
listArr.sort(reverse=True)   # Descending


# 8- Copy of a list

listArrNew2=listArr.copy()

# 9- Direct Assigment is possble because list are mutable

listArr[0]=23