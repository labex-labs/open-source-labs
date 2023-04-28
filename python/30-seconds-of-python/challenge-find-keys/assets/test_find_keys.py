import unittest
import sys
sys.path.append("/home/labex/project")
from find_keys import *

class TestFindKeys(unittest.TestCase):
    
    def test_find_keys(self):
        dict1 = {'a': 1, 'b': 2, 'c': 1}
        dict2 = {'x': 'apple', 'y': 'banana', 'z': 'apple'}
        
        self.assertEqual(find_keys(dict1, 1), ['a', 'c'])
        self.assertEqual(find_keys(dict1, 2), ['b'])
        self.assertEqual(find_keys(dict2, 'apple'), ['x', 'z'])
        self.assertEqual(find_keys(dict2, 'banana'), ['y'])

if __name__ == '__main__':
    unittest.main()