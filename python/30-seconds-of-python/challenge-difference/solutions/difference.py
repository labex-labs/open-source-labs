def difference(a, b):
  _b = set(b)
  return [item for item in a if item not in _b]
