def argfunction (*args, **kwargs):
    for items in args:
        print(items)
    
    for key, value in kwargs:
        print(f"{key} is the id of {value} ")

places = ("Urlabari", "Damak", "Kathmandu", "Itahari")
lists = {1: "Teacher", 2:"Instructor", 6:"Principal"}

argfunction (places, lists)