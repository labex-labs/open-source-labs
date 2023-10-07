import unittest
import sys

sys.path.append("/home/labex/project")
from io import StringIO
from generate_a_3D_array import generate_a_3D_array


class TestGenerate3DArray(unittest.TestCase):
    def test_generate_3D_array(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to generate a 3D array
        generate_a_3D_array()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid 3D array
        try:
            array = eval(output)
            expected = [
                [[0 for col in range(8)] for col in range(5)] for row in range(3)
            ]
            self.assertListEqual(array, expected)
        except (ValueError, TypeError):
            self.fail("Output is not a valid 3D array")


if __name__ == "__main__":
    unittest.main()
