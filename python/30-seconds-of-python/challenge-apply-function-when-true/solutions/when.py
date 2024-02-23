def when(predicate, when_true):
    return lambda x: when_true(x) if predicate(x) else x
