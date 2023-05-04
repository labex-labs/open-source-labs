import unittest
import sys

sys.path.append("/home/labex/project")
from words import *


class TestWords(unittest.TestCase):
    def test_words(self):
        s1 = "I love Python!!"
        expected_output1 = ["I", "love", "Python"]
        self.assertEqual(words(s1), expected_output1)

        s2 = "python, javaScript & coffee"
        expected_output2 = ["python", "javaScript", "coffee"]
        self.assertEqual(words(s2), expected_output2)

        s3 = "build -q --out one-item"
        pattern = r"\b[a-zA-Z-]+\b"
        expected_output3 = ["build", "q", "out", "one-item"]
        self.assertEqual(words(s3, pattern), expected_output3)


if __name__ == "__main__":
    unittest.main()
