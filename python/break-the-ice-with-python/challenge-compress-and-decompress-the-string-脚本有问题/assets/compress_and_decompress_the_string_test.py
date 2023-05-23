import unittest
import ast

file_path = '/home/labex/project/compress_and_decompress_the_string.py'

class TestZlibUsage(unittest.TestCase):
    def test_zlib_usage(self):
        with open(file_path, 'r') as f:
            code = f.read()
            if not code.strip():
                self.fail(f"{file_path} is empty.")
            try:
                tree = ast.parse(code)
            except SyntaxError:
                self.fail(f"{file_path} contains syntax errors.")

        found_zlib_usage = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == 'compress' and isinstance(node.func.value, ast.Name) and node.func.value.id == 'zlib':
                    found_zlib_usage = True
                    break
                elif node.func.attr == 'decompress' and isinstance(node.func.value, ast.Name) and node.func.value.id == 'zlib':
                    found_zlib_usage = True
                    break

        if found_zlib_usage:
            self.assertTrue(True)
        else:
            self.fail(f"{file_path} does not use zlib module for string compression/decompression.")


if __name__ == '__main__':
    unittest.main()
