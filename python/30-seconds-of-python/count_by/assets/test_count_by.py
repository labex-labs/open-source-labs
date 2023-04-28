import unittest
from count_by import *

class TestCountBy(unittest.TestCase):
  
  def test_count_by_default(self):
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1}
    self.assertEqual(count_by(lst), expected)
    
  def test_count_by_fn(self):
    lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    expected = {5: 1, 6: 1, 7: 1, 8: 2}
    self.assertEqual(count_by(lst, len), expected)
    
  def test_count_by_empty_list(self):
    lst = []
    expected = {}
    self.assertEqual(count_by(lst), expected)
    
  def test_count_by_same_values(self):
    lst = [1, 1, 1, 1, 1, 1]
    expected = {1: 6}
    self.assertEqual(count_by(lst), expected)