import ast
import unittest

file_path = '/home/labex/project/static_method_of_class.py'

class Test(unittest.TestCase):
    def test_class_exists(self):
        with open(file_path, 'r') as f:
            tree = ast.parse(f.read())
            classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
            self.assertTrue('American' in classes, "Class 'American' does not exist")

    def test_method_exists(self):
        with open(file_path, 'r') as f:
            tree = ast.parse(f.read())
            methods = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            self.assertTrue('printNationality' in methods, "Method 'printNationality' does not exist")

    def test_staticmethod_exists(self):
        with open(file_path, 'r') as f:
            tree = ast.parse(f.read())
            staticmethods = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and 'staticmethod' in [d.id for d in node.decorator_list]]
            self.assertTrue('printNationality' in staticmethods, "Keyword 'staticmethod' does not exist")

if __name__ == '__main__':
    unittest.main()
