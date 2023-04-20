import random


DELTA = 0.01
eval_count = 0


def create_problem(filename):
    f = open(filename, "r")
    expression = f.readline()

    var_names = []
    low = []
    up = []

    for line in f.readlines():
        _temp = line.split(",")
        var_names.append(_temp[0])
        low.append(float(_temp[1]))
        up.append(float(_temp[2]))
    domain = [var_names, low, up]
    return (expression, domain)


def random_init(p):
    domain = p[1]
    init = []
    for i in range(0, len(domain[0])):
        init.append(random.uniform(domain[1][i], domain[2][i]))
    return init


def evaluate(current, p):
    global eval_count
    eval_count += 1
    expr = p[0]
    var_names = p[1][0]
    for i in range(len(var_names)):
        assignment = var_names[i] + "=" + str(current[i])
        exec(assignment)
    return eval(expr)


def mutate(current, i, d, p):
    current_copy = current[:]
    domain = p[1]
    low = domain[1][i]
    up = domain[2][i]
    if low <= (current_copy[i] + d) <= up:
        current_copy[i] += d
    return current_copy


def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)


def describe_problem(p):
    print()
    print("Objective function:")
    print(p[0])
    print("Search space:")
    var_names = p[1][0]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(f"{var_names[i]} : {low[i], up[i]}")


def display_result(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))
    print(f"Minimum value: {minimum:,.3f}")
    print()
    print(f"Total number of evaluations: {eval_count:,}")


if __name__ == "__main__":
    p = create_problem("./data/Convex.txt")
    solution = random_init(p)
    minimum = evaluate(solution, p)
    describe_problem(p)
    display_result(solution, minimum)
