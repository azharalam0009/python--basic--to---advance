'''
factorial(5)=1
factorial(5)=2X1
factorial(5)=3X2X1
factorial(5)=4X3X2X1
factorial(5)=5X4X3X2X1

factorial(n)=nX(n-1)X....3X2X1

factorial(n)=n* factorial(n-1)
'''


def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n=int(input("Enter your number:"))
print(f"The factorial of this number is:{factorial(n)}")