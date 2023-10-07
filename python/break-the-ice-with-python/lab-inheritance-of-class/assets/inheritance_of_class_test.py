import sys

sys.path.append("/home/labex/project")
import unittest
from inheritance_of_class import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        square1 = Square(5)
        self.assertEqual(square1.area(), 25, "Area calculation is incorrect")
        square2 = Square()
        self.assertEqual(square2.area(), 0, "Area calculation is incorrect")


if __name__ == "__main__":
    unittest.main()
