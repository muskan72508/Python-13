# # If we don't pass any mode
# # 'r' mode is the default mode

# # Modes 

# # 'r'-- Read  (rt)
# # 'w'-- Write  (wt)
# # 'a'-- Append  (at)
# # 'c'  -- create (ct)

# # Apart from modes we also need
# # to specify how we want to handle the file

# # 't'  text 
# # 'b'  binary  (rb) (wb)  (ab)  (cb) [Images pdfs etc]


# # Read a text file


# f=open('csv/test.txt','r') 

# text=f.read()


# print(text)
# f.close()


# Writing to a file

# f=open('csv/test.txt','w')

# f.write("Hello preeti !")

# f.close()


# # Append in a file

# f=open('csv/test.txt','a')


# f.write("\nHello")

# f.close()



# func-[open,close,read,write]
# mode-'r','w','a'



# def readFileforMe(path):
#     fileRead=open(path,'r')
#     text=fileRead.read()
#     print(text)
#     fileRead.close()


# readFileforMe('csv/test.txt')



# fileWrite=open('csv/test.txt','w')
# fileAppend=open('csv/test.txt','a')

# fileWrite.write("Hello World \npreeti")
# fileAppend.write("\nHello World1")
# fileAppend.write("\nHello World2")
# fileAppend.write("\nHello World3")
# fileAppend.write("\nHello World4")


# fileWrite.close()
# fileAppend.close()


# readFileforMe('csv/test.txt')





# # readline() 
# # Reads single line from file
# # If we want to read multile lines use loop


file=open('csv/test.txt','r')



i=0
listDict=[]
colList=[]
# createListofDict
while True:
    line=file.readline()

    # Will give col name
    if i==0:
        colList=line.split(",")
        lastValue=colList[len(colList)-1]
        newLastValue=lastValue[0:len(lastValue)-1]
        colList[len(colList)-1]=newLastValue
        
    # This will give me data
    if i!=0:
        # A,North,450
        arr=line.split(',')
        print(arr)
        if(len(arr)==3):
            product=arr[0]
            region=arr[1]
            sales=arr[2]


            if(sales[len(sales)-1]=="\n"):
                newSales=int(sales[0:len(sales)-1])
            else:
                newSales=int(sales)

           

            if(region and product and sales):
                dictHelp={}
                dictHelp[colList[0]]=product
                dictHelp[colList[1]]=region
                dictHelp[colList[2]]=newSales

            listDict.append(dictHelp)
            
       
    i=i+1
    if not line:
        break


print(listDict)

# Calculate the total revenue across all regions and products.

sum=0
for valDict in listDict:
    saleValue=valDict["Sales"]
    sum=sum+saleValue

print(sum)



# i=0
# while i<10:
#     print("preeti")
#     i=i+1

# for i in range(0,10):
#     print("preeti")


# print(line)

# file.close()

# # Print marks of 3 students in 3 subjects
# # 56,45,67
# # 12,34,63
# # 13,64,23
# # f=open('test.txt','r')

# # i=0
# # while True:
# #     i=i+1
# #     line=f.readline()
# #     if not line:
# #         break
# #     m1=line.split(',')[0]
# #     m2=line.split(',')[1]
# #     m3=line.split(',')[2]
# #     print(f"Marks of student {i} in M1 is {m1} in M2 is {m2} in M3 is {m3}")


# # writelins() 
# # Write single line from file

# # f=open('test.txt','w')

# # lines=['line1\n','line2\n','line3\n']
# # f.writelines(lines)

# # We can also use 

# # lines=['line1','line2','line3']
# # for line in lines:
# #     f.write(line+"\n")

# # f.close()



# # txt file
# # csv file


# # 'r'-- Read  (rt)
# # 'w'-- Write  (wt)
# # 'a'-- Append  (at)
# # 'c'  -- create (ct)

# # Apart from modes we also need
# # to specify how we want to handle the file

# # 't'  text 
# # 'b'  binary  (rb) (wb)  (ab)  (cb) [Images pdfs etc]

# file=open("test.txt",'r')


# # Read All data in one go
# # data=file.read()


# # If we want to read line line by line

# line=file.readline()

# while True:
#     line=file.readline()
#     if not line:
#         break
#     print(line)

# file.close()

# Write in a file

# file=open("test.txt",'w')

# file.write("Hello")

# file.close()


# Append in a file

# file=open("test.txt",'a')

# file.write("\nHello appending this data")

# file.close()
