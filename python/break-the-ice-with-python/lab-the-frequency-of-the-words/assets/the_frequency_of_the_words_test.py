import unittest
import sys
from io import StringIO

# Add the path of the code file
sys.path.append("/home/labex/project")

# Import the code to be tested
from the_frequency_of_the_words import the_frequency_of_the_words


class TestYour(unittest.TestCase):
    def test_output(self):
        # Redirect standard input and output to buffer
        stdin = sys.stdin
        stdout = sys.stdout
        sys.stdin = StringIO()
        sys.stdout = StringIO()

        # Input test data
        test_input = "the quick brown fox jumps over the lazy dog"
        sys.stdin.write(test_input)
        sys.stdin.seek(0)

        # Run the code
        the_frequency_of_the_words()

        # Restore standard input and output
        output = sys.stdout.getvalue()
        sys.stdin = stdin
        sys.stdout = stdout

        # Check if the output matches the expected result
        expected_output = (
            "brown:1\ndog:1\nfox:1\njumps:1\nlazy:1\nover:1\nquick:1\nthe:2\n"
        )
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
