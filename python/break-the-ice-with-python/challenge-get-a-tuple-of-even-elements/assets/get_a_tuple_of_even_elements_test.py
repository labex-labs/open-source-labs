import unittest
import sys

sys.path.append("/home/labex/project")

from get_a_tuple_of_even_elements import get_a_tuple_of_even_elements

class TestGetATupleOfEvenElements(unittest.TestCase):
    def test_get_a_tuple_of_even_elements(self):
        # Redirect stdout to a buffer
        from io import StringIO
        import sys
        buffer = StringIO()
        sys.stdout = buffer

        # Call the function
        get_a_tuple_of_even_elements()

        # Get the output from the buffer
        output = buffer.getvalue().strip()

        # Assert that the output is correct
        expected_output = "(2, 4, 6, 8, 10)"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
