# min
# max
# average
# sum
# length/count


# arrHelp=[2,4,1,5,6,9,7,1,3,4,2,5]

# minAns=10**10
# maxAns=-10**10
# sum=0
# count=0

# for val in arrHelp:

#     # To find Sum
#     sum=sum+val

#     # To find count
#     count=count+1

#     # To find min
#     if(val<minAns):.ln v
#         minAns=val

#     # To find max
#     if(val>maxAns):
#         maxAns=val




# print("The minimum value is: ",minAns)
# print("The maximum value is: ",maxAns)
# print("The sum is: ",sum)
# print("The count is: ",count)
# print("Average is: ",sum/count)



# pookie pyhton assignment
strnump = "hello"
print(strnump[len(strnump)-1::-1])





# QUES 2
strnew1 = "madam"

if strnew1 == strnew1[len(strnew1)-1::-1]:
    print("Yes it is a palindrome")
else:
    print("No it is no")
strnew2 = "heello"
if strnew2 == strnew2[len(strnew1)-1::-1]:
    print("Yes it is a palindrome")
else:
    print("No it is no")








# # QUES 3
val = "programming"
 
countVowel=0
# vowelIndex=[]

for index in range(0,len(val)):
    charVal=val[index]
    if(charVal=='a' or charVal=='e' or charVal=='i' or charVal=='o' or charVal=='u'):
        countVowel=countVowel+1

print("Number of Vowels: ",countVowel)        
 







# QUES 4
strchar = "banana"
strval = " "
for val in strchar:
    if(val!= "a"):
        strval = strval + val
print(strval)







# ques -5
input= "apple"   

ans={}

for val in input:
    if ans.get(val):
        # Key Exist
        ans[val]=ans[val]+1
    else:
        # Key does not exist
        ans[val]=1

print(ans)


# # ques - 6
# 10Convert a string to title case (capitalize first letter of each word)
# Write a Python program to convert a string to title case.
# Example:
# Input: "hello world"
# Output: "Hello World"




input = "hello world"
arr=input.split()


ans=""
for val in arr:
    newWord=val.capitalize()
    ans=ans+newWord+" "
print(ans[0:len(ans)-1])






### Q7. Replace all spaces in a string with hyphens ("-")
# Example:
# Input: "hello world python"
# Output: "hello-world-python"


newarr = "hello world python"

input1 = newarr.replace(" ","-")

print(input1)






### Q8. Find the longest word in a sentence
# Write a Python program to find the longest word in a given sentence.
# Example:"The quick brown fox jumps over the lazy dog"
# Input: 
# 
newarr1 = "the quick brown fox jumps over the lazy dog"
newarr = newarr1.split(" ")
mx = -1
ans  = ""
for val in newarr:
    wordlen = len(val)
    if(wordlen>mx):
        mx = wordlen
        ans = val
       
print(ans)        








### Q9. Check if a string contains only digits
# Write a program that checks if a string consists only of numeric characters.
# Example:
# Input: "12345"
# Output: True
# Input: "123a5"
# Output: False

newarr = "12345"
if(newarr.isnumeric()):
    print("Yes it contains only Numbers")
else:
    print("No it contains only Numbers")




    



### Q10. Count occurrences of a specific word in a string
# Write a program that counts how many times a word appears in a given sentence.
# Example:
# Output: 3
# Input: "apple banana apple orange apple", word = "apple"

newarr = "apple banana apple orange apple"
print(newarr.count("apple"))







# 3. String Slicing
### Q11. Extract the first and last character of a string
# Example:
# Input: "Python"
# Output: "P", "n"
newarr = "python"
# newarr1 = newarr[0:len(newarr):5]
# print(newarr1)
ans = ""
for index in range(0,len(newarr)):
    if (index == 0 or index ==len(newarr)-1):
        ans = ans+newarr[index]
print(ans)      






### Q12. Extract all even indexed characters from a string
# Example:
# Input: "Python"
# Output: "Pto"

strinput = "python"
ans = ""
for index in range(0,len(strinput)):
    if (index%2==0): 
        ans = ans+strinput[index]
print(ans)        

# print(strinput[::2])







### Q13. Remove the first and last character from a string
# Example:
# Input: "Python"
# Output: "ytho"

strinput = "python"
ans = ""
for index in range(0,len(strinput)):
    if (index != 0 and index!= len(strinput)-1):
        ans = ans+strinput[index]
print(ans)      
# strinput1 = strinput[1:len(strinput)-1]
# print(strinput1)






# ### Q14. Extract a substring from a given string
# Example:
# Input: "HelloWorld", start=1, end=5
# Output: "ello"
# ---
strinput = "helloworld"
ans = ""
for index in range(0,len(strinput)):
    if (index > 0 and index<5):
        ans = ans+strinput[index]
print(ans)    







# 15. Find the maximum and minimum number in a list
# Example:
# Input: [10, 20, 5, 8, 30]
# Output: Max: 30, Min: 5
newarr = [10,20,5,8,30]
# newarr1 = sorted(newarr)
# print(newarr1)
maxnum = max(newarr)
min_num = min(newarr)
print(maxnum)
print(min_num)






### Q16. Remove duplicates from a list
# Example:
# Input: [1, 2, 3, 1, 2, 4, 5]
# Output: [1, 2, 3, 4, 5]

listArr=[1, 2, 3, 1, 2, 4, 5]
obj={}
for val in listArr:
    obj[val]=True

