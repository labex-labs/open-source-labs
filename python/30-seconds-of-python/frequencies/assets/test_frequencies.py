import unittest
from frequencies import *

class TestFrequencies(unittest.TestCase):
  
  def test_frequencies(self):
    self.assertEqual(frequencies([1,2,3,3,4,4,4]), {1:1, 2:1, 3:2, 4:3})
    self.assertEqual(frequencies(['a','b','c','c','c']), {'a':1, 'b':1, 'c':3})
    self.assertEqual(frequencies([]), {})
    self.assertEqual(frequencies([1,1,1,1]), {1:4})
    self.assertEqual(frequencies([1,'a',1,'a',1]), {1:3, 'a':2})

if __name__ == '__main__':
  unittest.main()