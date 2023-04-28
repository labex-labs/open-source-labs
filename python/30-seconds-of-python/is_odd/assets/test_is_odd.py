import unittest
import sys
sys.path.append("/home/labex/project")
from is_odd import *

class TestIsOdd(unittest.TestCase):
    def test_odd_number(self):
        self.assertEqual(is_odd(3), True)
    
    def test_even_number(self):
        self.assertEqual(is_odd(4), False)
    
    def test_zero(self):
        self.assertEqual(is_odd(0), False)
    
    def test_negative_odd_number(self):
        self.assertEqual(is_odd(-5), True)
    
    def test_negative_even_number(self):
        self.assertEqual(is_odd(-6), False)
    
if __name__ == '__main__':
    unittest.main()