import unittest
import sys

sys.path.append("/home/labex/project")
from chunk_into_n import *

from math import ceil


def chunk_into_n(lst, n):
    size = ceil(len(lst) / n)
    return list(map(lambda x: lst[x * size : x * size + size], list(range(n))))


class TestChunkIntoN(unittest.TestCase):
    def test_chunk_into_n(self):
        self.assertEqual(chunk_into_n([1, 2, 3, 4, 5], 2), [[1, 2, 3], [4, 5]])
        self.assertEqual(chunk_into_n([1, 2, 3, 4, 5], 3), [[1, 2], [3, 4], [5]])
        self.assertEqual(chunk_into_n([1, 2, 3, 4, 5], 5), [[1], [2], [3], [4], [5]])
        self.assertEqual(
            chunk_into_n([1, 2, 3, 4, 5], 6), [[1], [2], [3], [4], [5], []]
        )
        self.assertEqual(chunk_into_n([], 2), [[], []])
        self.assertEqual(chunk_into_n([1], 2), [[1], []])
        self.assertEqual(chunk_into_n([1, 2], 2), [[1], [2]])


if __name__ == "__main__":
    unittest.main()
