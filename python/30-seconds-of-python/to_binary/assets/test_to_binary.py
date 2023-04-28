import unittest
from to_binary import *

def to_binary(n):
    return bin(n)

class TestToBinary(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(to_binary(5), '0b101')
        self.assertEqual(to_binary(10), '0b1010')
    
    def test_negative_integer(self):
        self.assertEqual(to_binary(-5), '-0b101')
        self.assertEqual(to_binary(-10), '-0b1010')
    
    def test_zero(self):
        self.assertEqual(to_binary(0), '0b0')

if __name__ == '__main__':
    unittest.main()