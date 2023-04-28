import unittest
import sys
sys.path.append("/home/labex/project")
from key_of_min import *

def key_of_min(d):
  return min(d, key = d.get)

class TestKeyOfMin(unittest.TestCase):
  
  def test_key_of_min(self):
    self.assertEqual(key_of_min({'a': 1, 'b': 2, 'c': 3}), 'a')
    self.assertEqual(key_of_min({'x': 10, 'y': 5, 'z': 8}), 'y')
    self.assertEqual(key_of_min({'p': 0, 'q': -1, 'r': -5}), 'r')
    self.assertEqual(key_of_min({'m': 100, 'n': 100, 'o': 100}), 'm')

if __name__ == '__main__':
  unittest.main()