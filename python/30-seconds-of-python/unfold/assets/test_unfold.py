import unittest
from unfold import *

def unfold(fn, seed):
  def fn_generator(val):
    while True:
      val = fn(val[1])
      if val == False: break
      yield val[0]
  return [i for i in fn_generator([None, seed])]

class TestUnfold(unittest.TestCase):
  
  def test_positive_case(self):
    self.assertEqual(unfold(lambda x: (x, x-1) if x > 0 else False, 5), [5, 4, 3, 2, 1])
  
  def test_negative_case(self):
    self.assertEqual(unfold(lambda x: (x, x-1) if x > 0 else False, -5), [])