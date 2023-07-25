def remove_certain_numbers_from_list():
    orig_lst = [12, 24, 35, 70, 88, 120, 155]
    indices = [0, 2, 4, 6]

    new_list = [i for (j, i) in enumerate(orig_lst) if j not in indices]
    print(new_list)


remove_certain_numbers_from_list()
