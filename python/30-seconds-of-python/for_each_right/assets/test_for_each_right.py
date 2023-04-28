import unittest
import sys
sys.path.append("/home/labex/project")
from for_each_right import *

class TestForEachRight(unittest.TestCase):
  
  def test_for_each_right(self):
    lst = [1, 2, 3, 4, 5]
    result = []
    for_each_right(lst, lambda x: result.append(x))
    self.assertEqual(result, [5, 4, 3, 2, 1])
    
    lst = ["a", "b", "c"]
    result = []
    for_each_right(lst, lambda x: result.append(x.upper()))
    self.assertEqual(result, ["C", "B", "A"])