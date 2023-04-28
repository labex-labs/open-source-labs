import unittest
import sys

sys.path.append("/home/labex/project")
from map_values import *


class TestMapValues(unittest.TestCase):
    def test_map_values(self):
        obj = {"a": 1, "b": 2, "c": 3}
        fn = lambda x: x * 2
        result = map_values(obj, fn)
        expected = {"a": 2, "b": 4, "c": 6}
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
