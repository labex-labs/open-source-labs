def remove_duplicate_numbers_from_list():
    li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    for i in li:
        if li.count(i) > 1:
            li.remove(i)
    print(li)


remove_duplicate_numbers_from_list()
