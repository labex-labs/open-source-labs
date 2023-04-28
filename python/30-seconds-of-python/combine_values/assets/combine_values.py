from collections import defaultdict

def combine_values(*dicts):
  res = defaultdict(list)
  for d in dicts:
    for key in d:
      res[key].append(d[key])
    pass