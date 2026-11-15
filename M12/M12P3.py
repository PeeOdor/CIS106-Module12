# Problem 3: load last names and scores from a file into parallel arrays,
# then display the students with the highest and lowest scores.

import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scores.txt")


def load_data(file_name):
    names = []
    scores = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                names.append(parts[0])
                scores.append(int(parts[1]))
    return names, scores


def display_names(names, scores):
    print("Names and scores:")
    print(f"  {'Last Name':<12}{'Score':>5}")
    for i in range(len(names)):
        print(f"  {names[i]:<12}{scores[i]:>5}")


def display_high_low(names, scores):
    high_var = 0
    high_index = 0
    low_var = 999
    low_index = 0
    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i
    print(f"Highest score: {names[high_index]} with {high_var}")
    print(f"Lowest score:  {names[low_index]} with {low_var}")


def main():
    names, scores = load_data(DATA_FILE)
    display_names(names, scores)
    print()
    display_high_low(names, scores)


main()