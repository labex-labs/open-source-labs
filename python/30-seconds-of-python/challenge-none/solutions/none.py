def none(lst, fn=lambda x: x):
    return all(not fn(x) for x in lst)
