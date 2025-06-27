# <!-- I'll help you by extracting just the questions and their expected outputs from the text file. Here's the cleaned-up version: -->

# <!-- ### String Basics
# 1. *Reverse a String*  
#    Write a Python program to reverse a string using slicing.  
#    Input: "hello"  
#    <!-- Output: "olleh"
#  <!-- str = "hello" -->

# str = "hello"
# print(str[len(str)-1::-1])

# strnew  = ""
# for index in range(len(str)-1,-1,-1):
#     strnew = strnew+str[index]
# print(strnew)



# <!-- 2. *Check Palindrome*  
#    Write a function to check if a string is a palindrome.  
#    Input: "radar"   -->
#    <!-- Output: True

# input = "radar"
# revString=input[len(input)-1::-1]
# if input == revString:
#     print("palindrome")
# else:
#     print("no , its not palindrome")

# 3. *Count Vowels and Consonants*  
#    Write a program to count the number of vowels and consonants in a string.  
#    Input: "Python"  
#    Output:  
#    Vowels: 1  
#    Consonants: 5

# str = "python"
# vowels = 0
# consonants = 0


# for index in range(0,len(str)):
#     charval = str[index]
#     if(charval == 'a' or charval=='e' or charval=='i' or charval=='u' or charval == 'o'):
#         vowels = vowels+1
        
#     else: 
#         consonants= consonants+1
# for val in str:
#     if (val =='a' or val =='e' or val == 'i' or val == 'o' or val == 'u'):
#         vowels = vowels+1
#     else:
#         consonants= consonants+1    



# print(vowels)
# print(consonants)

# 4. *Substring Check*  
#    Write a program to check if one string is a substring of another.   -->
#    <!-- Input: "hello", "ell"  
#    Output: True --> 



# input = "hello"
# strFind="ell"
# if(input.find(strFind)):
#     print(" present")
# else:
#     print(" not present")





# <!-- 5. *String Length*   --> 
#    <!-- Write a program to find the length of a string without using the len() function.
#    Input: "string length"
#    Output: 13


# strNew1 = "string length"
# count = 0
# for val in strNew1:
#     count = count+1
# print(count)


# ### String Slicing
# 6. *Extract First and Last Characters*  
#    Write a program to extract the first and last characters of a string.  
#    Input: "hello"  
#    Output: "ho"
strNew = "hello"
print(strNew[::len(strNew)-1])


strnew = "hello"
strnew1 =""
for index in range(0,len(strnew)):
    charval = strnew[index]
    if(index == 0 or index == len(strnew)-1):
          strnew1 = strnew1+charval
          print(strnew1)

    
    


# 7. *Slice to Reverse Words*  
#    Write a program to reverse the words in a sentence.  
#    Input: "Hello World"  
#    Output: "World Hello"

# input = "hello world"    
# input1 = input.split(" ")
# print(input1)
# input1.reverse()

# ans=""
# input1=['world', 'hello']
# for val in input1:
#     ans=ans+val+ " "
# print(ans)







# 8. *Middle Character(s)*  
#    Write a program to find the middle character(s) of a string.  
#    - If the length of the string is odd, return the middle character.  
#    - If it is even, return the two middle characters.  
#    Input: "Python"  
#    Output: "th"


# input="python"
# size=len(input)
# index=int(size/2)
# if(size%2==0):
#     print(input[index],input[index-1])
    

#     # Print two char
# else:
#     print(input[index])
    # print 1 char


# # preeti-- 7/2=3.5 ->3
# # 0-s
# # 1-a
# # 2-r
# # 3-t
# # 4-h
# # 5-a
# # 6-k


# 2,3

# 0-p
# 1-y
# 2-t
# 3-h
# 4-o
# 5-n






# 9. *Alternate Characters*  
#    Write a program to print every alternate character of a string.  
#    Input: "abcdef"  
#    Output: "ace"


# str="abcdef"
# ans=""
# for i in range(0,len(str)):
#     if(i%2==0):
#         ans=ans+str[i]
# print(ans)


# str1 = str[0:len(str)-1:2]
# print(str1)




# 10. *Remove Specific Slice*  
#     Write a program to remove a slice from a string.  
#     Input: "abcdefgh", Remove slice: from index 2 to 5  
#     Output: "abgh"



