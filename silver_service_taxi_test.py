from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = input("C - Choose taxi\nD - Drive\nQ - Quit\n>>> ").upper()


def main():
    """..."""
    prius = Taxi("prius", 100)
    limo = SilverServiceTaxi("Limo", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(prius, "\n", limo, "\n", hummer)
    print(MENU)

    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    bill_to_date = 0

    while MENU != "Q":
        if MENU == "C":
            print("Taxis available:")
            for number, current_taxi in enumerate(taxis):
                print(f"{number} - {current_taxi}")

            choose_taxi = int(input("Choose current_taxi: "))

            current_taxi = taxis[choose_taxi]
            print(current_taxi)

            print(f"Bill to date: ${bill_to_date:.2f}")

        elif MENU == "D":
            drive_taxi = int(input("Drive how far? "))
            current_taxi.drive(drive_taxi)

            print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare()}")
            bill_to_date += current_taxi.get_fare()

        else:
            print("Invalid input error message")

        print(MENU)


main()
