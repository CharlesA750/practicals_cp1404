from taxi import Taxi

def main():
    fare1 = Taxi("Prius 1", 100, 1.23)
    print("{} with {} units of fuel with price ${}/km".format(fare1.name, fare1.fuel, fare1.price_per_km))
    distance_traveled = float(input("How many kilometers did the taxi drive?"))
    fare1.drive(distance_traveled)
    print(fare1)
    fare2 = Taxi("Prius 1", 100, 1.23)
    print("{} with {} units of fuel with price ${}/km".format(fare2.name, fare2.fuel, fare2.price_per_km))
    distance_traveled = float(input("How many kilometers did the taxi drive?"))
    fare2.drive(distance_traveled)
    print(fare2)


main()


