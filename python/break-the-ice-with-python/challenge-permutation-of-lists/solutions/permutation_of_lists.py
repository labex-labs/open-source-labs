from itertools import permutations


def permuation_generator(iterable):
    p = permutations(iterable)
    for i in p:
        print(i)


x = [1, 2, 3]
permuation_generator(x)
