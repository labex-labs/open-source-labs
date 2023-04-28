import unittest
from none import *

def none(lst, fn = lambda x: x):
  return all(not fn(x) for x in lst)

class TestNone(unittest.TestCase):
  
  def test_none(self):
    self.assertTrue(none([], lambda x: x > 0))
    self.assertTrue(none([0, -1, -2], lambda x: x > 0))
    self.assertFalse(none([1, 2, 3], lambda x: x > 0))
    self.assertFalse(none([0, -1, 2], lambda x: x > 0))
    self.assertTrue(none(['', None, 0]))
    self.assertFalse(none(['', None, 0, 'hello']))
    
if __name__ == '__main__':
  unittest.main()