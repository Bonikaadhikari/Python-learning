#This is my Day-14 Revision in basics of Python In PhiCoders
#Today I will go for methods of Tuples.
#Tuples element cannot be changed or modified. To change the elements of tuples, we have to convert it into lists. 
#Because tuples are immutable.

#Some methods of tuples.
#Count
animals = ("Cow", "dog", "cat")
result = animals.count("Cow")
print(type(animals))
print(result)

#Index
n = (1, 2, 4, 6, 3, 6)
result = n.index(4)
print(result)

#Length
animals = ("Cow", "dog", "cat")
result = len(animals)
print("The length of animal tuple is ", result)