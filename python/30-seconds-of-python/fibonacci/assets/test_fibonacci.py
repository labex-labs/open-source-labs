import unittest
from fibonacci import *

class TestFibonacci(unittest.TestCase):
    
    def test_negative_input(self):
        self.assertEqual(fibonacci(-1), [0])
        
    def test_zero_input(self):
        self.assertEqual(fibonacci(0), [0])
        
    def test_positive_input(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3, 5])
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertEqual(fibonacci(1), [0, 1])
        
if __name__ == '__main__':
    unittest.main()