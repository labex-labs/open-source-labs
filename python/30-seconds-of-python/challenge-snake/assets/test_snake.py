import unittest
import sys

sys.path.append("/home/labex/project")
from snake import *


class TestSnake(unittest.TestCase):
    def test_snake(self):
        self.assertEqual(snake("helloWorld"), "hello_world")
        self.assertEqual(snake("snake_case"), "snake_case")
        self.assertEqual(snake("kebab-case"), "kebab_case")
        self.assertEqual(snake("CamelCaseTest"), "camel_case_test")
        self.assertEqual(snake("ALLCAPS"), "allcaps")
        self.assertEqual(snake(""), "")
