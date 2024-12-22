#This is my Fourth day of revision in basics of Python for PhiCoders. 
#Today i will go for Functions.

#functions
def CalculateMean(a, b, c, d, n):
    mean = (a + b + c + d) / n
    print(mean)
a = 4
b = 7
c = 10
d = 8
n = 4
CalculateMean( a, b, c, d, n)
# mean = (a + b + c + d) / n
# print(mean)

w = 20
x = 4
y = 3
z = 8
n = 4
CalculateMean( w, x, y, z, n)
# mean = (w + x + y + z) / n
# print(mean)

def isPositive ( a):
    if(a>0):
        print("The number", a, "is positive")
    elif(a<0):
        print("The number", a, "is negative")
    else:
        print("The number", a, "is zero")

a = int(input("Enter a number"))
print("The number is", a)
isPositive(a)

x = int(input("Enter a number"))
print("The number is", x)
isPositive(x)