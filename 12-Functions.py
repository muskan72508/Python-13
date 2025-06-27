
# def calculateGmean(a,b):
#     return (a*b)/(a+b)

# result=calculateGmean(9,8)

# print(result)


# def average(a=9,b=1):
#     print("Average",(a+b)/2)


# average(a=1)
# average(b=9,a=21)


# If we do not give any value it 
# become a required argument



# Giving * before argument treat it as a tuple
# Giving ** before argument teart it as a dictionary

def averageTuple(*numbers):
    sum=0

    for i in numbers:
        sum=sum+i
    print(sum/len(numbers))


averageTuple(5,6,7,1)

# def nameDict(**name):
#     print(name["fname"])


# nameDict(aname="ffv",bname="fgf",fname="ljn")