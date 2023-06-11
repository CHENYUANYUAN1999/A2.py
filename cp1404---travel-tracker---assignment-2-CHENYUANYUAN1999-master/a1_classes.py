"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from placecollection import PlaceCollection

import csv

FILENAME = "place.csv"
traveller = PlaceCollection


def main():
    print("Travel Tracker 1.0 - by Chen Yuanyuan")
    traveller.load_places("places.csv")
    show_menu()
    menu()
    print("Have a nice day :)")
    sort_csv_file()


def show_menu():
    print("Menu:\nL - List place\nR - Recommend random place"
          "\nA = Add new place\nM - Mark a place as visited\nQ - Quit")


def menu():
    user_input = input(">>> ").upper()
    while user_input != "Q":
        if user_input == "L":
            unvisited_place = show_list()
            if unvisited_place >0:
                print("{} places. You still want to visit {} places".format(unvisited_place,unvisited_place))
            else:
                print("No unvisited places.")
        elif user_input == "A":
            add_new_place()
        elif user_input == "R":
            recommend_place()
        elif user_input == "M":
            mark_visited_place()
        else:
            print("Invalid menu choice")
        traveller.save_file("places.csv")
        print("Thank you!")
        break


def show_list():
        count = 0
        unvisited_places = 0
        for row in traveller.place:
            if row[3] == "visited":
                count += 1
                print("{:>2}.{<{}} in {:>{}} priority {}".format(count,row[0],20,row[1],20,row[2]))
            else:
                # city_sign = " "
                count += 1
                print("{:>2}.{<{}} in {:>{}} priority {}".format(count, row[0], 20, row[1],20,row[2]))
                unvisited_places += 1
        return unvisited_places


def add_new_place():
    add_list = []
    while True:
        try:
            city = input("Name: ")
            break
        except TypeError:
            print("Input cannot be blank")

    while True:
        try:
            country = input("Country: ")
            break
        except TypeError:
            print("Input cannot be blank")

    while True:
        try:
            priority = input("Priority: ")
            break
        except TypeError:
            print("Input cannot be blank")
    add_list.append(city)
    add_list.append(country)
    add_list.append(priority)
    traveller.places.append(add_list)


def recommend_place():
    with open(FILENAME, "r") as csvfile:
        reader = csv.reader(csvfile)
        # Reverse the order since by default sorted method is in the increasing order
        # But here I want to recommend user has the highest priority place
        sorted_place = sorted([row for row in reader if row[3] == "n"], key=lambda row: int(row[2]), reverse=True)

        if len(sorted_place) > 0:
            print("Not sure where to visit next?")
            recommend_places = sorted_place[0]
            print(f"How about... {recommend_places[0]} in {recommend_places[1]}?")
        else:
            print("No places left to visit")


def mark_visited_place():
    show_list()
    with open(FILENAME, "r") as csvfile:
        reader = csv.reader(csvfile)
        csv_list = [row for row in reader]

    unvisited_cities = [row for row in csv_list if row[3] == "n"]
    if len(unvisited_cities) == 0:
        print("No unvisited place.")
        return

    while True:
        user_input = input("Enter the number of a place to mark as visited\n>>> ")
        if not user_input.isnumeric() or int(user_input) not in range(1, len(csv_list) + 1):
            print("Invalid input. Please enter a valid number.")
        elif csv_list[int(user_input) - 1][3] == "v":
            print(f"You have already visited {csv_list[int(user_input) - 1][0]}.")
        else:
            break

    city_index = int(user_input) - 1
    city_name = unvisited_cities[city_index][0]
    country_name = unvisited_cities[city_index][1]
    csv_list[csv_list.index(unvisited_cities[city_index])][3] = 'v'

    with open(FILENAME, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        sorted_list = sorted(csv_list, key=lambda row: ('n' if row[3] == 'n' else 'v', int(row[2])))
        writer.writerows(sorted_list)

    print(f"{city_name} in {country_name} visited")


def sort_csv_file():
    with open(FILENAME, "r") as csvfile:
        reader = csv.reader(csvfile)
        sorted_list = sorted(reader, key=lambda row: (row[3], int(row[2])))

    with open(FILENAME, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sorted_list)


main()
