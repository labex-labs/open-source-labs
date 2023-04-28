import unittest
from includes_any import *

class TestIncludesAny(unittest.TestCase):
  
  def test_includes_any(self):
    self.assertEqual(includes_any([1,2,3], [2,4]), True)
    self.assertEqual(includes_any(['a','b','c'], ['d','e']), False)
    self.assertEqual(includes_any([], [1,2,3]), False)
    self.assertEqual(includes_any([1,2,3], []), False)
    self.assertEqual(includes_any([], []), False)

if __name__ == '__main__':
  unittest.main()