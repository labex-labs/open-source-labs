import unittest
from initialize_2d_list import *

class TestInitialize2DList(unittest.TestCase):
  
  def test_all_none(self):
    result = initialize_2d_list(3, 4)
    expected = [[None, None, None], [None, None, None], [None, None, None], [None, None, None]]
    self.assertEqual(result, expected)
    
  def test_all_zero(self):
    result = initialize_2d_list(2, 2, 0)
    expected = [[0, 0], [0, 0]]
    self.assertEqual(result, expected)
    
  def test_all_empty_string(self):
    result = initialize_2d_list(1, 3, "")
    expected = [[""], [""], [""]]
    self.assertEqual(result, expected)
    
  def test_mixed_values(self):
    result = initialize_2d_list(2, 3, [1, 2])
    expected = [[[1, 2], [1, 2]], [[1, 2], [1, 2]], [[1, 2], [1, 2]]]
    self.assertEqual(result, expected)
    
if __name__ == '__main__':
  unittest.main()