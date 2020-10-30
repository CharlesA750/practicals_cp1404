from unreliable_car import UnreliableCar


def main():
    car1 = UnreliableCar("Prius 1", 100, 50)
    car1.drive(40)
    print("{} has {} units of fuel and has driven {}".format(car1.name, car1.fuel, car1.odometer))


main()
