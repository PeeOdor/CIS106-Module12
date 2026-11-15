# Problem 2: parallel arrays of last names and exam scores.
# The name at each position goes with the score at the same position.

last_names = ["Anderson", "Brooks", "Carter", "Diaz", "Evans",
              "Foster", "Garcia", "Harris", "Jackson", "Kim"]
scores = [88, 92, 75, 67, 95, 81, 73, 59, 84, 90]


def display_names(names, exam_scores):
    print("Names and scores in order:")
    print(f"  {'Last Name':<12}{'Score':>5}")
    for i in range(len(names)):
        print(f"  {names[i]:<12}{exam_scores[i]:>5}")


def display_names_reverse(names, exam_scores):
    print("Names and scores in reverse order:")
    print(f"  {'Last Name':<12}{'Score':>5}")
    i = len(names) - 1
    while i >= 0:
        print(f"  {names[i]:<12}{exam_scores[i]:>5}")
        i -= 1


def main():
    display_names(last_names, scores)
    print()
    display_names_reverse(last_names, scores)


main()