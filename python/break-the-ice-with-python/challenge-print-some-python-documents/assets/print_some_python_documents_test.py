import ast
import unittest

file_path = 'E:\\VSCode\\github\\open-source-challenges\\python\\break-the-ice-with-python\\challenge-print-some-python-documents\\assets\\print_some_python_documents.py'

class DocStringVisitor(ast.NodeVisitor):
    def __init__(self):
        self.has_doc = False

    def visit_FunctionDef(self, node):
        for child in ast.walk(node):
            if isinstance(child, ast.Name) and child.id == '__doc__':
                self.has_doc = True
                break
        self.generic_visit(node)

class TestCode(unittest.TestCase):
    def test_doc(self):
        with open(file_path, 'r') as f:
            code = f.read()
        tree = ast.parse(code)
        visitor = DocStringVisitor()
        visitor.visit(tree)
        self.assertTrue(visitor.has_doc, 'Code does not have __doc__')

if __name__ == '__main__':
    unittest.main()
