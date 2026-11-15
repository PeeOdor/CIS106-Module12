# Problem 5: same as Problem 4, but displays "Name not found" when the
# last name is not in the list.

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
    found = False
    i = 0
    while i < len(names) and not found:
        if names[i].lower() == search_name.lower():
            print(f"  {names[i]} - batting average {averages[i]:.3f}")
            found = True
        i += 1
    if not found:
        print("  Name not found")


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