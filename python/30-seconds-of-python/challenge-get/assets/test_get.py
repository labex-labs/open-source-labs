import unittest
import sys
sys.path.append("/home/labex/project")
from get import *


class TestGet(unittest.TestCase):
  
  def test_get(self):
    d = {'a': {'b': {'c': 1}}}
    self.assertEqual(get(d, ['a', 'b', 'c']), 1)
    
    d = {'a': {'b': {'c': [1, 2, 3]}}}
    self.assertEqual(get(d, ['a', 'b', 'c', 1]), 2)
    
    d = {'a': {'b': {'c': {'d': 'hello'}}}}
    self.assertEqual(get(d, ['a', 'b', 'c', 'd']), 'hello')
    
    d = {'a': [1, 2, 3]}
    self.assertEqual(get(d, ['a', 1]), 2)
    
    d = {'a': [1, {'b': 2}, 3]}
    self.assertEqual(get(d, ['a', 1, 'b']), 2)
    
if __name__ == '__main__':
  unittest.main()