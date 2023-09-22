a = int(input("Enter Your Age: "))
print("Your age is ", a)

# print(a == 15) #is euqal to
# print(a < 15) #is less than
# print(a > 15) #is greater than
# print(a != 15) #is not equal to
# print(a >= 15) #greater than and equal to


# if (a >= 18):
#     print("You can vote")
# else:
#     print("You cannot vote")

if (a >= 60):
    print("Your are Senior Citizen")
elif (a >= 20):
    print("You are Young")
elif (a >= 12):
    print("You are TeenAger")
else:
    print("You are a Child")

n = int(input("Enter a value of number"))
if(n > 0):
    print("The number is positive")
elif(n == 0):
    print("The number is Zero")
else:
    print("The number is zero")

num = 18
if (num < 0):
    print("Number is negative")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num >= 10):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero")





