def bifurcate_by(lst, fn):
    return [[x for x in lst if fn(x)], [x for x in lst if not fn(x)]]
