import unittest
from group_by import *
from collections import defaultdict

def group_by(lst, fn):
    d = defaultdict(list)
    for el in lst:
        d[fn(el)].append(el)
    return dict(d)

class TestGroupBy(unittest.TestCase):
    def test_group_by(self):
        lst = [1, 2, 3, 4, 5, 6]
        fn = lambda x: x % 2
        expected_output = {0: [2, 4, 6], 1: [1, 3, 5]}
        self.assertEqual(group_by(lst, fn), expected_output)

if __name__ == '__main__':
    unittest.main()