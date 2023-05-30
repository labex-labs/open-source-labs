import unittest
import sys
# Add the path to the project directory
sys.path.append("/home/labex/project")
from io import StringIO
from find_runner_up_scores import find_runner_up_scores

class TestFindRunnerUpScores(unittest.TestCase):
    def test_find_runner_up_scores(self):
        # Redirect stdin and stdout to buffers
        input_data = "5\n2 3 6 6 5\n"
        expected_output = "5"
        captured_input = StringIO(input_data)
        captured_output = StringIO()
        sys.stdin = captured_input
        sys.stdout = captured_output

        # Call the function to find the runner-up score
        find_runner_up_scores()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is correct
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
