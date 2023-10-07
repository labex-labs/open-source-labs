import unittest
import sys

sys.path.append("/home/labex/project")

from print_keys_of_a_dictionary import print_keys_of_a_dictionary


class TestPrintKeysOfADictionary(unittest.TestCase):
    def test_print_keys(self):
        # Redirect stdout to a buffer
        from io import StringIO
        import sys

        buffer = StringIO()
        sys.stdout = buffer

        # Call the function
        print_keys_of_a_dictionary()

        # Get the output from the buffer
        output = buffer.getvalue().strip()

        # Assert that the output is correct
        expected_output = str(dict.fromkeys(range(1, 21)).keys())
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
