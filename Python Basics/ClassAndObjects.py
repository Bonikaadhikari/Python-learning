class Student:
    name = "Bonika"
    age = 21
    address = "Urlabari"
a = Student()
print(a.name, a.address)

a.name= "Shrutee"
print(a.name)

class Staffs:
    name = "Ram"
    age = "30"
    post = "Teacher"
    salary = "35000"
    def info(self):
        print(f"{self.name} is a {self.post}. He is {self.age} years old. His monthly income is {self.salary}")

x = Staffs()
y = Staffs()
x.name = "Shyam"
x.age = 32

y.name = "Hari"
x.post = "Principal"

x.info()
y.info()