# ### String Methods
# 11. *Count Occurrences*  
input = "abcdefgh"

for i in range(0,2):
    print(input[i])

for i in range(6,len(input)):
    print(input[i])


#     Write a program to count the number of occurrences of a substring in a string using a string method.  
#     Input: "banana", "na"  
#     Output: 2
# str = "banana"
# print(str.count("na"))

# 12. *Change Case*  
#     Write a program to convert a string to uppercase and lowercase.  
#     Input: "Python"  
#     Output:  
#     Uppercase: "PYTHON"  
#     Lowercase: "python"

# input  = "python"
# input1 = input.upper()
# print(input1)




# 13. *Remove Whitespaces*  
#     Write a program to remove all leading and trailing whitespaces from a string.  
#     Input: "   hello   "  
#     Output: "hello"


# str="   hello   "

# start=-1
# end=-1


# for index in range(0,len(str)):
#     if(str[index]!=" "):
#         start=index
#         break

# for index in range(len(str)-1,-1,-1):
#     if(str[index]!=" "):
#         end=index
#         break

# print(str[start:end+1:1])


# 14. *Replace Characters*  
#     Write a program to replace all occurrences of a character in a string with another character.  
#     Input: "hello", "l", "x"  
#     Output: "hexxo"
# input = "hello"
# input1  = input.replace("l" ,"x")
# print(input1)


# 15. *Find Index*  
#     Write a program to find the first occurrence of a substring in a string.  
#     Input: "hello world", "world"  
#     Output: 6


# str="hello world"
# print(str.find("world"))





# 16. *Split and Join*  
#     Write a program to split a sentence into words and then join them back with a hyphen (-).  
#     Input: "I dushman Python"  
#     Output: "I-dushman-Python"

# input  = "I dushman Python"
# input1 = input.split()

# print(input1)
# # list=['I', 'dushman', 'Python']

# ans=""
# for val in input1:
#     ans=ans+val+"-"

# print(ans[0:len(ans)-1])




# ### Mixed Challenges
# 17. *Anagram Check*  
#     Write a program to check if two strings are anagrams of each other.  
#     Input: "listen", "silent"  
#     Output: True


# else:
#     print("No")



# dict1={}
# dict2={}

# for val in str1:

#     if(dict1.get(val)):
#         dict1[val]=dict1[val]+1
#     else:
#         dict1[val]=1

# for val in str2:

#     if(dict2.get(val)):
#         dict2[val]=dict2[val]+1
#     else:
#         dict2[val]=1

# print(dict1)
# print(dict2)


# str1="listen"
# str2="silentttt"

# str1Sorted=sorted(str1)
# str2Sorted=sorted(str2)

# if(str1Sorted==str2Sorted):
#     print("Yes")
# # 



# 18. *Remove Duplicates*  
#     Write a program to remove duplicate characters from a string.  
#     Input: "programming"  
#     Output: "progamin"


# dic={}
# str="programming" 

# ans=""

# for val in str:
#     if(dic.get(val)):
#         print("Do nothing",val)
#     else:
#         ans=ans+val
#         dic[val]=1

# print(ans)



# 19. *Count Words*  
#     Write a program to count the number of words in a string.  
#     Input: "Python is awesome"  
#     Output: 3


# str="Python is awesome"

# strList=str.split()
# print(len(strList))



# 20. *Longest Word*  
#     Write a program to find the longest word in a sentence.  
#     Input: "I dushman programming"  
#     Output: "programming"



# str="I dushman programming kdhg"  
# strList=str.split()
# mx=-1
# ans=""


# for val in strList:
#     size=len(val)
#     if(size>mx):
#         mx=size
#         ans=val

# print(ans)




# # 21. *Sorting a string*  
# #     Write a program to sort the characters in a string.  
# #     Input: "djfnaarthjabefrt"  
# #     Output: "aaabdeffhjjnrtt" --> -


# str= "djfnaarthjabefrt"  
# arr=[]

# for val in str:
#     arr.append(val)

# print(arr)
# arr.sort()
# print(arr)
# strSorted=sorted(str)
# print(strSorted)


# ans=""


# for val in arr:
#     ans=ans+val

# print(ans)














