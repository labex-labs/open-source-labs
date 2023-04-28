import unittest
import sys
sys.path.append("/home/labex/project")
from sort_dict_by_value import *

class TestSortDictByValue(unittest.TestCase):
  
  def test_sort_dict_by_value(self):
    d = {'a': 3, 'b': 1, 'c': 2}
    expected_output = {'b': 1, 'c': 2, 'a': 3}
    self.assertEqual(sort_dict_by_value(d), expected_output)
    
    d = {'a': 3, 'b': 1, 'c': 2}
    expected_output = {'a': 3, 'c': 2, 'b': 1}
    self.assertEqual(sort_dict_by_value(d, reverse=True), expected_output)
    
    d = {'a': 3, 'b': 3, 'c': 2}
    expected_output = {'c': 2, 'a': 3, 'b': 3}
    self.assertEqual(sort_dict_by_value(d), expected_output)
    
if __name__ == '__main__':
  unittest.main()