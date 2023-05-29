def sqr(x):
    return x * x


def use_of_map():
    squaredNumbers = list(map(sqr, range(1, 21)))
    print(squaredNumbers)


use_of_map()
