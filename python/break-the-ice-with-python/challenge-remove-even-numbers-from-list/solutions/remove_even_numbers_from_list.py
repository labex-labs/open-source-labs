def is_even(n):
    return n % 2 != 0


def remove_even_numbers_from_list():
    li = [5, 6, 77, 45, 22, 12, 24]
    lst = list(filter(is_even, li))
    print(lst)


remove_even_numbers_from_list()
