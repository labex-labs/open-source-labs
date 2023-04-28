def cast_list(val):
    return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]
