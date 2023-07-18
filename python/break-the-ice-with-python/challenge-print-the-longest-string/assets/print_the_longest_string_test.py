import unittest
import sys
sys.path.append("/home/labex/project")
from io import StringIO
from print_the_longest_string import print_the_longest_string

class TestPrintVal(unittest.TestCase):
    def test_print(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        print_the_longest_string("hello", "world")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "hello\nworld")

        captured_output = StringIO()
        sys.stdout = captured_output
        print_the_longest_string("hello", "123456")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "123456")

if __name__ == '__main__':
    unittest.main()
