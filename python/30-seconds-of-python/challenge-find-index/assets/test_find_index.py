import unittest
import sys

sys.path.append("/home/labex/project")
from find_index import *


class TestFindIndex(unittest.TestCase):
    def test_find_index(self):
        lst = [1, 2, 3, 4, 5]
        fn = lambda x: x > 3
        self.assertEqual(find_index(lst, fn), 3)

        lst = ["apple", "banana", "cherry"]
        fn = lambda x: "a" in x
        self.assertEqual(find_index(lst, fn), 0)

        lst = [True, False, True, False]
        fn = lambda x: x == False
        self.assertEqual(find_index(lst, fn), 1)

        lst = []
        fn = lambda x: x > 0
        self.assertRaises(StopIteration, find_index, lst, fn)


if __name__ == "__main__":
    unittest.main()