import ast
import unittest

file_path = '/home/labex/project/subclass_of_class.py'

class Test(unittest.TestCase):
    def test_class_exists(self):
        with open(file_path, 'r') as f:
            module = ast.parse(f.read())
        classes = [node.name for node in ast.walk(module) if isinstance(node, ast.ClassDef)]
        self.assertTrue('American' in classes, "Class 'American' does not exist")
        self.assertTrue('NewYorker' in classes, "Class 'NewYorker' does not exist")
        

if __name__ == '__main__':
    unittest.main()
