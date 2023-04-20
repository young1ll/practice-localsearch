from src import tsp


filename = "./data/tsp30.txt"
result = tsp.create_problem(filename)


def test_create_problem():
    test_case1, test_case2, test_case3 = result
    assert (test_case1, len(test_case2), len(test_case2[0])) == (30, 30, 2)
