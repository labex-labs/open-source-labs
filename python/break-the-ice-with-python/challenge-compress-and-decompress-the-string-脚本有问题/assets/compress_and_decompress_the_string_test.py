import unittest
import zlib
from io import StringIO
import sys
sys.path.append("/home/labex/project")
from compress_and_decompress_the_string import compress_and_decompress_the_string

class TestCompressAndDecompress(unittest.TestCase):
    def test_compress_and_decompress_the_string(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to compress and decompress a string and print the results
        compress_and_decompress_the_string()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid compressed and decompressed string
        try:
            output_lines = output.split('\n')
            self.assertEqual(len(output_lines), 2)
            compressed_string = bytes(output_lines[0], 'utf-8')
            decompressed_string = bytes(output_lines[1], 'utf-8')
            self.assertIsInstance(compressed_string, bytes)
            self.assertIsInstance(decompressed_string, bytes)
            self.assertEqual(zlib.decompress(compressed_string), bytes(
                'hello world!hello world!hello world!hello world!', 'utf-8'))
        except (ValueError, TypeError):
            self.fail("Output is not a valid compressed and decompressed string")


if __name__ == '__main__':
    unittest.main()
