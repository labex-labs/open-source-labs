import unittest
import ast


class TestDefineAnonymousFunctions(unittest.TestCase):
    def test_lambda(self):
        with open("/home/labex/project/define_anonymous_functions.py", "r") as f:
            code = f.read()
        self.assertTrue(check_lambda_usage(code))


def check_lambda_usage(code):
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Lambda):
            return True
    return False


if __name__ == "__main__":
    unittest.main()
