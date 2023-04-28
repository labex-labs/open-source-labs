import unittest
from sample import *
from random import choice

class TestSample(unittest.TestCase):
    
    def test_sample(self):
        lst = [1, 2, 3, 4, 5]
        result = sample(lst)
        self.assertIn(result, lst)

if __name__ == '__main__':
    unittest.main()