# Works with both for and while loo

# Else is only executed if all the
# iterations are completed

for i in range(0,4):
    print(i)

else:
    print("Sorry no i")


for i in range(0,4):

    if(i==2):
        break
    print(i)

else:
    print("Sorry no i")