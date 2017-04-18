from Prac07.guitar import Guitar
from Prac07.guitar_list import GuitarList


def main():
    # my_guitars = GuitarList()
    # run = True
    # while run:
    #     name = input("name:")
    #     if name == "":
    #         break
    #     year = input("year:")
    #     cost = input("cost:")
    #     my_guitars.add(Guitar(name, int(year), float(cost)))
    #     print("{} ({}): ${:.2f} added.".format(name, int(year), float(cost)))
    #     print(my_guitars)
    # print("These are my Guitars:")

    guitars = []
    run = True
    while run:
        name = input("name:")
        if name == "":
            break
        year = input("year:")
        cost = input("cost:")
        guitars.append(Guitar(name, int(year), float(cost)))
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Fender Stratocaster", 1964, 18480.65))
    for i, guitar in enumerate(guitars):
        vintage_string = guitar.is_vintage()
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))


main()
