# # 1.Write a program to print numbers from 1 to 10 using a `for` loop.

# # 2.Write a program to calculate and print the sum of the first 10 natural numbers using a `for` loop.

# # 3.Write a program to print all even numbers between 1 and 20.

# # 4.Write a program to print numbers from 10 to 1 in reverse order using a `for` loop.

# # 5.Write a program to print the multiplication table of 5 using a `for` loop.
# # 5 * 1 = 5
# # 5 * 2 = 10
# # 5 * 3 = 15
# # 5 * 4 = 20

# # 6.Write a program to find the factorial of a number (e.g., 5!) using a `for` loop.

# # 7.Given a list `numbers = [1, 2, 3, 4, 5]`, write a program to find and print the sum of all elements in the list using a `for` loop.

# # 8.Write a program to count the number of vowels in a string (e.g., `"hello world"`) using a `for` loop.

# # 9.Write a program to find and print the largest number in a list (e.g., `[3, 6, 2, 8, 4]`) using a `for` loop.

# # 10.Write a program to print the following pattern using a `for` loop:  

# # *
# # **
# # ***
# # ****
# # *****

# # 11-Print sum of all numbers divisible by 10 between 1-1000

# Ques -1
# for val in  range(1,11):
#     print(val)


# Ques-2
# sum=0
# count=0
# for val in range(1,1001):

#     if val%2==0:
#         count=count+1
#     sum=sum+val
# print(sum)
# print(count)


# Ques-3

# for val in  range(1,21):
#    if (val%2==0):
#     print(val)

# ques -4 


# for val in range(20,1,-1):
#     print(val)

# ques -6



# prod=1
# for val in range(1,6):
#     print("prod: ",prod,"val: ",val)
#     prod=prod*val
#     print("prod: ",prod,"val: ",val)
# print(prod)

# ques -7

# numarr = ["1","2" ,"3", "4", "5"]
# sum = 0
# for val in numarr:
#   sum = sum+int(val)   
# print(sum)   

# numarr = [1,2,3,4,5]
# sum = 0
# for val in numarr:
#   sum = sum+val   
# print(sum)    

# ques -8
# num = "hello world"
# count = 0
# for val in num:
#     if (val == "a" or val=="e"or val== "i"or val=="o"or val=="u"):
#         count = count+1
# print(count) 



# num = "hello world"
# count = 0  # Initialize vowel count to 0

# # Loop through each character in the string
# for val in num:
#     if val in "aeiou":  # Check if the character is a vowel
#         count = count+1 # Increment the count if a vowel is found

# print("Total number of vowels:", count)

# ques -9

# numarr= [3, 6, 2, 8, 4]
# numarr.sort()
# print(numarr[len(numarr)-1])  


# mx=-1
# for i in numarr:
#     mx=max(mx,i)
# print(mx)





# ques - 11
# count = 0 
# # sum = 0
# for val in range(1,1001):
#     if (val%10 == 0):
#         count = count +1
#         # sum = sum + val

# print(count) 
# print(sum)   
  

# ques -5

# 5 * 1 = 5
# 5 * 2 = 10
# for val in range(1,11):
#     print(f"5 * {val} = {5*val}")


# Write a program to print the following pattern using a `for` loop:  

# *
# **
# ***
# ****
# *****



# # Nested Loops

# for i in range(1,6):
#     for j in range(0,i):
#         print(i,j)
#         print("*",end=" ")
#     print('\n')

# for i range (0,10):  
# for people in range(0,12):


# Aa Ab Ac   Ad    Ae
# 1  11 111  1111  11111
# 2  22 222  2222  22222
# 3  33 333  3333  33333 


# for val in range(1,6):
#     for j in range(0,i):
#         print("*",end =" ")
#         print('/n')



