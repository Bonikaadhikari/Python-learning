#This is my Day-9 of revision in basics of Python for PhiCoders. 
#Today i will write a program to print factorial number by taking input from user using for loop.

n = int(input("Provide a number"))
fact = 1
if(n == 0 or n == 1):
    print("The factorial is 1")
elif(n<0):
    print("Sorry, Factorial doesn't exist for negative numbers")  
else:
    print("The factorial of", n, "is", fact)
    for i in range(1, n+1):
        fact = fact * i 


