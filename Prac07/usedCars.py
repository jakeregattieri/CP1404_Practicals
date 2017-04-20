from Prac07.car import Car


def main():
    # car2 = Car("sports car", 200)
    # car2.drive(155)
    # print("fuel =", car2.fuel)
    # print("odo =", car2.odometer)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    limo.drive(115)
    print("fuel =", limo.fuel)
    print("odo =", limo.odometer)
    print(limo)


main()
