import unittest
from powerset import *

class TestPowerset(unittest.TestCase):

    def test_powerset(self):
        self.assertEqual(powerset([1,2,3]), [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)])
        self.assertEqual(powerset([4,5]), [(), (4,), (5,), (4,5)])
        self.assertEqual(powerset(['a','b','c']), [(), ('a',), ('b',), ('c',), ('a', 'b'), ('a', 'c'), ('b', 'c'), ('a', 'b', 'c')])

if __name__ == '__main__':
    unittest.main()