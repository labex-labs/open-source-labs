import unittest
from io import StringIO
import sys

sys.path.append("/home/labex/project")

# 导入被测试的代码
from print_such_numbers import print_such_numbers


class TestYour(unittest.TestCase):
    def test_output(self):
        # 重定向标准输出到缓冲区
        stdout = sys.stdout
        sys.stdout = StringIO()

        # 运行代码
        print_such_numbers()

        # 恢复标准输出
        output = sys.stdout.getvalue()
        sys.stdout = stdout

        # 检查输出是否与预期结果匹配
        expected_output = "2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
