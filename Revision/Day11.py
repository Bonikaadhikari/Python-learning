#This is my Day-11 of revision in basics of Python for PhiCoders. 
#Today i will Learn to print fibonacci Series using for loop.

n1 = 0
n2 = 1
sum = 0

for i in range(0, 20):
    print(sum, end = " ")
    n1 = n2
    n2 = sum
    sum = n1 + n2

#Fibonacci Series with user input and error handling
try:
    num = int(input("Enter a number"))
    n1 = 0
    n2 = 1
    sum = 0
    for i in range(0, num):
        print(sum, end = " ")
        n1 = n2
        n2 = sum
        sum = n1 + n2
except ValueError:
    print("Provide a valid number")


