import unittest
import sys
sys.path.append("/home/labex/project")
from for_each import *


class TestForEach(unittest.TestCase):
  
  def test_for_each(self):
    lst = [1, 2, 3, 4, 5]
    result = []
    fn = lambda x: result.append(x*2)
    for_each(lst, fn)
    self.assertEqual(result, [2, 4, 6, 8, 10])

if __name__ == '__main__':
  unittest.main()