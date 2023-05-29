def even(x):
    return x % 2 == 0


def squer(x):
    return x * x


def use_of_map_and_filter():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # first filters number by even number and the apply map() on the resultant elements
    li = map(squer, filter(even, li))
    print(list(li))


use_of_map_and_filter()
