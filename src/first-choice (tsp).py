from tsp import *

LIMITS = 100


def first_choice(p):
    current = random_init(p)
    values = evaluate(current, p)
    i = 0
    while i < LIMITS:
        successor = random_mutant(current, p)
        values_eval = evaluate(successor, p)
        if values_eval < values:
            current = successor
            values = values_eval
            i = 0
        else:
            i += 1
    return current, values


def random_mutant(current, p):
    while True:
        i, j = sorted([random.randrange(p[0]) for _ in range(2)])
        if i < j:
            current_copy = inversion(current, i, j)
            break
    return current_copy


def display_setting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")


if __name__ == "__main__":
    p = create_problem("./data/tsp30.txt")
    solution, minimum = first_choice(p)
    describe_problem(p)
    display_setting()
    display_result(solution, minimum)
