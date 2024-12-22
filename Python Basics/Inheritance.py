class Workers:
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname
        

    def showDetails(self):
        print(f"The name of worker {self.id} is {self.name} {self.surname}.") 
class Employee(Workers):
    def showPost(self):
        print("The post is Manager")

w1 = Workers(210, "Ram", "Thapa")
w1.showDetails()

w2 = Employee(10, "Hari", "Bahadur")
w2.showDetails()
w2.showPost()