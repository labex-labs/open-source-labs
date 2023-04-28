import unittest
from values_only import *

class TestValuesOnly(unittest.TestCase):
  
  def test_values_only(self):
    flat_dict = {'a': 1, 'b': 2, 'c': 3}
    self.assertEqual(values_only(flat_dict), [1, 2, 3])
    
if __name__ == '__main__':
  unittest.main()