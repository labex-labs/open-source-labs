import unittest
import sys

sys.path.append("/home/labex/project")

from custom_exception_class import CustomException


class TestCustomException(unittest.TestCase):
    def test_input_less_than_10(self):
        with self.assertRaises(CustomException) as cm:
            num = 5
            if num < 10:
                raise CustomException("Input is less than 10")
        self.assertEqual(str(cm.exception), "Input is less than 10")

    def test_input_greater_than_10(self):
        with self.assertRaises(CustomException) as cm:
            num = 15
            if num > 10:
                raise CustomException("Input is greater than 10")
        self.assertEqual(str(cm.exception), "Input is greater than 10")

if __name__ == '__main__':
    unittest.main()
