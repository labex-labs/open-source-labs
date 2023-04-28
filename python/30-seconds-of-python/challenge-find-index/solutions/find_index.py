def find_index(lst, fn):
  return next(i for i, x in enumerate(lst) if fn(x))
