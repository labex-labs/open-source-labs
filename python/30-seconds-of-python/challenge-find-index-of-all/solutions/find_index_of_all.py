def find_index_of_all(lst, fn):
    return [i for i, x in enumerate(lst) if fn(x)]
