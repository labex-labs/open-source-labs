def includes_any(lst, values):
  for v in values:
    if v in lst:
      return True
  return False
