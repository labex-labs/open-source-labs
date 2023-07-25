def remove_a_number_from_list():
    li = [12, 24, 35, 24, 88, 120, 155]
    li = [x for x in li if x != 24]
    print(li)


remove_a_number_from_list()
