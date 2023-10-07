import unittest
import sys
import ast

sys.path.append("/home/labex/project")


def find_hello_world(code):
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Str) and node.s == "hello world!":
            return True
    return False


class TestUnicodeString(unittest.TestCase):
    def test_unicode_string(self):
        with open("/home/labex/project/unicode_string.py", "r") as f:
            code = f.read()
        self.assertTrue(find_hello_world(code))


if __name__ == "__main__":
    unittest.main()
