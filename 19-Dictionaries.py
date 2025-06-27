# # Always remember unlike set
# # dictionary are always alphabetic
# # sorted order of key 


# dic={
#     "Harry":"Human Being",
#     "Spoon":"Object"
# }

# # How to access the element

# # Throws error if key doen not exist
# print(dic["Spoon"])

# # Throws null if key doen not exist
# print(dic.get("Spoon"))

# # To get all the keys
# print(dic.keys())  # Returns a tuple

# # To get all the values
# print(dic.values())  # Returns a tuple

# for key in dic.keys():
#     print(f"The value of coresponding to the key {key} is {dic[key]}")


# # To get key value pair
# print(dic.items())  # Returns a tuple

# for key,value in dic.items():
#     print(f"The value of coresponding to the key {key} is {value}")


# # Methods on Dictionaries

# # 1- Update a dictionary
# # Update the values of the key if present
# # else create a new key value pair

# ep1 ={
#     122:45,
#     123:89,
#     567:69,
#     670:69,
# }
# ep2 ={
#    222:67,
#    122:90
# }

# ep1.update(ep2)

# print(ep1)


# # 2- clear()
# # To remove all items from dictionary

# # 3- pop()
# # If we want to remove a sepicific key 
# ep1.pop(122)
# print(ep1)

# # If we want to remove last element from dictionary 
# ep1.popitem()
# print(ep1)



# dict1={
#     12:"sartaka",
#     13:"klxfdgm",
#     14:"dlkg",
#     15:"d,g",
# }

# # get keys values items clear pop update


# python={
#     "aa":"preeti",
#     "bb":"muskan",
#     "cc":"aditya",
#     "dd":"mansi"
# }

# # To get a specific value from key


# # This will brek the code
# # python["aa"]
# # while if we use get 
# # and we don't find the key we will get null
# print(python.get("aa"))
# print(python.get("ee"))


# # Return a tuple of all keys in python dictionary
# print(python.keys())
# ["aa","'bb","cc","dd"]

# for key in python.keys():
#     print("The keys is: ",key)
#     print("The value on that key is: ",python[key])

# print(python.values())
# ["preeti","muskan","aditya","mansi"]

# for val in python.values():
#     print(val)

# for key,value in python.items():
#     print("Key is: ",key)
#     print("Value is: ",value)



# # To clear all the keys and to empty the dictionary
# python.clear()

# # To add a new key
# python["ee"]="naina"

# # To delete a key
# python.pop("ee")

# # To merge two dictionary

# # Update the values of the key if present
# # else create a new key value pair
# python1={
#     "dd":"priya",
#     "ee":"yash"
# }
# python.update(python1)
# print(python)




# python1={
#     0:"jf",
#     3:"lmdg",
#     4:"kdgm",
#     1:"ksmfg",
#     2:"kgm"
# }
# python1[7]="fgkmn"
# python1[6]="kdsf"
# print(python1)




# # Three basic stuff

# # get()   
# # Takes only one argument that is a key and returns value
# # present on it

# # keys()
# # Returns a tuple of keys in a dict


# # pop()
# # To delete a key
# # Takes only one argument that is a key and
# # delete the key value pair


dictHep={
    "storeNumber":1,
    "storeString":"Help me",
    "storeListOfNumbers":[1,23,13,14,5],
    "storeListOfStrings":["Mus","Sar","Man"],
    "storeDic":{
        "apple":10,
        "banana":15,
        "carrot":{
            "carrot1":12,
            "carrot2":121,
            "carrot3":122,

        }
    }

}

# getMeMyNumber=dictHep.get("storeNumber")
# getMeMyString=dictHep.get("storeString")
# getMeMyList=dictHep.get("storeListOfNumbers")

# getMeMyDic=dictHep.get("storeDic")
# getMeMyDic2=getMeMyDic.get("carrot")


# for key in getMeMyDic.keys():
#     print(key)

# for key in getMeMyDic2.keys():
#     print(key)



kmc={
    "professor":["aa","bb","cc"],
    "clubs":["Malang","Mortage","Fractal"],
    "students":[
        {
            "name":"Muskan",
             'id':1
        },
        {
            "name":"Mansi",
             'id':2
        },
        {
            "name":"Priya",
             'id':3
        }
    ],
    "studentOrder":{
        "Zomato":{
            "Office":{
                "South":{
                    "kamla":[1,2,32,11,45],
                    "est2":[3,6]
                    
                },
                "East":[2,3],
                "West":[3,6]
            },
            "Rating":5
        },
        "Swiggy":{
            "Office":"Mumbai",
            "Rating":4
        },
        "Zepto":{
            "Office":"Bandra",
            "Rating":3
        }
    }
}

# listAddr=kmc.get("studentOrder").get("Zomato").get("Office").get("South").get("kamla")
# listAddr.sort()
# print(listAddr)

# getmyorderDict = kmc.get("studentOrder")
# getmycompaniestup = getmyorderDict.keys()

# for companiesNameStr in getmycompaniestup:
#     companyDataDict=getmyorderDict.get(companiesNameStr)
#     placeStr=companyDataDict.get("Office")
#     rating=companyDataDict.get("Rating")

#     print("The Office Name is: ",companiesNameStr)
#     print("The Place Name is: ",placeStr)
#     print("The Rating is: ",rating)


# getMyProfs=kmc.get("professor")
# for val in getMyProfs:
#     print(val)

# getmyclub = kmc.get("clubs")
# for val in getmyclub:
#     print(val)    


# getmystudents = kmc.get("students")



# for  myStudentDict in getmystudents:
#     studentname=myStudentDict.get("name")
#     print(studentname)



kmc1={
    "list1":[3,45,23,76],
    "list2":[21,66,21,90],
    "list3":[43,12,43]
}
# Give me a list having sum of list1,list2,list3
# [147,198,98]

# sum=0
# sum1=0
# sum2=0
# listArr = kmc1.get("list1")
# for val in listArr:
#     sum=sum+val
    
# listArr = kmc1.get("list2")
# for val in listArr:
#     sum1=sum1+val

# listArr = kmc1.get("list3")
# for val in listArr:
#     sum2=sum2+val

# print([sum,sum1,sum2])


ans=[]
getKeysTup=kmc1.keys()
for key in getKeysTup:
    listArr = kmc1.get(key)
    sum=0
    for val in listArr:
        sum=sum+val
    ans.append(sum)

print(ans)


