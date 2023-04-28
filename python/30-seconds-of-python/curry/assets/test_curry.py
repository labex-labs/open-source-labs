import unittest
from curry import *
from functools import partial

def curry(fn, *args):
  return partial(fn, *args)

class TestCurry(unittest.TestCase):
  
  def test_curry(self):
    def add(a, b):
      return a + b
    curried_add = curry(add, 2)
    self.assertEqual(curried_add(3), 5)
    
if __name__ == '__main__':
  unittest.main()