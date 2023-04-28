import unittest
import sys

sys.path.append("/home/labex/project")
from words import *


class TestWords(unittest.TestCase):
    def test_words(self):
        self.assertEqual(words("Hello, World!"), ["Hello", "World"])
        self.assertEqual(words("This is a test."), ["This", "is", "a", "test"])
        self.assertEqual(words("12345"), [])
        self.assertEqual(
            words("Hello, World!", pattern="[a-zA-Z]+"), ["Hello", "World"]
        )
        self.assertEqual(
            words("This is a test.", pattern="[a-z]+"), ["is", "a", "test"]
        )
        self.assertEqual(
            words("Hello-World", pattern="[a-zA-Z]+-?[a-zA-Z]+"), ["Hello-World"]
        )


if __name__ == "__main__":
    unittest.main()