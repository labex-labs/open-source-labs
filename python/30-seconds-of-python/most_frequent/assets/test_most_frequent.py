import unittest
from most_frequent import *

def most_frequent(lst):
  return max(set(lst), key = lst.count)

class TestMostFrequent(unittest.TestCase):
  
  def test_most_frequent(self):
    self.assertEqual(most_frequent([1, 2, 3, 3, 4]), 3)
    self.assertEqual(most_frequent([1, 1, 2, 2, 2, 3]), 2)
    self.assertEqual(most_frequent(['a', 'b', 'b', 'c', 'c', 'c', 'c']), 'c')

if __name__ == '__main__':
  unittest.main()