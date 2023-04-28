def every(lst, fn = lambda x: x):
  return all(map(fn, lst))
