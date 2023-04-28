import unittest
import sys
sys.path.append("/home/labex/project")
from max_by import *


class TestMaxBy(unittest.TestCase):
  
  def test_max_by(self):
    lst = [1, 2, 3, 4, 5]
    fn = lambda x: x * 2
    self.assertEqual(max_by(lst, fn), 10)
    
    lst = ["apple", "banana", "cherry"]
    fn = lambda x: len(x)
    self.assertEqual(max_by(lst, fn), 6)
    
    lst = [{"name": "John", "age": 25}, {"name": "Jane", "age": 30}, {"name": "Bob", "age": 20}]
    fn = lambda x: x["age"]
    self.assertEqual(max_by(lst, fn), 30)
    
if __name__ == '__main__':
  unittest.main()