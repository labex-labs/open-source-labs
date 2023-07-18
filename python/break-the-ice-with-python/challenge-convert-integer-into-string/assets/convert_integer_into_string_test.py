import unittest
import sys
sys.path.append("/home/labex/project")

from io import StringIO

from convert_integer_into_string import convert_integer_into_string

class TestPrintValue(unittest.TestCase):
    def test_print(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        convert_integer_into_string(123)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "123")

if __name__ == '__main__':
    unittest.main()
