# Problem 4: load 10 player names and batting averages from a file into
# parallel arrays, display them, and search for a player by last name.

import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "players.txt")


def load_data(file_name):
    names = []
    averages = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                names.append(parts[0])
                averages.append(float(parts[1]))
    return names, averages


def display_players(names, averages):
    print("Players and batting averages:")
    print(f"  {'Last Name':<12}{'Average':>8}")
    for i in range(len(names)):
        print(f"  {names[i]:<12}{averages[i]:>8.3f}")


def search_player(names, averages, search_name):
    for i in range(len(names)):
        if names[i].lower() == search_name.lower():
            print(f"  {names[i]} - batting average {averages[i]:.3f}")


def main():
    names, averages = load_data(DATA_FILE)
    display_players(names, averages)
    print()
    search_name = input("Enter a last name to search (or 'quit' to stop): ").strip()
    while search_name.lower() != "quit":
        search_player(names, averages, search_name)
        search_name = input("Enter a last name to search (or 'quit' to stop): ").strip()
    print("Goodbye!")


main()