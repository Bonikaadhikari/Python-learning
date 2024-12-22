#This is my Day-16 of revision in basics of Python for PhiCoders. 
#Today i will Learn about Recursion.
#Recursion is the process of defining something in terms of itself.

def factorial(n):
    if(n==0 or n==1):
       return 1
    else:
        return n * factorial ( n- 1)
print(factorial(5))