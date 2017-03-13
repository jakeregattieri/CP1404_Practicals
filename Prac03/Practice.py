INVALID_NAME = ""


user_name = input("what is your name: ".strip())
while user_name == INVALID_NAME:
    print("invalid name")
    user_name = input("what is your name: ".strip())
for i in range(user_name):