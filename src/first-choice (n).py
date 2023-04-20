from numeric import *

LIMITS = 100


def first_choice(p):
    current = random_init(p)
    values = evaluate(current, p)
    i = 0
    while i < LIMITS:
        successor = random_mutant(current, p)
        value_eval = evaluate(successor, p)
        if value_eval < values:
            current = successor
            values = value_eval
            i = 0
        else:
            i += 1
    return current, values


def random_mutant(current, p):
    i = random.randint(0, len(current) - 1)
    delta = [DELTA, -DELTA]
    d = random.choice(delta)
    return mutate(current, i, d, p)


def display_setting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", DELTA)


if __name__ == "__main__":
    p = create_problem("./data/Convex.txt")
    solution, minimum = first_choice(p)
    describe_problem(p)
    display_setting()
    display_result(solution, minimum)
