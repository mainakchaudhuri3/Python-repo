a = int(input("Enter your first value: "))
b = int(input("Enter your second value: "))


def numoperation(a,b):
    if a * b <= 1000:
       return print(a * b)
    else :
       return print(a + b)

##### Driver Code ###########

numoperation(a,b)