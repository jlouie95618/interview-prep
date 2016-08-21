from random import randint, uniform


def random_int_list(size = 50, lower_bound = 0, upper_bound = 20, to_sort = False):
    print("random_int_list")
    if to_sort:
        return sorted([randint(lower_bound, upper_bound) for _ in range(size)])
    else:
        return [randint(lower_bound, upper_bound) for _ in range(size)]


def random_float_list(size = 50, lower_bound = 0, upper_bound = 20, to_sort = False, precision = 3):
    print("random_int_list")
    if to_sort:
        return sorted([round(uniform(lower_bound, upper_bound), precision) for _ in range(size)])
    else:
        return [round(uniform(lower_bound, upper_bound), precision) for _ in range(size)]


def random_int_matrix():
    pass