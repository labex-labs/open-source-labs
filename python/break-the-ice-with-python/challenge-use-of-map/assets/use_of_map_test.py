import sys
import unittest
from io import StringIO

sys.path.append("/home/labex/project")
from use_of_map import use_of_map

class Test(unittest.TestCase):

    def test_use_of_filter(self):
        li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]\n"
        with StringIO() as buffer:
            sys.stdout = buffer
            use_of_map()
            sys.stdout = sys.__stdout__
            self.assertEqual(buffer.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
