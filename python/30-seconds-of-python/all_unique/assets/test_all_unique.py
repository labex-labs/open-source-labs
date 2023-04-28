import unittest
import sys
sys.path.append("/home/labex/project")
from all_unique import *

class TestAllUnique(unittest.TestCase):
    
    def test_all_unique(self):
        self.assertTrue(all_unique([1, 2, 3, 4]))
        self.assertFalse(all_unique([1, 2, 3, 3]))
        self.assertTrue(all_unique([]))
        self.assertTrue(all_unique(["a", "b", "c"]))
        self.assertFalse(all_unique(["a", "b", "c", "a"]))
        
if __name__ == '__main__':
    unittest.main()