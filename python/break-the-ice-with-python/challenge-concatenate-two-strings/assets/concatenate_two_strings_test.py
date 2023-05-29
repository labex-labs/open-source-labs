import unittest
import sys
sys.path.append("/home/labex/project")
from io import StringIO
from concatenate_two_strings import concatenate_two_strings

class TestPrintValue(unittest.TestCase):
    def test_print(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        concatenate_two_strings("hello", "world")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "helloworld")

if __name__ == '__main__':
    unittest.main()
