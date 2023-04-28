import unittest
from num_to_range import *


class TestNumToRange(unittest.TestCase):
    
    def test_num_to_range(self):
        self.assertEqual(num_to_range(50, 0, 100, 0, 10), 5)
        self.assertEqual(num_to_range(25, 0, 50, 0, 5), 2.5)
        self.assertEqual(num_to_range(75, 50, 100, 5, 10), 7.5)
        self.assertEqual(num_to_range(0, -10, 10, 0, 100), 50)
        self.assertEqual(num_to_range(10, -10, 10, 0, 100), 100)
        
if __name__ == '__main__':
    unittest.main()