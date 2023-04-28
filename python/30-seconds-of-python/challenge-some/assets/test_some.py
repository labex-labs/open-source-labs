import unittest
import sys
sys.path.append("/home/labex/project")
from some import *

class TestSome(unittest.TestCase):
  
  def test_some(self):
    self.assertEqual(some([1,2,3]), True)
    self.assertEqual(some([0, False, None]), False)
    self.assertEqual(some([0, False, None], bool), False)
    self.assertEqual(some([1,2,3], lambda x: x > 2), True)
    self.assertEqual(some(['apple', 'banana', 'cherry'], lambda x: 'a' in x), True)
    self.assertEqual(some(['apple', 'banana', 'cherry'], lambda x: 'm' in x), False)

if __name__ == '__main__':
  unittest.main()