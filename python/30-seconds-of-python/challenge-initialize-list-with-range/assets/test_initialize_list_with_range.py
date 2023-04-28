import unittest
import sys

sys.path.append("/home/labex/project")
from initialize_list_with_range import *


class TestInitializeListWithRange(unittest.TestCase):
    def test_default_step(self):
        self.assertEqual(initialize_list_with_range(5), [0, 1, 2, 3, 4, 5])

    def test_custom_start_and_step(self):
        self.assertEqual(initialize_list_with_range(10, 2, 2), [2, 4, 6, 8, 10])

    def test_negative_start_and_step(self):
        self.assertEqual(initialize_list_with_range(5, -5, -1), [-5, -4, -3, -2, -1, 0])

    def test_end_equals_start(self):
        self.assertEqual(initialize_list_with_range(0), [0])

    def test_end_less_than_start(self):
        self.assertEqual(initialize_list_with_range(-5, -1), [])
