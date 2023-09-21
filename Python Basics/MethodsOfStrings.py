a = "My name is Bonika Adhikari"
print(a)
print(a.upper())
print(a.lower())
print(a.replace("My name is","I am"))

b = "Hi!"
print(b.rstrip("!"))

animal = "cat dog cow"
print(animal.split(" "))

c = "bonika"
print(c.capitalize())

heading = "about myself"
print(heading.center(50))
print(b.endswith("!"))
print(a.endswith("a"))
print(a.endswith("is",4, 10))
print(a.endswith("is", 2, 4))
print(a.startswith("My"))
#We can override variable in python
print(a.find("is"))
print(a.find("b")) #Find returns to -1 if it cannot find the string and gives starting number of index if the string is found
#If i want python to throw error if it doesn't fiknds the letter than i use index()
# print(a.index("copy"))

name = "This is my name"
print(name.isalnum())
#isalum prints the result true if the strings have alphanumeric character
name = "WelcomeToPython9"
print(name.isalnum())

r = "Good4"
print(r.isalpha())
r = "Good"
print(r.isalpha())
#isalpha prints the result true if the strings have alphabetical character

print(heading.islower())
#islower prints true if the variables contains lower character strings

a = "HELLOWORLD"
print(a.isupper())
print(heading.isupper())
#isupper prints true if the variables contains upper character strings

b = "Hello World\n"
print(b.isprintable()) #isprintable prints false if there is non printable character

str1 = "     "
print(str1.isspace()) #isspace prints true if there is white blank space. The space can be with tab or the sapce key

a = "Hello"
print(a.istitle()) #istitle prints true if the given string have title format(First letter Capital) 
print(a)
print(a.swapcase()) #swapcase swap the cases of the strings i.e. Lower will be in Upper and upper will be in lower

i = "cow is a useful animal"
print(i.title()) #Title capitalizes first letter of each word in an sentence
