
from prac_09.taxi import Taxi
class SilverServiceTaxi(Taxi):
    flagfall = 4.50
    def __init__(self, name, fuel,fanciness = 0.0):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * self.fanciness
        self._odometer = self._odometer

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall+ (super().get_fare())

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent taxi."""
        super().drive(distance)
        return self.current_fare_distance

    def __str__(self):
        return f"{super().__str__()}, plus flagfall of ${self.flagfall}"
