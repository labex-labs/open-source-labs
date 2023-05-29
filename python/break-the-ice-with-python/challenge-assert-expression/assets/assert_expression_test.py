import ast
import unittest
import sys

sys.path.append("/home/labex/project")


class TestAssertExpressions(unittest.TestCase):
    def test_assert_expressions(self):
        with open("/home/labex/project/assert_expression.py", "r") as f:
            tree = ast.parse(f.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.Assert):
                    self.assertTrue(True)
                    return
            self.fail("Do not find assert expressions in your code")


if __name__ == "__main__":
    unittest.main()
