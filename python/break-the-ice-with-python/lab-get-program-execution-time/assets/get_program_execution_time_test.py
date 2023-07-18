import unittest
from io import StringIO
import sys
sys.path.append("/home/labex/project")
from get_program_execution_time import get_program_execution_time


class TestProgramExecutionTime(unittest.TestCase):
    def test_get_program_execution_time(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to get program execution time and print it
        get_program_execution_time()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid float
        try:
            output_float = float(output)
            self.assertGreaterEqual(output_float, 0.0)
            self.assertLessEqual(output_float, 1.0)
        except ValueError:
            self.fail("Output is not a valid float")

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
