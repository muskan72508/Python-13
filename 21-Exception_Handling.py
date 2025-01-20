
# Finally is even executed 
# even if we have returned a value 
# from try and except

def func():
    a=input()
    try:
        for i in range(1,a):
            print(i)
        return 1
    except Exception as err:
        print(err)
        return 0
    finally:
        print("I am always executed")


print(func())
print("End of Program")



# Raising Custom Error

a=int(input("Enter value between 5 and 9"))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")