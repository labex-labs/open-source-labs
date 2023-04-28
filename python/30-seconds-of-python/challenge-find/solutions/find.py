def find(lst, fn):
  return next(x for x in lst if fn(x))
