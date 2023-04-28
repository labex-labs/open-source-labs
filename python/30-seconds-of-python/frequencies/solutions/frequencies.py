from collections import defaultdict

def frequencies(lst):
  freq = defaultdict(int)
  for val in lst:
    freq[val] += 1
  return dict(freq)
