from functools import reduce


def compose_right(*fns):
    return reduce(lambda f, g: lambda *args: g(f(*args)), fns)
