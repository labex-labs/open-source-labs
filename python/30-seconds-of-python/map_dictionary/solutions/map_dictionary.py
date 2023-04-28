def map_dictionary(itr, fn):
  return dict(zip(itr, map(fn, itr)))
