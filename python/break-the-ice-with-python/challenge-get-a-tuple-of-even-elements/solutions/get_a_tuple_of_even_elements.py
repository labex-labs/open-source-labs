def get_a_tuple_of_even_elements():
    tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    tpl1 = tuple(i for i in tpl if i % 2 == 0)
    print(tpl1)


get_a_tuple_of_even_elements()
