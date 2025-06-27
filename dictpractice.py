# # student = {
# #         "name": "John Doe",
# #         "age": 21,
# #         "grade": "A"
# # }
# # print(student["grade"])
# # student["subject"]="math"
# # print(student)

# # fruits = {"apple": 10, "banana": 20, "orange": 15}

# # print(fruits.keys())
# # print(fruits.values())

# # for key in fruits.keys():
# #     print(key)
# #     print(fruits[key])
# # listArr = [2,4,5,6,7]
# # for val in listArr:
# #     print(val)
# # student = {"abc":"sar"}
# # student["abc"]: "mus",
# # print(student)


# # Check if the key "grapes" exists in the fruits dictionary. Print "Key exists" if true, otherwise print "Key does not exist".
# # fruits["grapes"]
# # print(fruits.get("grape"))

# #  Remove the "banana" key from the fruits dictionary and print the updated dictionary
# # if fruits.get("banana"):
# #     fruits.pop("banana")
# #     print(fruits)

# #  program to iterate through the fruits dictionary and print each key and its corresponding value in the format:
     
# #      apple: 10
# #      banana: 20
# #      orange: 15

# # for key in fruits.keys():
# #     print(key)
# # #     print(fruits[key])

# #  Write a program to count the occurrences of each character in a string using a dictionary. For example, given the string "hello", the output should be:
# #      python
# #      {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# # misStr="hello"
# # ans={}

# # for val in misStr:
# #     if(ans.get(val)):
# #         ans[val]=ans[val]+1
# #     else:
# #         ans[val]=1

# # print(ans)



# #  Given a dictionary:
# #      python
# # #      colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
     
# # #      Write code to create a new dictionary with keys and values swapped. For example:
# # #      python
# # #      {"#FF0000": "red", "#00FF00": "green", "#0000FF": "blue"}
     
# # colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
# # ans = {}
# # for keys in colors.keys():
#     val = colors[keys]
# #     ans[val]=keys
# # print(ans)

# # - Merge these two dictionaries and print the result:
# #      python
# # dict1 = {"a": 1, "b": 2}
# # dict2 = {"b": 3, "c": 4}
     
# # for key in dict2.keys():
# #     dict1[key]=dict2[key]

# # print(dict1)

# # - Sort the fruits dictionary by:
# #       - Keys in ascending order.
# #       - Values in descending order.



# # 1-Sorting a dictionary by key and by value
# # fruits = {"apple": 10, "banana": 20,"zebra":100, "orange": 15}


# # Sort by key
# # ans={}

# # sortedKeys=sorted(fruits.keys())
# # for key in sortedKeys:
# #     ans[key]=fruits[key]

# # print(ans)


# # Sort By Value


# # for key,value in fruits.items():
# #     print(key)



# # sortedValue=sorted(fruits.items(), key=Value)




# # # Sort by value
# # sorted_by_values = {key: value for key, value in sorted(fruits.items(), key=lambda item: item[1])}


# # print(sorted_by_values)


# # 2- Sorting a list of dictionary based on some key

# # [
# #     {
# #         "name":"Muskan",
# #         "age":22,
# #         "phone":"8735"
# #     },
# #     {
# #         "name":"mansi",
# #         "age":23,
# #         "phone":'8375'
# #     }
# # ]



# #  a dictionary to store the details of three students, where each student is represented as a nested dictionary containing their name, age, and marks. For example:
# #       python
# #       students = {
# #           "student1": {"name": "Alice", "age": 22, "marks": 85},
# #           "student2": {"name": "Bob", "age": 20, "marks": 90},
# #           "student3": {"name": "Charlie", "age": 23, "marks": 78},
# #       }
      
# #       Write a program to:
# #       - Print the name and marks of each student.
# #       - Calculate the average marks.


# # students = {
# #           "student1": {"name": "Alice", "age": 22, "marks": 85},
# #           "student2": {"name": "Bob", "age": 20, "marks": 90},
# #           "student3": {"name": "Charlie", "age": 23, "marks": 78},
# #       }


# # sum=0
# # count=0


# # print(students.get("student1").get("name"))
# # print(students.get("student1").get("age"))

# # for key in students.keys():
# #     count=count+1
# #     newDict=students[key]

# #     sum=sum+int(newDict["marks"])

# #     print("Name is:",newDict["name"])
# #     print("Marks is:",newDict["marks"])
    

# # print("Average is: ",sum/count)


# # students = {
# #           "student1": [2,3,4],
# #           "student2": [5,6,1],
# #           "student3": [6,1,9],
# #       }

# # for key in students.keys():
# #     val=students.get(key)
# # #     print(val[0])

