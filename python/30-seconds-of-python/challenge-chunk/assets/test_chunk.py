import unittest
import sys

sys.path.append("/home/labex/project")
from chunk import *
from math import ceil


def chunk(lst, size):
    return list(
        map(
            lambda x: lst[x * size : x * size + size],
            list(range(ceil(len(lst) / size))),
        )
    )


class TestChunk(unittest.TestCase):
    def test_chunk(self):
        self.assertEqual(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(chunk([1, 2, 3, 4, 5], 3), [[1, 2, 3], [4, 5]])
        self.assertEqual(chunk([1, 2, 3, 4, 5], 1), [[1], [2], [3], [4], [5]])
        self.assertEqual(chunk([], 2), [])
