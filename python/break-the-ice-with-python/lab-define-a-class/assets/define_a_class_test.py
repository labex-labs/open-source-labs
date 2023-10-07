import unittest
import sys
from io import StringIO

# 添加代码文件路径
sys.path.append("/home/labex/project")

# 导入被测试的代码
from define_a_class import IOstring


class TestYour(unittest.TestCase):
    def test_output(self):
        # 重定向标准输入输出到缓冲区
        stdin = sys.stdin
        stdout = sys.stdout
        sys.stdin = StringIO()
        sys.stdout = StringIO()

        # 输入测试数据
        test_input = "hello\n"
        sys.stdin.write(test_input)
        sys.stdin.seek(0)

        # 运行代码
        xx = IOstring()
        xx.get_string()
        xx.print_string()

        # 恢复标准输入输出
        output = sys.stdout.getvalue()
        sys.stdin = stdin
        sys.stdout = stdout

        # 检查输出是否与预期结果匹配
        expected_output = "HELLO\n"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
