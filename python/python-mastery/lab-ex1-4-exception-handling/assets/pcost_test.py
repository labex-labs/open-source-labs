import unittest
import sys
import io

sys.path.append("/home/labex/project")

from pcost import portfolio_cost


class TestPortfolioCost(unittest.TestCase):
    def test_value_error(self):
        # 准备测试数据
        filename = "/home/labex/project/portfolio3.dat"

        # 重定向标准输出到缓冲区
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # 调用被测试的函数
        portfolio_cost(filename)

        # 恢复标准输出
        sys.stdout = sys.__stdout__

        # 获取捕获的输出
        output = captured_output.getvalue()

        # 验证输出是否包含预期的错误信息
        self.assertIn("invalid literal for int() with base 10: '-'", output)


if __name__ == "__main__":
    unittest.main()
