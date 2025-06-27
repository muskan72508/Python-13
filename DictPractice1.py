# Print the value of the Name key, add a new key Course with value "Python", update the value of Grade to "A+", and remove the Age key.


# mus = {
#     "Name" : "John Doe",
#     "Age" : "21",
#     "Grade": "A"
# }

# print(mus.get("Name"))
# mus["Course"]="Python"
# mus["Grade"]="A+"

# (mus.pop("Age"))
# print(mus)





# stat = {
#     "pen":5,
#     "notebook":10 , 
#     "eraser":3,
#     "pencil":7
# }

# # stat.values()
# listitems = stat.items()
# for valtup in listitems:
#     key = valtup[0]
#     val = valtup [1]
#     print("Key is",key)
#     print("Value is",val)
# print(listitems)





# d = {"apple": 10, "banana": 20, "cherry": 15}
# key_to_check = "banana"

# listitems = d.items()
# for valtup in listitems:
#     key = valtup[0]
#     val = valtup[1]

#     if key == "banana":
#         print(val)
#     else:
#         print(None)    


# if(d.get(key_to_check)):
#     print("Key exist")
# else:
#     print("Key does not exist")


# Task: Add a new subject "Biology" to the list of subjects and print all the subjects.

# student = {"name": "Alice", "subjects": ["Math", "Physics", "Chemistry"]}


# student["subjects"].append("Biology")

# print(student)





# Question 5: Iteration with Lists
# Task: Iterate over a dictionary and print each key along with its values.
# Sample Input:
# pythoninventory = {
#     "fruits": ["apple", "banana", "mango"],
#     "vegetables": ["carrot", "broccoli", "spinach"],
#     "dairy": ["milk", "cheese", "yogurt"]
# }



# listitems = pythoninventory.items()
# for valtup in listitems:
#     key = valtup[0]
#     valList = valtup[1]
#     print("key is: ",key)
#     for val in valList:
#         print(val)



# Question 6: List Manipulation in Dictionary
# Task: Create a dictionary where the keys are numbers (1 to 1000) and the values are lists containing squares of the respective key.

# ansDict={}
# # # ansDict[1]=1
# # # ansDict[2]=4
# # # ansDict[3]=9
# # # ansDict[4]=16

# for val in range(1,1001):
#     key=val
#     value=val*val
#     ansDict[key]=value
    # print(ansDict)



# Task: Write a program to access the city of a nested dictionary.
# Sample Input:
# mainDict = {
#     "name": "Emma",
#     "details": {
#         "age": 25, 
#         "address": {
#             "city": "New York",
#             "zip": "10001"
#         }
#     }
# }

# mainDict["name"]
# subdict = mainDict["details"]

# subdict["age"]
# subdict1 = subdict["address"]

# print(subdict1["city"])


# kmc={
#     "muskan":{
#         "city":"abc",
#         "age":10,
#         "details":{
#             "father":"asd",
#             "maothe":"klgn"
#         }
        
#     },
#     "muskan1":{
#         "city":"abc1",
#         "age":100,
#         "details":{
#             "father":"asddv",
#             "maothe":"klgnds"
#         }
#     },
#     "muskan2":{
#         "city":"abc2",
#         "age":1000,
#         "details":{
#             "father":"asdsfdsadg",
#             "maothe":"klgsdvfabn"
#         }
#     },
#     "muskan3":{
#         "city":"abc3",
#         "age":10000,
#         "details":{
#             "father":"asdsdavsd",
#             "maothe":"klgvsdbn"
#         }
#     }
# }

# subList=kmc.items()


# for val in subList:
#     key=val[0]
#     value=val[1]

#     # value is a dictionary
#     # subDict=value["details"] is also a dict

#     subDict=value["details"]
#     print(subDict["father"])




# noida={
#     "sector1":{
#         "abc":{
#             "F1":"Aditya",
#             "F2":"preeti"
#         },
#         "abc1":{
#             "F3":"Aditya1",
#             "F4":"preeti1"
#         },
#         "abc2":{
#             "F5":"Aditya2",
#             "F6":"preeti2"
#         }
#     },
#     "sector2":{
#         "abc11":{
#             "F11":"Aditya11",
#             "F21":"preeti11"
#         },
#         "abc12":{
#             "F31":"Aditya11",
#             "F41":"preeti11"
#         },
#         "abc22":{
#             "F51":"Aditya22",
#             "F61":"preeti22"
#         }
#     }
# }


# valList=noida.items()

# for val in valList:
#     key=val[0]
#     value=val[1]

#     val1List=value.items()

#     for val1 in val1List:
#         key1=val1[0]
#         value1=val1[1]

#         val2List=value1.items()

#         for val2 in val2List:
#             key2=val2[0]
#             value2=val2[1]
#             print(value2)

   
# company = {
#     "department": {"sales": 15, "tech": 25, "hr": 10},
#     "location": {"city": "San Francisco", "state": "CA"}
# }
# department = company["department"]
# location = company["location"]

# listitem = company.items()
# for valtup in listitem:
#     key = valtup[0]
#     value = valtup[1]
#     department["sales"]= 20

#     listitem1 = value.items()
#     for val1 in listitem1:
#         key = val1[0]
#         value1  = val1[1]
#         location["country"] = "USA"
#         print(val1)


# department = company.get("department")
# department["sales"] = 20

