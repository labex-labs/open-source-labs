import unittest
from drop import *

class TestDrop(unittest.TestCase):
    
    def test_drop_default(self):
        self.assertEqual(drop([1,2,3]), [2,3])
        
    def test_drop_custom(self):
        self.assertEqual(drop([1,2,3,4], 2), [3,4])
        
    def test_drop_empty(self):
        self.assertEqual(drop([]), [])
        
    def test_drop_single(self):
        self.assertEqual(drop([1]), [])
        
if __name__ == '__main__':
    unittest.main()