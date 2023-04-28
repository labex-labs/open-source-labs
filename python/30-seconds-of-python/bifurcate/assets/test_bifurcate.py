import unittest
from bifurcate import *

def bifurcate(lst, filter):
    return [
        [x for x, flag in zip(lst, filter) if flag],
        [x for x, flag in zip(lst, filter) if not flag]
    ]

class TestBifurcate(unittest.TestCase):
    def test_bifurcate(self):
        self.assertEqual(bifurcate([1, 2, 3, 4, 5], [True, False, True, False, True]), [[1, 3, 5], [2, 4]])
        self.assertEqual(bifurcate(['a', 'b', 'c', 'd', 'e'], [False, True, False, True, False]), [['b', 'd'], ['a', 'c', 'e']])
        self.assertEqual(bifurcate([], []), [[], []])
        self.assertEqual(bifurcate([1, 2, 3], [True, True, True]), [[1, 2, 3], []])
        self.assertEqual(bifurcate([1, 2, 3], [False, False, False]), [[], [1, 2, 3]])

if __name__ == '__main__':
    unittest.main()