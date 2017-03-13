SUM = 0
COUNT = 0


valid_input = False
while not valid_input:
    try:
        age = int(input("enter age:"))
        if age <= 0:
            print("invalid Age!")
        else:
            valid_input = True
    except ValueError:
        print("invalid Age!")
while age > 0:
    try:
        SUM += age
        COUNT += 1
        age = int(input("enter age:"))
    except ValueError:
        print("invalid Age!")
average_age = SUM / COUNT
print(average_age)