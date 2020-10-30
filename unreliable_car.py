from car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability=""):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):

        distance_driven = super().drive(distance)
        if self.reliability < random.randint(0, 100):
            distance_driven = 0
        return distance_driven



