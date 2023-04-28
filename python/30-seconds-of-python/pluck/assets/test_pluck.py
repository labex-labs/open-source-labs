import unittest
from pluck import *


def pluck(lst, key):
    return [x.get(key) for x in lst]

class TestPluck(unittest.TestCase):
    def test_pluck(self):
        lst = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}]
        self.assertEqual(pluck(lst, 'name'), ['John', 'Jane'])
        self.assertEqual(pluck(lst, 'age'), [25, 30])
        self.assertEqual(pluck(lst, 'gender'), [None, None])

if __name__ == '__main__':
    unittest.main()