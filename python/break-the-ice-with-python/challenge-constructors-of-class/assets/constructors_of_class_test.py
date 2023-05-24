import sys

sys.path.append("/home/labex/project")
import unittest

from constructors_of_class import Circle


class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(
            circle.area(), 78.54, places=4, msg="Area calculation is incorrect"
        )


if __name__ == "__main__":
    unittest.main()
