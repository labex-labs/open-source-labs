import unittest
import sys

sys.path.append("/home/labex/project")
from merge_dictionaries import *


class TestMergeDictionaries(unittest.TestCase):
    def test_merge_dictionaries(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        dict3 = {"e": 5, "f": 6}
        expected_output = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
        self.assertEqual(merge_dictionaries(dict1, dict2, dict3), expected_output)


if __name__ == "__main__":
    unittest.main()
