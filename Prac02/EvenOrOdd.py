

def main():
    valid_input = False
    while not valid_input:
        try:
            age = int(input("age: "))
            if age < 0:
                print("not a valid age!")
            else:
                valid_input = True
        except ValueError:
            print("not a valid input")
    if get_even(age):
        print("even")
    else:
        print("odd")


def get_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

main()