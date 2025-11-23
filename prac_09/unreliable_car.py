import random
from prac_09.car import Car
class UnreliableCar(Car):


    def __init__(self, name, fuel, reliability = 0.1):
        """Initialize a UnreliableCar object."""
        super().__init__(name,fuel)
        self.reliability = reliability

    def driven(self, distance):
        """Drive the car."""
        random_number = random.randint(0, 100)
        if random_number > self.reliability:
            super().drive(distance)
        else:
            super().drive(0)

    def __str__(self):
        return f"{super().__str__()}"




