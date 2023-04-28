import unittest
import sys
sys.path.append("/home/labex/project")
from all_equal import *

class TestAllEqual(unittest.TestCase):
    def test_all_equal(self):
        self.assertTrue(all_equal([1, 1, 1, 1]))
        self.assertTrue(all_equal([2, 2, 2, 2, 2, 2]))
        self.assertTrue(all_equal([3, 3, 3, 3, 3, 3, 3]))
        self.assertTrue(all_equal(["a", "a", "a", "a"]))
        self.assertFalse(all_equal([1, 2, 3, 4]))
        self.assertFalse(all_equal([1, 1, 2, 1, 1]))
        self.assertFalse(all_equal(["a", "b", "c", "d"]))
        self.assertFalse(all_equal([]))
        
if __name__ == '__main__':
    unittest.main()