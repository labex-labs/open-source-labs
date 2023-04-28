import unittest
from sum_of_powers import *

class TestSumOfPowers(unittest.TestCase):

    def test_sum_of_powers(self):
        self.assertEqual(sum_of_powers(5), 55)
        self.assertEqual(sum_of_powers(5, 3), 225)
        self.assertEqual(sum_of_powers(5, 2, 2), 54)

if __name__ == '__main__':
    unittest.main()