import unittest
import ast
import sys

sys.path.append("/home/project")

from catch_the_exceptions import divide

class TestDivideFunction(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide()

    def test_try_except(self):
        with open('/home/project/catch_the_exceptions.py', 'r') as f:
            source = f.read()
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Try):
                if not node.handlers:
                    self.fail("No exception handler in try-except block at line {}".format(node.lineno))
                elif len(node.handlers) > 1:
                    self.fail("Multiple exception handlers in try-except block at line {}".format(node.lineno))
                elif not isinstance(node.handlers[0].type, ast.Name) or node.handlers[0].type.id != 'Exception':
                    self.fail("Incorrect exception type in try-except block at line {}".format(node.lineno))
                elif not node.handlers[0].body:
                    self.fail("Empty exception handler in try-except block at line {}".format(node.lineno))
                else:
                    self.assertTrue(True)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
