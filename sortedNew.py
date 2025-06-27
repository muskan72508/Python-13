# # 1- Sorting a String
# # 2- Sorting a List of Numbers
# # 3- Sorting a Tuple
# # 4- Sorting a dictionary by Key
# # 5- Sorting a dictionary by Value
# # 6- Sorting a List of String
# # 7- Sorting a list of list
# # 8- Sorting a list of Tuples
# # 9-Sorting a list of dictionary



# sorted ------>>  It always return a list 




# 1- Sorting a String


str1="Muskan"
str11=str1.lower()


arrSorted=sorted(str11)

ans=""
for val in arrSorted:
    ans=ans+val
print("Sorted String is",ans)


#  # 2- Sorting a List of Numbers

arrList=[1,45,21,4,21,67]

arrSorted=sorted(arrList)

print("Sorted List is",arrSorted)


# 3- Sorting a Tuple

tup=(23,1,533,12,324,12,1)
arrSorted=sorted(tup)
print("Sorted Tupele is: ",tuple(arrSorted))
 



# Expected output: (1, 2, 3, 'apple', 'banana')


# # 4- Sorting a dictionary by Key

# fruits={
#     23:"Muskan",
#     12:"preeti",
#     56:"Mansi",
#     5:"Aditya"
# }

# arrSorted=sorted(fruits)
# print(arrSorted)

# ansDict={}

# for key in arrSorted:
#     value=fruits[key]
#     ansDict[key]=value

# print("Sorted Dic by key is: ",ansDict)


# # 5- Sorting a dictionary by Value


# fruits={
#     23:"Muskan",
#     12:"preeti",
#     56:"Mansi",
#     5:"Aditya"
# }
# Aditya,Mansi,Muskan,preeti
# 5 56 23 12


# def getMyKey(arg):

#     # This will sort by key
    # return arg

#     # This will sort by value
    # return fruits[arg]

# arrSorted=sorted(fruits,key=getMyKey)

# ansDict={}

# for key in arrSorted:
#     value=fruits[key]
#     ansDict[key]=value

# print("Sorted Dic by value is: ",ansDict)



# 6- Sorting a List of String

# arrStr=["muskan","preeti","aditya","naina","anita","mansi"]

# arrStrSorted=sorted(arrStr)

# print(arrStrSorted)




# 7- Sorting a List of list


# arrList1=[["muskan","preeti","aa"],["aditya","mansi","bb"],["yash","anita","cc"],["mansi","preeti","dd"]]


# arrList1=[[21,3,4],[5,16,1],[56,9,2]]



# def getMyKey(arg):
#     print(arg)
#     firstElement=arg[0]
#     return firstElement

# arrSorted=sorted(arrList1,key=getMyKey)

# print(arrSorted)


# 8- Sorting a List of tuples



# arrList1=[("muskan","preeti"),("aditya","mansi"),("yash","anita"),("mansi","preeti")]

# def getMyKey(arg):
#     # By First Element
#     return arg[0]

# arrTup1Sorted=sorted(arrList1,key=getMyKey)

# print(arrTup1Sorted)


# # 9- Sorting a List of dict



# arrListDict=[

    # {
    #     "name":'muskan',
    #     "age":12
    # },
    # {
    #     "name":'mansi',
    #     "age":10
    # },
    #  {
    #     "name":'anita',
#         "age":50
#     },
#     {
#         "name":'naina',
#         "age":5
#     },
# ]

# def getMyKey(arg):
#     print(arg["name"])
#     return arg["name"]

# arrSorted=sorted(arrListDict,key=getMyKey)

# print(arrSorted)



# 10- Sorting as per sum



# arr1=[[2,3,1],[4,16,7],[2,6,1],[5,2,0]]


# def getMyKey(arg):
#     sum=0
#     for val in arg:
#         sum=sum+val
#     return sum
# arrSorted=sorted(arr1,key=getMyKey)

# print(arrSorted)
