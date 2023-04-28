def map_values(obj, fn):
  return dict((k, fn(v)) for k, v in obj.items())
