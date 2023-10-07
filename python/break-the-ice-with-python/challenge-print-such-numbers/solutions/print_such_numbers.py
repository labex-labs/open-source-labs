def print_such_numbers():
    for i in range(2000, 2201):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=",")


print_such_numbers()
