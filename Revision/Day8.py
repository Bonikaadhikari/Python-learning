#This is my Day-8 of revision in basics of Python for PhiCoders. 
#Today i will go with break and continue Statement.

#Break and Continue Statement
#Break
for i in range(12):
    if(i==10):
        break
    print("5 X", i+1, "=", 5 * (i+1))

print("Loop breaked")

#Continue
for i in range(15):
    if(i==10):
        print("Continued") 
        continue
    print("6 X", i+1, "=", 6 * (i+1))

