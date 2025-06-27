import pandas as pd

# Loading the csv file

file = pd.read_csv("csv/sales.csv")

# Print first 2 rows 
print(file.head(2))



# Print last 2 rows
print(file.tail(2))


# Return a tuple of (rows,columns)
print(file.shape)


print(file.columns)


for col in file.columns:

    # To get all the keys
    print("Column name is",col)

    # Loop through all the keys to get each column item
    for item in file[col]:
        print(item)


print(file["Region"])


# Data Selection 

# obj={
#     "apple":[{
#         "apple":[1,4,3],
#         "bananna":[1,2,3],
#         "grapes":[1,2,3],
#         "oranges":[1,2,3],
#     },{
#         "apple":[1,2,3],
#         "bananna":[1,2,3],
#         "grapes":[1,2,3],
#         "oranges":[1,2,3],
#     },],

#     2:{
#         "apple":1,
#         "bananna":2,
#         "grapes":3,
#         "oranges":4
#     }
# }
# for i in obj["apple"]:
#     print(i)


# listDict=obj["apple"]

# for dictItem in listDict:
#     for itemTup in dictItem.items():
#         key=itemTup[0]
#         valueList=itemTup[1]
#         print("key is",key)
#         print("Value is",valueList)
#         sortedList=sorted(valueList)
#         for val in sortedList:
#             print(val)