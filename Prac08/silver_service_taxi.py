from Prac08.taxi import Taxi


class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = float(fanciness * self.price_per_km)
        self.price_per_km = self.fanciness
        self.flagfall = 4.50

    def __str__(self):
        return "{} plus a flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """ get the price for the taxi trip """
        return (self.price_per_km * self.current_fare_distance) + self.flagfall


def try_silver_service_taxi():
    new_taxi = SilverServiceTaxi("gary", 200, 4)
    print(new_taxi)
    new_taxi.drive(60)
    print(new_taxi)
    print("${:.2f}".format(new_taxi.get_fare()))

if __name__ == '__main__':
    try_silver_service_taxi()
