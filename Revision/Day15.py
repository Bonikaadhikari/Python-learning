#This is my Day-15 Revision in basics of Python In PhiCoders
#Today I will go for methods of Dictonaries and Raise a custom error.

#Update
dic = {1: "Bonika", 2: "Shrutee", 3: "Ram"}
dic2 = {10: "Sweta", 5: "Arjun"}
dic.update(dic2)
print(dic)

#Clear (Clears all the elements of dictonary)
dic = {1: "Bonika", 2: "Shrutee", 3: "Ram"}
dic.clear()
print(dic)

#Pop
dic = {1: "Bonika", 2: "Shrutee", 3: "Ram"}
dic.pop(1)
print(dic)

#Popitem(It pops out the last items)
dic = {1: "Bonika", 2: "Shrutee", 3: "Ram"}
dic.popitem()
print(dic)

#Del(It delets the items in the lists)
dic = {1: "Bonika", 2: "Shrutee", 3: "Ram"}
del dic[2]
print(dic)

#Get(get the value of the key item)
dic = {1: "Bonika", 2: "Shrutee", 3: "Ram"}
a = dic.get(2)
print(a)

#Custom Error
age = int(input("Enter a positive number"))
if(age<=0):
    raise ValueError("Please provide a positive number")
elif(age>=16):
    print("You can Vote")
else:
    print("You are Non-Voter")