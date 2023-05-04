def find_key(dict, val):
    return next(key for key, value in dict.items() if value == val)
