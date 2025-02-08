# 练习8.1：编写单元测试

在一个单独的文件 `test_stock.py` 中，为 `Stock` 类编写一组单元测试。为了帮助你开始，这里有一小段测试实例创建的代码：

```python
# test_stock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

if __name__ == '__main__':
    unittest.main()
```

运行你的单元测试。你应该会得到类似这样的输出：

## .

Ran 1 tests in 0.000s

    OK

一旦你确定它能正常工作，编写额外的单元测试来检查以下内容：

- 确保 `s.cost` 属性返回正确的值（49010.0）
- 确保 `s.sell()` 方法能正确工作。它应该相应地减少 `s.shares` 的值。
- 确保 `s.shares` 属性不能被设置为非整数值。

对于最后一部分，你需要检查是否会引发异常。一种简单的方法是使用如下代码：

```python
class TestStock(unittest.TestCase):
  ...
    def test_bad_shares(self):
         s = stock.Stock('GOOG', 100, 490.1)
         with self.assertRaises(TypeError):
             s.shares = '100'
```
