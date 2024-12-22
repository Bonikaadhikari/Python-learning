#This is my Day-13 Revision in basics of Python In PhiCoders
#Today I will go for methods of sets.

#Union
color = {"Red", "Green", "Blue", "White"}
color2 = {"Pink", "Purple", "Green", "Blue"}
color3 = color.union(color2)
print(color3)

#Intersection
color3 = color.intersection(color2)
print(color3)

# #Intersection_update
# color.intersection_update(color2)
# print(color)

#Symmetric_difference
color.symmetric_difference(color2)
print(color)

#Symmetric_difference_update
color.symmetric_difference_update(color2)
print(color)

#Some buit-in methods of sets
#isdisjoint
countries = {"Nepal", "India", "China", "Japan"}
countries2 = {"America", "Russia", "Nepal", "China"}
countries3 = countries.isdisjoint(countries2)
print(countries3)

countries = {"Nepal", "India", "China", "Japan"}
countries2 = {"America", "Russia"}
countries3 = countries.isdisjoint(countries2)
print(countries3)

#issuperset
countries = {"Nepal", "India", "China", "Japan"}
countries2 = {"America", "Russia", "Nepal", "China"}
countries3 = countries.issuperset(countries2)
print(countries3)

#issubset
countries = {"Nepal", "India", "China", "Japan"}
countries2 = {"America", "Russia", "Nepal", "China"}
countries3 = countries.issubset(countries2)
print(countries3)

#Add
countries = {"Nepal", "India", "China", "Japan"}
countries.add("Poland")
print(countries)

#Remove(It throws an error So we prefer to use discard method)
# countries = {"Nepal", "India", "China", "Japan"}
# countries.remove()
# print(countries)

#Discard
countries = {"Nepal", "India", "China", "Japan"}
countries.discard("China")
print(countries)

#Pop(It pops outs the items of the sets)
countries = {"Nepal", "India", "China", "Japan"}
countries.pop()
print(countries)

#Clear
countries = {"Nepal", "India", "China", "Japan"}
countries.clear()
print(countries)