import unittest
import sys

sys.path.append("/home/labex/project")
from byte_size import *


def byte_size(s):
    return len(s.encode("utf-8"))


class TestByteSize(unittest.TestCase):
    def test_byte_size(self):
        self.assertEqual(byte_size("hello"), 5)
        self.assertEqual(byte_size(""), 0)
        self.assertEqual(byte_size("1234567890"), 10)
        self.assertEqual(byte_size("こんにちは"), 15)
        self.assertEqual(byte_size("你好"), 6)


if __name__ == "__main__":
    unittest.main()
