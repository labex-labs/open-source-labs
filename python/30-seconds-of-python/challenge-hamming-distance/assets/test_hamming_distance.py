import unittest
import sys
sys.path.append("/home/labex/project")
from hamming_distance import *

class TestHammingDistance(unittest.TestCase):
    
    def test_hamming_distance(self):
        self.assertEqual(hamming_distance(0, 0), 0)
        self.assertEqual(hamming_distance(1, 4), 2)
        self.assertEqual(hamming_distance(7, 10), 3)
        self.assertEqual(hamming_distance(15, 15), 0)
        self.assertEqual(hamming_distance(255, 0), 8)
        self.assertEqual(hamming_distance(1023, 1023), 0)

if __name__ == '__main__':
    unittest.main()