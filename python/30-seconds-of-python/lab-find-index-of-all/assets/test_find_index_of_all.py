import unittest
import sys

sys.path.append("/home/labex/project")
from find_index_of_all import *


class TestFindIndexOfAll(unittest.TestCase):
    def test_find_index_of_all(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        fn = lambda x: x % 2 == 0
        self.assertEqual(find_index_of_all(lst, fn), [1, 3, 5, 7, 9])

        lst = ["apple", "banana", "cherry", "date", "elderberry"]
        fn = lambda x: len(x) > 5
        self.assertEqual(find_index_of_all(lst, fn), [1, 2, 4])

        lst = [True, False, True, False, True]
        fn = lambda x: x == True
        self.assertEqual(find_index_of_all(lst, fn), [0, 2, 4])


if __name__ == "__main__":
    unittest.main()
