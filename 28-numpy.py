import numpy as np


arr1=[1,2,3,4]
# sum = 0
# for i in range(0,len(arr1)):
#     val=arr1[i]
#     sum = sum+val
# print(sum)


# ->U can create list and can do multilple operatins

# numpyArr=np.array(arr1)

# sum=np.sum(numpyArr)

# print(sum)


normalList=[1,2,3,4]
numpyList=np.array(normalList)


# Statistics function provided By Numpy

# 1-Mean (Average) – np.mean()
print("Mean is: ",np.mean(numpyList))

# 2-Median – np.median()
print("Median is: ",np.median(numpyList))

# 3-Variance – np.var()
print("Variance is: ",np.var(numpyList))

# 4-Standard Deviation – np.std()
print("Standard Deviation is : ",np.std(numpyList))

# 4-Percentile – np.percentile()
print("Percentile is : ",np.percentile(numpyList,10))



# 5-Minimum & Maximum – np.min() & np.max()

print("Minimum is : ",np.min(numpyList))
print("Maximum is : ",np.max(numpyList))

# 6-Sum & Product – np.sum() & np.prod()

print("Sum is : ",np.sum(numpyList))
print("Product is : ",np.prod(numpyList))


# Operation provided By Numpy

arr1=[2,4,5,6]
arr2=[5,2,1,7]


arr1Numpy=np.array(arr1)
arr2Numpy=np.array(arr2)
arr3Numpy=arr1Numpy+arr2Numpy

print(arr3Numpy)

salary=[10,20,30]
bonus=[0.1,0.2,0.3]

salaryNumpy=np.array(salary)
bonusNumpy=np.array(bonus)
newSalaryNumpy=salaryNumpy+(bonusNumpy*salaryNumpy)



# To convert back to list

listArr=[1,2,34]

listArrNumpy=np.array(listArr)

backToList=listArrNumpy.tolist()



# Perform element-wise addition, subtraction, multiplication, and division on two NumPy arrays.

arr1  = [2,4,6,8,10]
arr2 = [3,6,9,7,5]

arr3 = np.array(arr1) + np.array(arr2)
print(arr3)


arr3 = np.array(arr2) - np.array(arr1)
print(arr3)

arr3 = np.array(arr1) * np.array(arr2)
print(arr3)

arr3 = np.array(arr1) /  np.array(arr2)
print(arr3)