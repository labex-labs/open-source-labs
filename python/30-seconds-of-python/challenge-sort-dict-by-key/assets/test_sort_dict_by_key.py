import unittest
import sys

sys.path.append("/home/labex/project")
from sort_dict_by_key import *


class TestSortDictByKey(unittest.TestCase):
    def test_sort_dict_by_key(self):
        d = {"b": 2, "a": 1, "c": 3}
        expected_output = {"a": 1, "b": 2, "c": 3}
        self.assertEqual(sort_dict_by_key(d), expected_output)

        d = {"b": 2, "a": 1, "c": 3}
        expected_output = {"c": 3, "b": 2, "a": 1}
        self.assertEqual(sort_dict_by_key(d, reverse=True), expected_output)

        d = {}
        expected_output = {}
        self.assertEqual(sort_dict_by_key(d), expected_output)

        d = {"a": 1}
        expected_output = {"a": 1}
        self.assertEqual(sort_dict_by_key(d), expected_output)
