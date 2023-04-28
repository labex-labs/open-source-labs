import unittest
import sys

sys.path.append("/home/labex/project")
from union_by import *


class TestUnionBy(unittest.TestCase):
    def test_union_by(self):
        a = [1, 2, 3]
        b = [2, 3, 4]
        fn = lambda x: x
        self.assertEqual(union_by(a, b, fn), [1, 2, 3, 4])

        a = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        b = [{"id": 2, "name": "Jane"}, {"id": 3, "name": "Bob"}]
        fn = lambda x: x["id"]
        self.assertEqual(
            union_by(a, b, fn),
            [
                {"id": 1, "name": "John"},
                {"id": 2, "name": "Jane"},
                {"id": 3, "name": "Bob"},
            ],
        )

        a = ["apple", "banana", "cherry"]
        b = ["cherry", "durian", "elderberry"]
        fn = lambda x: x[0]
        self.assertEqual(
            union_by(a, b, fn), ["apple", "banana", "cherry", "durian", "elderberry"]
        )
