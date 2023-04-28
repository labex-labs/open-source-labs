import unittest
import sys
sys.path.append("/home/labex/project")
from find_key import *

class TestFindKey(unittest.TestCase):
    
    def test_find_key(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        dict2 = {'x': 'apple', 'y': 'banana', 'z': 'cherry'}
        
        self.assertEqual(find_key(dict1, 2), 'b')
        self.assertEqual(find_key(dict2, 'banana'), 'y')
        self.assertRaises(StopIteration, find_key, dict1, 4)
        
if __name__ == '__main__':
    unittest.main()