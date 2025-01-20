

def factorial(num):
    if(num==0 or num==1):
        return num
    else:
        return (num*factorial(num-1))

print("Factorial of Number is: ",factorial(7))

def fibonacci(num):
    if(num==1):
        return 0
    elif(num==2):
        return 1
    elif(num==3):
        return 1
    return fibonacci(num-1)+fibonacci(num-2)

print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
    