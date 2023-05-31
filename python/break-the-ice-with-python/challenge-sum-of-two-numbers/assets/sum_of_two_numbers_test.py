import unittest
import sys
sys.path.append("/home/labex/project")
from sum_of_two_numbers import sum_of_two_numbers

class TestSumFunction(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_of_two_numbers(1, 2), 3)
        self.assertEqual(sum_of_two_numbers(-1, 1), 0)
        self.assertEqual(sum_of_two_numbers(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
