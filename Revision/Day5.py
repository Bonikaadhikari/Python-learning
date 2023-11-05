#This is my Fifth day of revision in basics of Python for PhiCoders. 
#Today i will go with Lists and Sets.


#lists
list1 = [(2, 4, 3), ["Apple", "Banana", "Mango"]]
print(list1)

colors = ["Red", "White", "Green", "Blue", "Black"]
print(colors)
print(type(colors))
print("Length of color list is", len(colors))
print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])
print(colors[4])
if "White" in colors:
    print("Yes")
else:
    print("No")

#Sets
s = { 2, 4, 5, 2, 9}
print(s)
#Set doesn't maintain order of data items.
name = {"Bonika", "Shreya", "Shrutee", "Sandip", "Shreya"}
print(name)
print(type(name))
