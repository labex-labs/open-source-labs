import unittest
from sum_by import *

def sum_by(lst, fn):
    return sum(map(fn, lst))

class TestSumBy(unittest.TestCase):
    def test_sum_by(self):
        self.assertEqual(sum_by([1, 2, 3], lambda x: x), 6)
        self.assertEqual(sum_by([1, 2, 3], lambda x: x**2), 14)
        self.assertEqual(sum_by([1, 2, 3], lambda x: x+1), 9)
        self.assertEqual(sum_by([], lambda x: x), 0)

if __name__ == '__main__':
    unittest.main()