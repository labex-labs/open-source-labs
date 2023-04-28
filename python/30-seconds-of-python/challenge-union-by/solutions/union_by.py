def union_by(a, b, fn):
    _a = set(map(fn, a))
    return list(set(a + [item for item in b if fn(item) not in _a]))
