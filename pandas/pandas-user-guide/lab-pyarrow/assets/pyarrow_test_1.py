import unittest
import importlib

class PyArrowTestCase(unittest.TestCase):
    def test_pyarrow_installed(self):
        try:
            importlib.import_module('pyarrow')
            self.assertTrue(True, "pyarrow已安装")
        except ImportError:
            self.fail("pyarrow未安装")

if __name__ == '__main__':
    unittest.main()
