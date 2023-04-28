import unittest
import sys
sys.path.append("/home/labex/project")
from capitalize_every_word import *

def capitalize_every_word(s):
    return s.title()

class TestCapitalizeEveryWord(unittest.TestCase):
    
    def test_capitalize_every_word(self):
        self.assertEqual(capitalize_every_word("hello world"), "Hello World")
        self.assertEqual(capitalize_every_word("this is a test"), "This Is A Test")
        self.assertEqual(capitalize_every_word("1234"), "1234")
        self.assertEqual(capitalize_every_word(""), "")
        self.assertEqual(capitalize_every_word("hElLo WoRlD"), "Hello World")

if __name__ == '__main__':
    unittest.main()