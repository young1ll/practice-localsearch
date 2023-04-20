from src import numeric


filename = "./data/Convex.txt"
exp = "(x1 - 2) ** 2 + 5 * (x2 - 5) ** 2 + 8 * (x3 + 8) ** 2 + 3 * (x4 + 1) ** 2 + 6 * (x5 - 7) ** 2"
result = numeric.create_problem(filename)


def test_create_problem():
    test_case1, test_case2 = result
    assert test_case1.strip() == exp
    assert (len(test_case2), len(test_case2[0])) == (3, 5)


def test_random_init():
    test_case = numeric.random_init(result)
    assert len(test_case) == 5
    assert all([isinstance(x, float) for x in test_case])


def test_evaluate():
    test_case = numeric.evaluate([1, 1, 1, 1, 1], result)
    assert test_case == 957
