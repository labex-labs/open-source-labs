import unittest
import sys
sys.path.append("/home/labex/project")
from has_duplicates import *

def has_duplicates(lst):
    return len(lst) != len(set(lst))

class TestHasDuplicates(unittest.TestCase):
    def test_no_duplicates(self):
        self.assertFalse(has_duplicates([1, 2, 3, 4]))
    
    def test_duplicates(self):
        self.assertTrue(has_duplicates([1, 2, 3, 3]))
    
    def test_empty_list(self):
        self.assertFalse(has_duplicates([]))
    
    def test_single_item_list(self):
        self.assertFalse(has_duplicates([1]))
    
    def test_multiple_duplicates(self):
        self.assertTrue(has_duplicates([1, 2, 3, 3, 4, 4]))
    
    def test_string_list(self):
        self.assertTrue(has_duplicates(['a', 'b', 'c', 'c']))
    
    def test_mixed_type_list(self):
        self.assertTrue(has_duplicates([1, 'a', 2, 'b', 'c', 'c', 1]))
    
if __name__ == '__main__':
    unittest.main()