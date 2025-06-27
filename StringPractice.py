# import math

# ### *String Basics*
# 1. *Reverse a String*  
#    Write a Python program to reverse a string using slicing.  
#    Input: "hello"  
#    Output: "olleh"


# strNew1 = "hello"
# # print(strNew1[4::-1])

# strNew=""
# for index in range(len(strNew1)-1,-1,-1):
#     strNew=strNew+strNew1[index]

# print("Reverse is: ",strNew)


 
# 2. *Check Palindrome*  
#    Write a function to check if a string is a palindrome.  
#    Input: "radar                                        x"  
#    Output: True

# strnew1 = "radar"
# if strnew1 == strnew1[len(strnew1)-1::-1]:
#     print("Yes it is a palindrome")
# else:
# #     print("No it is now")

# # 3. *Count Vowels and Consonants*  
# #    Write a program to count the number of vowels and consonants in a string.  
# #    Input: "Python"  
# #    Output:  
   
# #    Vowels: 1  
# #    Consonants: 5
# val = "pyhton"
# countVowel=0
# countConsotants=0
# vowelIndex=[]
# consonantsIndex=[]

# for index in range(0,len(val)):
#     charVal=val[index]
#     if(charVal=='a' or charVal=='e' or charVal=='i' or charVal=='o' or charVal=='u'):
#         countVowel=countVowel+1
#         vowelIndex.append(index)
#         print("Vowel")
#     else:
#         countConsotants=countConsotants+1
#         consonantsIndex.append(index)
#         print("Constants")

# countVowel=0
# countConsotants=0
# vowelIndex=[]
# consonantsIndex=[]
# musPu=0
# for charVal in val:
#     if(charVal=='a' or charVal=='e' or charVal=='i' or charVal=='o' or charVal=='u'):
#         countVowel=countVowel+1
#         vowelIndex.append(musPu)
#         # print("Vowel")
#     else:
#         countConsotants=countConsotants+1
#         consonantsIndex.append(musPu)
#         # print("Constants")


#     musPu=musPu+1

# print("Number of Vowels: ",countVowel,vowelIndex)
# print("Number of Consonants: ",countConsotants,consonantsIndex)

# a=val.count("a")
# e=val.count('e')
# i=val.count("i")
# o=val.count("o")
# u=val.count("u")


# print("Number of Vowels: ",a+e+i+o+u)
# print("Number of Consonants: ",len(val)-(a+e+i+o+u))



# 4. *Substring Check*  
#    Write a program to check if one string is a substring of another.  
#    Input: "hello", "ell"  
#    Output: True

# strNew1 = "hello"
# strFind="ell"

# if(strNew1.find(strFind)==-1):
#     print("not present")

# else:
#     print(" Present")








# 5. *String Length*  
#    Write a program to find the length of a string without using the len() function.
# strNew1 = "string length"
# count = 0
# for val in strNew1:
#     count = count+1
# print(count)



# ### *String Slicing*
# 6. *Extract First and Last Characters*  
#    Write a program to extract the first and last characters of a string.  
#    Input: "hello"  
# #    Output: "ho"
# strNew1 = "hello"
# print(strNew1[::len(strNew1)-1])

# 
# 7. *Slice to Reverse Words*  
#    Write a program to reverse the words in a sentence.  
#    Input: "Hello World"  
#    Output: "World Hello"

# strNew1 = "Hello World"
# listArr=strNew1.split(" ")
# listArr.reverse()
# finalStr=""
# for res in listArr:
#     finalStr=finalStr+res+" "
# print(finalStr)

# 8. *Middle Character(s)*  
#    Write a program to find the middle character(s) of a string.  
#    - If the length of the string is odd, return the middle character.  
#    - If it is even, return the two middle characters.  
#    Input: "Python"  
#    Output: "th"

# strNew1 = "python"



# muskan  ---> 6 chars  --> sk

# preeti --> 7 chars   --> t



# if(len(strNew1)%2==0):
#     index=int(len(strNew1)/2)
#     print(strNew1[index-1],strNew1[index])
# else:
#     index=len(strNew1)/2
#     print(strNew1[math.floor(index)])
    # math.floor it round off the number




# 9. *Alternate Characters*  
#    Write a program to print every alternate character of a string.  
#    Input: "abcdef"  
#    Output: "ace"


# strNew1="abcdef"
# # # print(strNew1[::2])

# muskuAns=""

# for index in range(0,len(strNew1)):
#     if(index%2==0):
#       muskuAns=muskuAns+strNew1[index]

# print(muskuAns)

# 10. *Remove Specific Slice*  
#     Write a program to remove a slice from a string.  
#     Input: "abcdefgh", Remove slice: from index 2 to 5  
#     Output: "abgh"

# strNew1="abcdefgh"
# strAns=""

