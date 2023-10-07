import unittest
import sys
from io import StringIO

# Add the path of the code file
sys.path.append("/home/labex/project")

# Import the code to be tested
from check_the_validity_of_password import check


class TestYour(unittest.TestCase):
    def test_output(self):
        # Redirect standard input and output to buffer
        stdin = sys.stdin
        stdout = sys.stdout
        sys.stdin = StringIO()
        sys.stdout = StringIO()

        # Input test data
        test_input = "ABd1234@1,a F1#,2w3E*,2We3345\n"
        sys.stdin.write(test_input)
        sys.stdin.seek(0)

        # Run the code
        s = input().split(",")
        lst = filter(check, s)
        print(",".join(lst))

        # Restore standard input and output
        output = sys.stdout.getvalue()
        sys.stdin = stdin
        sys.stdout = stdout

        # Check if the output matches the expected result
        expected_output = "ABd1234@1\n"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
