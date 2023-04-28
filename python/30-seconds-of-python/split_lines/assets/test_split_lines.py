import unittest
import sys
sys.path.append("/home/labex/project")
from split_lines import *

class TestSplitLines(unittest.TestCase):
    
    def test_split_lines(self):
        s = "Hello\nWorld\n"
        expected_output = ["Hello", "World", ""]
        self.assertEqual(split_lines(s), expected_output)
        
    def test_split_lines_empty_string(self):
        s = ""
        expected_output = [""]
        self.assertEqual(split_lines(s), expected_output)
        
    def test_split_lines_single_line(self):
        s = "Hello"
        expected_output = ["Hello"]
        self.assertEqual(split_lines(s), expected_output)
        
    def test_split_lines_multiple_empty_lines(self):
        s = "\n\n\n"
        expected_output = ["", "", "", ""]
        self.assertEqual(split_lines(s), expected_output)
        
    def test_split_lines_tab_delimiter(self):
        s = "Hello\tWorld"
        expected_output = ["Hello\tWorld", ""]
        self.assertEqual(split_lines(s), expected_output)