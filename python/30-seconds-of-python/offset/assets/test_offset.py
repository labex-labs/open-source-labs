import unittest
from offset import *

def offset(lst, offset):
    return lst[offset:] + lst[:offset]

class TestOffset(unittest.TestCase):
    
    def test_offset(self):
        self.assertEqual(offset([1,2,3,4,5], 2), [3,4,5,1,2])
        self.assertEqual(offset([1,2,3,4,5], -2), [4,5,1,2,3])
        self.assertEqual(offset(['a','b','c','d','e'], 3), ['d','e','a','b','c'])
        self.assertEqual(offset(['a','b','c','d','e'], -3), ['c','d','e','a','b'])
        self.assertEqual(offset([], 5), [])
        
if __name__ == '__main__':
    unittest.main()