# location = company.get("location")
# location["country"] = "USA"

# print(department)
# print(location)




# students = {
#     "student1": {"name": "Tom", "grade": "A"},
#     "student2": {"name": "Jerry", "grade": "B"},
#     "student3": {"name": "Spike", "grade": "C"}
# }

# listitem = students.items()
# for valtup in listitem:
#     key = valtup[0]
#     value = valtup[1]

#     listitem1 = value.items()
#     for val1 in listitem1:
#         key = val1[0]
#         value1 = val1[1]
#         print("key is:",key)
#         print("value is :",value1)



# colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
          

# listitem = colors.items()
# # print(listitem)
# dicto = {}
# for valtup in listitem:
#     key = valtup[1]
#     value = valtup[0]
#     dicto[key]=value
# print(dicto)


# Merge two 

# string
# list
# dict


# str1="fmb"
# str2="kkfndg"

# str3=str1+str2

# a=[1,2,3,4]
# b=[5,6,7]

# c=a+b


# dict1={
#     "a":1,
#     "b":2,
#     "c":3
# }
# dict2={
#     "d":4,
#     "e":5,
#     "f":6,
#     "a":10
# }

# dict3={
#     **dict1,
#     **dict2
# }
# dict3=dict1 | dict2


# print(dict3)



#  Write a program to count the occurrences of each character in a string using a dictionary.
# input_string = "hello"


# ans={}


# for val in input_string:
#     if(ans.get(val)):
#         existingVal=ans[val]
#         ans[val]=existingVal+1
#     else:
#         ans[val]=1


# print(ans)

# ans1={}

# for index in range(0,len(input_string)):
#     key=index
#     value=input_string[index]
#     ans1[key]=value

# print(ans1)

# student = {"name": "John", "age": 20, "grade": "B"}
# key_to_update = "grade"
# new_value = "A"
# student[key_to_update]= new_value
# print(student)

# fruits = {"apple": 10, "banana": 20, "orange": 15}
# key_to_remove = "banana"
# fruits.pop(key_to_remove)
# print(fruits)


# numbers = [1, 2, 3, 4, 5]
# dicto = {}
# for val in numbers:
#     key = val
#     value = val*val
#     dicto[key]= value
# print(dicto)


# student = {"name": "Alice", "age": 22}
# key = "grade"
# if(student.get(key)):
#     print(value)
# else:
#     print("not found")


# sample_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# # count = 0
# listitem = sample_dict.items()
# # for val in listitem:
#     count = count+1
# print(len(listitem))


# prices = {"apple": 0.5, "banana": 0.25, "orange": 0.75, "pear": 0.60}
# listitems = prices.items()
# sum = 0
# for val in listitems:
#     key = val[0]
#     value = val[1]
#     sum = sum +value
# # print(sum)


# scores = {"John": 85, "Alice": 92, "Bob": 78, "Carol": 95,"preeti":12}
# listitems = scores.items()
# mx = -1
# for val in listitems:
#     key = val[0]
#     value = val[1]
#     mx = max(mx,value)

    # if(value>mx):
    #     mx=value
# print(mx)

# ages = {"Alice": 24, "Bob": 19, "Charlie": 30, "David": 17, "Eve": 22}
# Filter for people above 21
# listitems = ages.items()
# dicto = {}
# for val in listitems:
#     key = val[0]
#     value = val[1]
#     if(value>21):
#         dicto[key]=value

# print(dicto)



# users = ["Alice", "Bob", "Charlie","lmdsnglkfdgn"] 
# ages = [25, 30, 22] 
# cities = ["New York", "Los Angeles", "Chicago","lkfgndf","dklfgkfldh"] 


# {
#     'Alice': {'age': 25, 'city': 'New York'},
#     'Bob': {'age': 30, 'city': 'Los Angeles'},
#     'Charlie': {'age': 22, 'city': 'Chicago'}
# }


# size1=len(users)
# size2=len(ages)
# size3=len(cities)

# dictAns={}
# for index in range(0,min(size1,size2,size3)):

#     name=users[index]
#     age=ages[index]
#     city=cities[index]


#     key=name
#     value={'age': age, 'city': city}

#     dictAns[key]=value

# print(dictAns)

# sample_dict = {"a": 1, "b": 2, "c": 3}
# keys_to_check = ["a", "b", "d" ]

# listitems = sample_dict.items()
# for val in listitems:
#     # print(val)
#     key = val[0]
    # value = val[1]


    # a b c

    # count =0
    # for val1 in keys_to_check:
    #     if(val1==key):
    #         count=count+1
    # if(count==0):
    #     print("Not present")
    # else:
    #     print("Present")
        
    
    # if (keys_to_check.count(key)):
    #     print("present")
    # else:
    #     print("not found")




# unsorted_dict = {"banana": 3, "apple": 1, "orange": 2, "grapes": 4}
# arr = sorted(unsorted_dict)

# ans={}
# for key in arr:
#     value=unsorted_dict[key]
#     ans[key]=value

# print(ans)


scores = {"John": 85, "Alice": 92, "Bob": 78, "Carol": 95}

def getMyKey(arg):
    # print(arg)
    return scores[arg]

arr = sorted(scores,key=getMyKey,reverse=True)
print(arr)
ans={}
for key in arr:
    value=scores[key]
    ans[key]=value

print(ans)




