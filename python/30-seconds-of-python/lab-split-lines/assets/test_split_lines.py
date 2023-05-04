import unittest
import sys

sys.path.append("/home/labex/project")
from split_lines import *


class TestSplitLines(unittest.TestCase):
    def test_split_lines(self):
        s = "This\nis a\nmultiline\nstring.\n"
        expected_output = ["This", "is a", "multiline", "string.", ""]
        self.assertEqual(split_lines(s), expected_output)
