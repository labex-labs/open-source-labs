def includes_all(lst, values):
  for v in values:
    if v not in lst:
      return False
  return True
