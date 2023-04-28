from functools import partial

def curry(fn, *args):
  return partial(fn, *args)
