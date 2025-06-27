# # 1- Sorting a String
# # 2- Sorting a List of Numbers
# # 3- Sorting a Tuple
# # 4- Sorting a dictionary by Key
# # 5- Sorting a dictionary by Value
# # 6- Sorting a List of String
# # 7- Sorting a list of list
# # 8- Sorting a list of Tuples
# # 9-Sorting a list of dictionary

# # We will use a single function called sorted
# # This function always return a list after sorting

# # 1- Sorting a String

# # In ascending
# varStr="preeti"

# varStrSorted=sorted(varStr)

# ans=""
# for val in varStrSorted:
#     ans=ans+val
# print("String after sorting is: ",ans)

# # In descending
# varStr="preeti"

# varStrSorted=sorted(varStr,reverse=True)

# ans=""
# for val in varStrSorted:
#     ans=ans+val
# print("String after sorting is: ",ans)

# # 2- Sorting a List of Numbers

# arrList=[10,2,32,21,22,45,11,98]

# arrSorted=sorted(arrList)

# print(arrSorted)


# # 3- Sorting a Tuple

# arrTup=(10,2,32,21,22,45,11,98)

# tupSorted=sorted(arrTup)

# print(tuple(tupSorted))

# # 4- Sorting a dictionary by Key

fruits={
    23:"Muskan",
    12:"preeti",
    56:"Mansi",
    5:"Aditya"
}

# # keysInFruits=fruits.keys()
# sortedKeys=sorted(fruits)

# ansObj={}
# for key in sortedKeys:
#     ansObj[key]=fruits[key]
# print(ans)    



# # 5- Sorting a dictionary by Value

itemsInFruits=fruits.items()
# # [(23,"muskan"),(12,"preeti"),(56,"masnsi"),(5,"Aditya")]

def getMyKey(varTup):
    return varTup[1]

sortedFruitsByValue=sorted(itemsInFruits,key=getMyKey)

ansObj={}

for varTup in sortedFruitsByValue:
    key=varTup[0]
    val=varTup[1]
    ansObj[key]=val

print(ansObj)




# # 6- Sorting a List of String

# arrStr=["muskan","preeti","aditya","naina","anita","mansi"]

# arrStrSorted=sorted(arrStr)

# print(arrStrSorted)




# # 7- Sorting a List of List

# arrList1=[["muskan","preeti","aa"],["aditya","mansi","bb"],["yash","anita","cc"],["mansi","preeti","dd"]]

# def getMyKey(varList):

#     # By First Element
#     # return varList[0]

#     # By Second Element
#     return varList[1]
      
      # By third Element   
#     return varList[2]


# arrList1Sorted=sorted(arrList1,key=getMyKey)

# print(arrList1Sorted)

#  8- Sorting a List of Tuples

# arrList1=[("muskan","preeti"),("aditya","mansi"),("yash","anita"),("mansi","preeti")]

# def getMyKey(varTup):

#     # By First Element
#     # return varTup[0]

#     # By Second Element
#     return varTup[1]

# arrTup1Sorted=sorted(arrList1,key=getMyKey)

# print(arrTup1Sorted)

# 9- Sorting a list of Dictionary

# arrListDict=[

#     {
#         "name":'muskan',
#         "age":12
#     },
#     {
#         "name":'mansi',
#         "age":10
#     },
#      {
#         "name":'anita',
#         "age":50
#     },
#     {
#         "name":'naina',
#         "age":5
#     },
# ]

# def getMyKey(varDict):
#     return varDict["name"]

# arrListDictSorted=sorted(arrListDict,key=getMyKey)
# print(arrListDictSorted)




# arrList1=[("muskan","preeti"),("aditya","mansi"),("yash","anita"),("mansi","preeti"),
#           ("muskan","shubham"),("preeti","agraj")]
# # 
# Sort with first index
# If value at first index is equal sort
# with second index

# 1- You are given a dictionary {'apple': 3, 'banana': 1, 'kiwi': 2, 'pineapple': 4}. Write a Python program to sort the dictionary by the length of its keys.
# 
# fruits = {'apple': 3, 'banana': 1, 'kiwi': 2, 'pineapple': 4}
# newlst = fruits.keys(        )
# print(newlst)
# def getmykey(helpstr):
#     return len(helpstr)
# fruitkeylst = sorted(newlst, key = getmykey)
# ans  = {}
# for key in fruitkeylst:
#     ans[key] = fruits[key]    
# print(ans)

# 2-Given a tuple of tuples ((1, 5), (3, 2), (4, 4), (2, 3)), sort it by the second element of each tuple.


# numbers  =  ((1, 5), (3, 2), (4, 4), (2, 3))

# def getmytup(helptup):
#     return helptup[1]
 
# numberstup = sorted(numbers, key= getmytup)
# print(numberstup)

# 3-Given a dictionary {'x': 50, 'y': 20, 'z': 10, 'w': 40}, write a Python program to sort the dictionary by its values in descending order and return it as a list of tuples.


num = {'x': 50, 'y': 20, 'z': 10, 'w': 40}
newnum = num.items()
print(newnum)
[('x' ,50) , ('y', 20) , ('z', 10)]
def getmykey(tup):
    return tup[1]
newnum1 = sorted(newnum , key = getmykey , reverse  = True)
print(newnum)




# 4-You have a list of lists [[3, 2, 1], [1, 1, 1], [2, 3], [4]]. Write a Python program to sort the list of lists by the sum of their elements.


# listHelp=[[3, 2, 1], [1, 1, 1], [2, 3], [4]]

# def getMyKey(helpList):
#     sum = 0
#     for val in helpList:
#         sum = sum+ val
#     return sum

# listHelpSorted=sorted(listHelp,key=getMyKey)

# print(listHelpSorted)





# 6-You are given a list of strings ["apple", "banana"].", "kiwi", "pineapple Write a Python program to sort the strings based on the number of vowels in each word.


strings = ["apple", "banana", "kiwi", "pineapple"]
def getmykey(helpstrings):
    count = 0
    for val in helpstrings:
        if val == "a" or val == "e" or val == "i" or val == "o" or val == "u":
            count = count +1
    return count        


stringsorted = sorted(strings , key = getmykey)
print(stringsorted)
