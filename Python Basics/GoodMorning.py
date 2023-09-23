time = int(input("Please enter any time in the format of 24 hours"))
print("It's", time, "o'clock")

if (time >=1 and time <= 11):
    print("Good morning")
elif (time == 12):
    print("Good noon")
elif (time >12 and time <= 18):
    print("Good Afternoon")
elif (time >18 and time <=23):
    print("Good Evening")
else:
    print("Invalid time")