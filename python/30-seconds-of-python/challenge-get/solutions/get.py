from functools import reduce
from operator import getitem

def get(d, selectors):
  return reduce(getitem, selectors, d)
