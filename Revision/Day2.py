#This is my second day of revision in basics of Python for PhiCoders. 
#Today i will go with conditional statements, operators and dictonaries.

# #conditional statements
# a = int(input("Enter a number"))
# print("The number is", a)

# if(a>0):
#     print("The number", a, "is positive")
# elif(a<0):
#     print("The number", a, "is negative")
# else:
#     print("The number", a, "is zero")

# #Operators
# x = 10
# y = 7

# ans1 = (x + y) 
# print("Addition of", x, "and", y, "is", ans1)

# ans2 = (x - y)
# print("Subtraction of", x, "and", y, "is", ans2)

# ans3 = (x * y)
# print("Multiplication of", x, "and", y, "is", ans3)

# ans4 = (x / y)
# print("Division of", x, "and", y, "is", ans4)

# ans5 = (x % y)
# print("Modulus of", x, "and", y, "is", ans5)


#dictonaries
dict = {"name":"Bonika", "Age":"21", "CanVote":"True"}
print(dict)
print(dict["name"])

dict1 = {
    1 :"Bonika",
    2 :"Bhawana",
    3 : "Pawan"
    }
print(dict1[3])
print(dict1.keys())
print(dict1.values())
print(dict1.get(6))

dic = {
    "cow": "domestic",
    "tiger": "wild",
    "fish": "aquatic",
    "snake": "reptile"
}
print(dic["snake"])

