from functools import reduce

def compose(*fns):
  return reduce(lambda f, g: lambda *args: f(g(*args)), fns)