# # ques -1
# #       - Print the value of the Name key.
# #    - Add a new key Course with value "Python".
# #    - Update the value of Grade to "A+".
# #    - Remove the Age key.



# mus = {
#    "Name" : "John Doe",
#    "age" : "21",
#    "Grade" : "A"
# }
# print(mus.get("Name"))


# mus["course"] = "python"
# print(mus.keys())
# print(mus.items())


# mus["grade"] = "A+"
# print(mus)


# mus.pop("age")
# print(mus.keys())

# # ques - 2
# # 2. *Iteration*  
# #    Write a program that iterates over the following dictionary and prints each key-value pair:  
# #    python 
# items = {"pen": 5, "notebook": 10, "eraser": 3, "pencil": 7}

# for key in items.items():
#     print(key)
   
# # 3. *Key Check*  
# #    Write a function that checks if a given key exists in a dictionary. For example:  
# #    python
# d = {"apple": 10, "banana": 20, "cherry": 15}
# #    key_to_check = "banana"
# print(d.get("banana"))
   
#    ## *List Inside Dictionaries:*
# # 4. *Access and Modify*  
# #    Given the following dictionary:  
# #    python
student = {"name": "Alice", "subjects": ["Math", "Physics", "Chemistry"]}
   
# # #    - Add a new subject "Biology" to the list of subjects.
# # #    - Print all the subjects.

newstudentlst = student.get("subjects")
newstudentlst.append("biology")
student["subjects"]=newstudentlst 

print(student)


# # 5. *Iteration with Lists*  
# #    Write a program to iterate over the following dictionary and print each key along with its values:  
# #    python
inventory = {
       "fruits": ["apple", "banana", "mango"],
       "vegetables": ["carrot", "broccoli", "spinach"],
       "dairy": ["milk", "cheese", "yogurt"] }
# # print(inventory)
listArr = inventory.items()
   
for tup in listArr:
    print("key is: ",tup[0])
    print("Value is: ",tup[1])



# strHelp="Delhi"   #Immutable
# listHelp=[1,2,4]  #mutable
# tupHelp=(3,4,5)   #Immutable
# dictHelp={        #mutable
#     "aa":1,
#     "bb":1
# }

# # If we use any function of string or tuple
# # they will return a new string or tuple 
# # respectively
# receiveStr=strHelp.upper()
# print(receiveStr)
# print(strHelp.upper())

# # If we use any function of list or dict
# # they will not return a new list or dict
# # but will change original one

# # receiveList=listHelp.sort()

# listHelp.sort()
# listHelp.append("jfbn")
# print(listHelp)


# 6. *List Manipulation in Dictionary*  
#    Create a dictionary where the keys are numbers (1 to 1000) and the values are lists containing squares of the respective key. For example:  
#    python
#    {1: [1], 2: [4], 3: [9]}


obj={}

for num in range(1,1001):
    obj[num]=[num*num]

print(obj)




# 7. *Access Nested Data*  
#    Write a program to access the city of the following dictionary:  
#    python
person = {
       "name": "Emma",
       "details": {
                   "age": 25, 
                   "address": {
                    "city": "New York",
                    "zip": "10001"
                    }
                }
   }

newdict = person.get("details")
newdict2 = newdict.get("address")

print(newdict2.get("city"))



   

# 8. *Modify Nested Data*  
#    Given the following dictionary:  
#    python
company = {
       "department": {"sales": 15, "tech": 25, "hr": 10},
       "location": {"city": "San Francisco", "state": "CA"}
   }
newdict = company.get("department")
# newdict2 = newdict.get("sales")
newdict["sales"] = 20
print(newdict)
#    - Update the sales department count to 20.
#    - Add a new key country with value "USA" to the location dictionary.


newdict = company.get("location")
newdict["country"] = "USA"
print(newdict)
   


# 9. *Iterate Nested Dictionary*  
#    Write a program to iterate over the following nested dictionary and print each key-value pair:  
#    python
students = {
       "student1": {"name": "Tom", "grade": "A"},
       "student2": {"name": "Jerry", "grade": "B"},
       "student3": {"name": "Spike", "grade": "C"}
   }
   
newdict = students.items()
# keys()
# items()

# keys()   --->list  [key1,key2,key3,key4]
# items()  ---->list [(key1,val1),(key2,val2),(key3,val3)]

for tup in newdict:
    key=tup[0]
    valDict=tup[1]

    for tup1 in valDict.items():
        print("Key is: ",tup1[0])
        print("Value is: ",tup1[1])

    # 10. *Merge Dictionaries*  
    # Write a function that merges two dictionaries and returns the result. For example:  
    # python
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    Result: {"a": 1, "b": 2, "c": 3, "d": 4}
