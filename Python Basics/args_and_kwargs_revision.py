print("Arguments")
def args_function(*args):
    print(args)
    print(type(args))
    for i in args:
        print(i)

args_function(1, "Bonika", False)

print("\nKeyword arguments")
def kwargs_function(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for item in kwargs.items():
        print(item)

kwargs_function(age = 3, Name = "Bonika", Boolean = False, Nothing = None)

    