# for index in range (0,len(strNew1)):
#     if(index<2 or index>5):
#         strAns=strAns+strNew1[index]

# print(strAns)




# ### *String Methods*
# 11. *Count Occurrences*  
#     Write a program to count the number of occurrences of a substring in a string using a string method.  
#     Input: "banana", "na"  
#     Output: 2

# strNew1="banana"
# finalAns=strNew1.count("na")
# print(finalAns)

# 12. *Change Case*  
#     Write a program to convert a string to uppercase and lowercase.  
#     Input: "Python"  
#     Output:  
    
#     Uppercase: "PYTHON"  
#     Lowercase: "python"


# strNew1="python"

# print(strNew1.upper())
# print(strNew1.lower())

# 13. *Remove Whitespaces*  
#     Write a program to remove all leading and trailing whitespaces from a string.  
#     Input: "   hello   "  
#     Output: "hello"



# strNew1="   hello   " 
# print(strNew1.replace(" ",""))


# strNew1="   hello hi   "  

# firstIndex=0
# lastIndex=len(strNew1)-1

# for index in range(0,len(strNew1)):
#     if(strNew1[index]!=" "):
#         firstIndex=index
#         break


# for index in range(len(strNew1)-1,-1):
#     if(strNew1[index]!=" "):
#         lastIndex=index
#         break

# ans=""

# for index in range(firstIndex,lastIndex):
#     ans=ans+strNew1[index]

# print(ans)

# 14. *Replace Characters*  
#     Write a program to replace all occurrences of a character in a string with another character.  
#     Input: "hello", "l", "x"  
#     Output: "hexxo"

# strNew1="hello"
# print(strNew1.replace("l","x"))

# 15. *Find Index*  
#     Write a program to find the first occurrence of a substring in a string.  
#     Input: "hello world", "world"  
#     Output: 6
# strNew1 = "hello world"
# print(strNew1.find("world"))



# 16. *Split and Join*  
#     Write a program to split a sentence into words and then join them back with a hyphen (-).  
#     Input: "I dushman Python"  
#     Output: "I-dushman-Python"

# strNew1 = "I dushman Python ;lsfdmbg fgn ldkg lkdgmlk lkdmflkd dlkgmdflk kldmlkd dlgkmdblk dflkmdlbk dlkfvdl dlkfmndsfl"
# newArr = strNew1.split(" ")
# ans = ""
# for index in range(0,len(newArr)):
#     if(index==len(newArr)-1):
#         ans = ans + newArr[index]
#     else:   
#         ans = ans + newArr[index] +"-"
# print(ans)

# ---

# ### *Mixed Challenges*
# 17. *Anagram Check*  
#     Write a program to check if two strings are anagrams of each other.  
#     Input: "listen", "silent"  
#     Output: True

# strNew1="listen"   
# strNew2="silent"

# arr1=[]
# arr2=[]

# for x in strNew1:
#     arr1.append(x)

# for y in strNew2:
#     arr2.append(y)

# arr1.sort()
# arr2.sort()

# strNew11=""
# strNew12=""
# for x in arr1:
#     strNew11=strNew11+x
# for y in arr2:
#     strNew12=strNew12+y

# if(arr1==arr2):
#     print("Yes")
# else:
#     print("No")

# if(strNew11==strNew12):
#     print("Yes")
# else:
#     print("No")



# 18. *Remove Duplicates*  
#     Write a program to remove duplicate characters from a string.  
#     Input: "programming"  
#     Output: "progamin"


# strNew1 = "programming"






# 19. *Count Words*  
#     Write a program to count the number of words in a string.  
#     Input: "Python is awesome"  
# #     Output: 3 

# strNew1="Python is awesome" 


# # newArr=strNew1.split(" ")
# # print(len(newArr))

# count=0
# for space in strNew1:
#     if(space==" "):
#         count=count+1
# print("Number of spaces are: ",count)
# print("Number of words are: ",count+1)


# 20. *Longest Word*  
#     Write a program to find the longest word in a sentence.  
#     Input: "I dushman programming"  
#     Output: "programming" 

# strNew1="I dushman programming"  
# strArr=strNew1.split(" ")


# mx=-1
# ans=""
# for words in strArr:
#     lenWord=len(words)
#     if(lenWord>mx):
#         mx=lenWord
#         ans=words

# print(ans)
#  These questions will help you practice string manipulation and strengthen your foundational skills in Python. Let me know if you'd like solutions or hints for any!


# 21- Sorting a string

# str11="djfnaarthjabefrt"

# ['d','j','n','a','a']
# ['a','a','d','j','n']


# listArr=[]

# for val in str11:
#     listArr.append(val)

# print(listArr)
# listArr.sort()

# ans=""

# for val in listArr:
#     ans=ans+val

# print(ans)


