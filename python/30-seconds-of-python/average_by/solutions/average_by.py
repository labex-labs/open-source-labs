def average_by(lst, fn = lambda x: x):
  return sum(map(fn, lst), 0.0) / len(lst)
