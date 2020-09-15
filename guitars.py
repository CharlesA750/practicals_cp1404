from guitars_class import Guitars

def main():
    guitars = []
    print("My guitars!")
    name = input("What is your name? ")
    year = int(input("What year was the guitar made? "))
    cost = float(input("How much did the guitar cost? "))
    guitars.append(Guitars(name, year, cost))
    print("{} ({}) : {} added.".format(name, year, cost))

    print("Listed guitars:")
    for i in enumerate(guitars):
        vintage_str = ""
        if Guitars.is_vintage():
            vintage_str = "(Vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i+1, name, year, cost, vintage_str))


main()