ans=[]

for key in obj.keys():
    ans.append(key)
print(ans)


# By Set

mySet=set()

for val in listArr:
    mySet.add(val)

ans=[]

for val in mySet:
    ans.append(val)
print(ans)






### Q17. Count occurrences of an element in a list
# Example:
# Input: [1, 2, 2, 3, 4, 4, 4, 5], element = 4
# Output: 3
newarr = [1, 2, 2, 3, 4, 4, 4, 5]
newarr1 = newarr.count(4)
print(newarr1)

count = 0
for val in newarr:
    if val == 4:
        count = count +1
print(count)





### Q18. Find the sum of all elements in a tuple
# Example:
# Input: (1, 2, 3, 4, 5)
# Output: 15
newarr = (1, 2, 3, 4, 5)
sum = 0
for val in newarr:
    sum = sum +val
print(sum)








### Q19. Convert a list to a tuple
# Example:
# Input: [1, 2, 3]
# Output: (1, 2, 3)
# newarr =  [1, 2, 3]

listArr=[1,2,3]
tupArr=tuple(listArr)

print(tupArr)






## 5. Dictionary
### Q20. Merge two dictionaries
# Example
# Input: dict1 = {'a': 1, 'b': 2}, dict2 = {'c': 3, 'd': 4}
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

for key in dict2.keys():
    dict1[key]=dict2[key]

print(dict1)







# ### Q21. Find the key with the maximum value in a dictionary
# # # output : b
newarr = {'a':10,'b':20,'c':15}

mx =-1
key_ans = None

for key, val in newarr.items():
    if val > mx:
        mx = val
        key_ans = key

print(key_ans)  






# Q22. Sort a dictionary by values
# Example:
# Input: {'a': 3, 'b': 1, 'c': 2}
# Output: {'b': 1, 'c': 2, 'a': 3}
newarr = {'a': 3, 'b': 1, 'd': 2,'c':5}


# Sort a dictioary by key
# Sort a dictionary by value

# By key

keyTup=newarr.keys()
sortedKeys=sorted(keyTup)

ans={}
for key in sortedKeys:
    ans[key]=newarr[key]

print("muskan",ans)



# By value
keyValTup=newarr.items()
# ((key1,val1),(key2,val2),(key3,val3),(key4,val4))
# keyValTup=((a,3),(b,1),(d,2),(c,5))

def getMyKey(childTup):

    # If we want to sort by key
    # return childTup[0]

    # If we want to sort by value
    return childTup[1]

keyValTupSorted=sorted(keyValTup,key=getMyKey)

ans={}

for valTup in keyValTupSorted:
    # ((a,3),(b,1),(d,2),(c,5))
    # key,val
    # valTup=(a,3)
    key=valTup[0]
    value=valTup[1]
    ans[key]=value

print("muskan",ans)


## 6. Sorting
### Q23. Sort a list of numbers in ascending order
# Example:
# Input: [4, 2, 9, 1, 5]
# Output: [1, 2, 4, 5, 9]
newarr =  [4, 2, 9, 1, 5]
newarr1 = sorted(newarr)
print(newarr1)





### Q24. Sort a list of dictionaries by a specific key by age
# Example:
# Input: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}]
# Output: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}]

newarr=  [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}]


def getMyKey(childDict):
    # {'name': 'Alice', 'age': 25}
    return childDict['age']


newarrSorted=sorted(newarr,key=getMyKey)

print("muskan",newarrSorted)


## 7. Sum, Averages, Count
### Q25. Find the sum of elements in a list
# Example:
# Input: [1, 2, 3, 4, 5]
# Output: 15
newarr =[1, 2, 3, 4, 5]
sum = 0
for val in newarr:
    sum = sum +val
print(sum)






### Q26. Find the average of numbers in a list
# Example:
# Input: [10, 20, 30, 40]
# Output: 25.0
newarr = [10, 20, 30, 40]
count = 0
sum = 0
for val in newarr:
        count = count +1
        sum = sum + val
average = sum/count
print(average)       






# 27. Count even and odd numbers in a list
# Example:
# Input: [1, 2, 3, 4, 5, 6]
# Output: Even: 3, Odd: 3
newarr = [1, 2, 3, 4, 5, 6]
counteven= 0
countodd = 0
for val in newarr:
    if val%2==0:
        counteven = counteven+1
    else:
        countodd = countodd+1
print(countodd)
print(counteven)







### Q28. Find the factorial of a number
# Example:
# Input: 5
# Output: 120


num=5
factorial=1


for numbers in range(1,num+1):
    factorial=factorial*numbers

print(factorial)





# ### Q29. Count words in a sentence
# Example:
# Input: "Python is awesome"
# Output: 3
newarr = "Python is awesome"
newarr1 =len(newarr.split())
print(newarr1)





# Q30. Convert a dictionary into two lists (keys and values)
# Example:
# Input: {'a': 1, 'b': 2, 'c': 3}
# Output: Keys: ['a', 'b', 'c'], Values: [1, 2, 3]

objDict={'a': 1, 'b': 2, 'c': 3}
keyTup=objDict.keys()
valTup=objDict.values()


keyList=[]
valList=[]
# ((key,val),(key,val),(key,val),(key,val))
for childTup in objDict.items():
    key=childTup[0]
    val=childTup[1]
    keyList.append(key)
    valList.append(val)
print(keyList)
print(valList)

