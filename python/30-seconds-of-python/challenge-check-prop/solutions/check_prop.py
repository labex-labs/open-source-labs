def check_prop(fn, prop):
    return lambda obj: fn(obj[prop])
