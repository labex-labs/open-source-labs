def for_each_right(itr, fn):
    for el in itr[::-1]:
        fn(el)
