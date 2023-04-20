import random
import math

eval_count = 0


def create_problem(filename):
    f = open(filename, "r")
    num_cities = int(f.readline())
    locations = []
    for line in f.readlines():
        locations.append(eval(line))
    f.close()
    table = calc_distance_table(num_cities, locations)
    return num_cities, locations, table


def calc_distance_table(num_cities, locations):
    table = []
    for i in range(num_cities):
        line = []
        for k in range(num_cities):
            distance = math.sqrt(
                (locations[i][0] - locations[k][0]) ** 2
                + (locations[i][1] - locations[k][1]) ** 2
            )
            line.append(distance)
        table.append(line)
    return table


def random_init(p):
    n = p[0]
    init = list(range(n))
    random.shuffle(init)
    return init


def evaluate(current, p):
    global eval_count
    eval_count += 1
    cost = 0
    num_cities, locations, table = p
    for i in range(num_cities):
        cost += table[current[i]][current[i - 1]]
    return cost


def inversion(current, i, j):
    current_copy = current[:]
    while i < j:
        current_copy[i], current_copy[j] = current_copy[j], current_copy[i]
        i += 1
        j -= 1
    return current_copy


def describe_problem(p):
    print()
    n = p[0]
    print(f"Number of cities: {n}")
    print(f"Locations:")
    locations = p[1]
    for i in range(n):
        print(f"{str(locations[i]):>12}", end="")
        if i % 5 == 4:
            print()


def display_result(solution, minimum):
    print()
    print("Best order of visits:")
    ten_per_row(solution)  # Print 10 cities per row
    print(f"Minimum tour cost: {round(minimum):,}")
    print()
    print(f"Total number of evaluations: {eval_count:,}")


def ten_per_row(solution):
    for i in range(len(solution)):
        print(f"{solution[i]:>5}", end="")
        if i % 10 == 9:
            print()


if __name__ == "__main__":
    p = create_problem("./data/tsp30.txt")
    solution = random_init(p)
    minimum = evaluate(solution, p)
    describe_problem(p)
    display_result(solution, minimum)
