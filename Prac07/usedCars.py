from Prac07.car import Car


def main():
    car1 = Car("Limo", 180)
    car1.drive(115)
    print("fuel =", car1.fuel)
    print("odo =", car1.odometer)
    print(car1)


main()
