# Problem 1: store 10 last names in an array and display them
# forward and in reverse order.

last_names = ["Anderson", "Brooks", "Carter", "Diaz", "Evans",
              "Foster", "Garcia", "Harris", "Jackson", "Kim"]


def display_names(names):
    print("Names in order:")
    for i in range(len(names)):
        print(f"  {i + 1}. {names[i]}")


def display_names_reverse(names):
    print("Names in reverse order:")
    i = len(names) - 1
    while i >= 0:
        print(f"  {len(names) - i}. {names[i]}")
        i -= 1


def main():
    display_names(last_names)
    print()
    display_names_reverse(last_names)


main()