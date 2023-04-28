import unittest
import sys
sys.path.append("/home/labex/project")
from camel import *

class TestCamel(unittest.TestCase):
    def test_camel(self):
        self.assertEqual(camel("hello_world"), "helloWorld")
        self.assertEqual(camel("hello-world"), "helloWorld")
        self.assertEqual(camel("hello world"), "helloWorld")
        self.assertEqual(camel("HELLO_WORLD"), "helloWorld")
        self.assertEqual(camel("hElLo_WoRlD"), "helloWorld")

if __name__ == '__main__':
    unittest.main()