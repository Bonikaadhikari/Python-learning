#This is my Day-12 Revision in basics of Python In PhiCoders
#Today I will go for methods of lists.

l = [11, 24, 3, 45, 2]
print(l)

#Sort 
#This method sorts the list in ascending order
l.sort()
print(l)

#This method sorts the list in descending order
l.sort(reverse=True)
print(l)

#Append (This method adds the value at the end of the list)
l.append(10)
print(l)

#Reverse (This method sorts the original list in descending order)
l.reverse()
print(l)

#Insert(This method inserts the specified value at the specified position)
l.insert(1, 10)

#Extend(This methods adds the given list with the another one)
m = [ 9, 4, 6 ]
l.extend(m)
print(l)

