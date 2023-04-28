def find_last(lst, fn):
    return next(x for x in lst[::-1] if fn(x))
