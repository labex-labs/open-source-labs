def some(lst, fn = lambda x: x):
  return any(map(fn, lst))
