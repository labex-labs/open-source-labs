def remove_special_numbers_from_list():
    li = [12, 24, 35, 70, 88, 120, 155]
    li = [x for x in li if x % 35 != 0]
    print(li)


remove_special_numbers_from_list()
