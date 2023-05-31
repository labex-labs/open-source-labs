import unittest
import sys
from io import StringIO

# Add the path of the code file
sys.path.append("/home/labex/project")

# Import the code to be tested
from print_each_even_numbers import print_each_even_numbers

class TestYour(unittest.TestCase):
    def test_output(self):
        # Redirect standard output to buffer
        stdout = sys.stdout
        sys.stdout = StringIO()

        # Run the code
        print_each_even_numbers()

        # Restore standard output
        output = sys.stdout.getvalue()
        sys.stdout = stdout

        # Check if the output matches the expected result
        expected_output = '2000,2002,2004,2006,2008,2020,2022,2024,2026,2028,2040,2042,2044,2046,2048,2060,2062,2064,2066,2068,2080,2082,2084,2086,2088,2200\n'
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
