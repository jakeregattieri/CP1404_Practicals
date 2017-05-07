from Prac08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        if float(randint(0, 100)) < self.reliability:
            super().drive(distance)


def run_tests():
    car1 = UnreliableCar("nissan", 100, 34)
    car1.drive(50)
    print(car1)
    print(car1.reliability)

if __name__ == '__main__':
    run_tests()
