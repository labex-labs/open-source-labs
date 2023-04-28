import unittest
import sys

sys.path.append("/home/labex/project")
from sort_by_indexes import *


def sort_by_indexes(lst, indexes, reverse=False):
    return [
        val
        for (_, val) in sorted(zip(indexes, lst), key=lambda x: x[0], reverse=reverse)
    ]


class TestSortByIndexes(unittest.TestCase):
    def test_sort_by_indexes(self):
        a = ["eggs", "bread", "oranges", "jam", "apples", "milk"]
        b = [3, 2, 6, 4, 1, 5]
        self.assertEqual(
            sort_by_indexes(a, b), ["apples", "bread", "eggs", "jam", "milk", "oranges"]
        )
        self.assertEqual(
            sort_by_indexes(a, b, True),
            ["oranges", "milk", "jam", "eggs", "bread", "apples"],
        )


if __name__ == "__main__":
    unittest.main()
