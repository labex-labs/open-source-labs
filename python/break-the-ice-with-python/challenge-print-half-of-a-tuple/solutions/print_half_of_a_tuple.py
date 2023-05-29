def print_half_of_a_tuple():
    tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    for i in range(0, 5):
        print(tpl[i], end=" ")
    print()
    for i in range(5, 10):
        print(tpl[i], end=" ")


print_half_of_a_tuple()
