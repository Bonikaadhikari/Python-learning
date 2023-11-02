#This is my second day of revision in basics of Python for PhiCoders. 
#Today i will go with conditional statements, operators, lists and dictonaries.

#conditional statements
a = int(input("Enter a number"))
print("The number is", a)

if(a>0):
    print("The number", a, "is positive")
elif(a<0):
    print("The number", a, "is negative")
else:
    print("The number", a, "is zero")

#Operators
x = 10
y = 7

ans1 = (x + y) 
print("Addition of", x, "and", y, "is", ans1)

ans2 = (x - y)
print("Subtraction of", x, "and", y, "is", ans2)

ans3 = (x * y)
print("Multiplication of", x, "and", y, "is", ans3)

ans4 = (x / y)
print("Division of", x, "and", y, "is", ans4)

ans5 = (x % y)
print("Modulus of", x, "and", y, "is", ans5)

#lists
list1 = [(2, 4, 3), ["Apple", "Banana", "Mango"]]
print(list1)


#dictonaries
dict1 = {"name":"Bonika", "Age":"21", "CanVote":"True"}
print(dict1)
