import unittest
import sys

sys.path.append("/home/labex/project")
from keys_only import *


def keys_only(flat_dict):
    return list(flat_dict.keys())


class TestKeysOnly(unittest.TestCase):
    def test_keys_only(self):
        self.assertEqual(keys_only({"a": 1, "b": 2, "c": 3}), ["a", "b", "c"])
        self.assertEqual(
            keys_only({"name": "John", "age": 30, "city": "New York"}),
            ["name", "age", "city"],
        )
        self.assertEqual(keys_only({}), [])


if __name__ == "__main__":
    unittest.main()
