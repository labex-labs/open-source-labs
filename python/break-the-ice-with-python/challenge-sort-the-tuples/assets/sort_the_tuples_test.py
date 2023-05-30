import unittest
import sys
from io import StringIO

# Add the path of the code file
sys.path.append("/home/labex/project")

# Import the code to be tested
from sort_the_tuples import sort_the_tuples


class TestYour(unittest.TestCase):
    def test_output(self):
        # Redirect standard input and output to buffer
        stdin = sys.stdin
        stdout = sys.stdout
        sys.stdin = StringIO()
        sys.stdout = StringIO()

        # Input test data
        test_input = "Tom,19,80\nJohn,20,90\nJony,17,91\nJony,17,93\nJson,21,85\n\n"
        sys.stdin.write(test_input)
        sys.stdin.seek(0)

        # Run the code
        sort_the_tuples()

        # Restore standard input and output
        output = sys.stdout.getvalue()
        sys.stdin = stdin
        sys.stdout = stdout

        # Check if the output matches the expected result
        expected_output = "[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]\n"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
