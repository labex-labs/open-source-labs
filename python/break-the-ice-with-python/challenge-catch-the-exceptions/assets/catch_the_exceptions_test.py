import unittest
import ast
import sys

sys.path.append("/home/labex/project")

from catch_the_exceptions import divide

class TestDivideFunction(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide()

    def check_try_except(filename):
        with open('/home/labex/project/catch_the_exceptions.py', 'r') as f:
            source = f.read()
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Try):
                if not node.handlers:
                    print(
                        f"Error: No exception handler in try-except block at line {node.lineno}")
                elif len(node.handlers) > 1:
                    print(
                        f"Error: Multiple exception handlers in try-except block at line {node.lineno}")
                elif not isinstance(node.handlers[0].type, ast.Name) or node.handlers[0].type.id != 'Exception':
                    print(
                        f"Error: Incorrect exception type in try-except block at line {node.lineno}")
                elif not node.handlers[0].body:
                    print(
                        f"Error: Empty exception handler in try-except block at line {node.lineno}")
                else:
                    print(
                        f"Success: try-except block at line {node.lineno} is correctly formatted")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
