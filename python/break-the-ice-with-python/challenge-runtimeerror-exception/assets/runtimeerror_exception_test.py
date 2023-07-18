import unittest
import ast

file_path = '/home/labex/project/runtimeerror_exception.py'


class TestCode(unittest.TestCase):
    def test_raise_runtime_error(self):
        with open(file_path, 'r') as f:
            code = f.read()
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Raise):
                for child_node in ast.walk(node):
                    if isinstance(child_node, ast.Name) and child_node.id == 'RuntimeError':
                        self.assertTrue(True)
                        return
        self.fail('No raise statement with RuntimeError found in code file')


if __name__ == '__main__':
    unittest.main()
