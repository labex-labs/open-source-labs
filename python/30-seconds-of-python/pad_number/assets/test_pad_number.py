import unittest
import sys
sys.path.append("/home/labex/project")
from pad_number import *

class TestPadNumber(unittest.TestCase):
    
    def test_pad_number(self):
        self.assertEqual(pad_number(5, 3), '005')
        self.assertEqual(pad_number(10, 5), '00010')
        self.assertEqual(pad_number(1234, 2), '1234')
        self.assertEqual(pad_number(0, 4), '0000')
        self.assertEqual(pad_number(987654321, 9), '987654321')
        
if __name__ == '__main__':
    unittest.main()