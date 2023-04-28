from math import ceil

def months_diff(start, end):
  return ceil((end - start).days / 30)
