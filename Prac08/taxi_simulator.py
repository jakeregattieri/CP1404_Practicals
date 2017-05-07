from Prac08.taxi import Taxi
from Prac08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    current_taxi = None
    print()
    print(MENU)
    user_input = input(">>>").upper()
    while user_input != "Q":
        if user_input == "C":
            print("Taxis available")
            for count, taxi in enumerate(taxis):
                print("{} - {}".format(count, taxi))
            valid_input = False
            while not valid_input:
                try:
                    user_choice = int(input("Choose taxi: "))
                    if user_choice < 0 or user_choice > count:
                        print("invalid taxi number")
                    else:
                        valid_input = True
                except ValueError:
                    print("invalid choice")
            current_taxi = taxis[user_choice]
            print("Bill to date: ${:.2f}".format(float(bill_to_date)))
        elif user_input == "D":
            if current_taxi is not None:
                distance = int(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
                bill_to_date += current_taxi.get_fare()
                print("Bill to date: ${:.2f}".format(float(bill_to_date)))
            else:
                print("no car")
        else:
            print("Invalid menu choice")
        print(MENU)
        user_input = input(">>>").upper()
    print("Total trip cost you ${:.2f}".format(bill_to_date))
    "Taxis are now:"
    for count, taxi in enumerate(taxis):
        print("{} - {}".format(count, taxi))


if __name__ == '__main__':
    main()