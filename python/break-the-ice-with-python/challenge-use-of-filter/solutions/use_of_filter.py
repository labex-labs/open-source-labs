def even(x):
    return x % 2 == 0


def use_of_filter():
    evenNumbers = filter(even, range(1, 21))
    print(list(evenNumbers))


use_of_filter()
