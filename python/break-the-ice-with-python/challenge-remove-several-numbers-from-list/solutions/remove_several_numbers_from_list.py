def remove_several_numbers_from_list():
    orig_list = [12, 24, 35, 70, 88, 120, 155]
    new_list = [i for (j, i) in enumerate(orig_list) if j not in range(1, 4)]
    print(new_list)


remove_several_numbers_from_list()
