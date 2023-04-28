from time import sleep

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
