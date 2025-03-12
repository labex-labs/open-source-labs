# 异常测试

测试是软件开发中至关重要的一部分，其中一个重要方面是确保你的代码能够正确处理错误情况。在 Python 中，`unittest` 模块提供了一种便捷的方式来测试特定异常是否按预期抛出。

1. 打开 `teststock.py` 文件。我们将添加一些用于检查异常的测试方法。这些测试将帮助我们确保代码在遇到无效输入时能正常运行。

```python
def test_shares_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.shares = '50'

def test_shares_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.shares = -50

def test_price_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.price = '490.1'

def test_price_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.price = -490.1

def test_attribute_error(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(AttributeError):
        s.share = 100  # 'share' is incorrect, should be 'shares'
```

现在，让我们来了解这些异常测试是如何工作的。

- `with self.assertRaises(ExceptionType):` 语句创建了一个上下文管理器。这个上下文管理器会检查 `with` 块内的代码是否抛出了指定的异常。
- 如果在 `with` 块内抛出了预期的异常，测试就会通过。这意味着我们的代码能够正确检测到无效输入并抛出相应的错误。
- 如果没有抛出异常或者抛出了不同的异常，测试就会失败。这表明我们的代码可能没有按预期处理无效输入。

这些测试旨在验证以下场景：

- 将 `shares` 属性设置为字符串应该抛出 `TypeError`，因为 `shares` 应该是一个数字。
- 将 `shares` 属性设置为负数应该抛出 `ValueError`，因为股数不能为负数。
- 将 `price` 属性设置为字符串应该抛出 `TypeError`，因为 `price` 应该是一个数字。
- 将 `price` 属性设置为负数应该抛出 `ValueError`，因为价格不能为负数。
- 尝试设置一个不存在的属性 `share`（注意缺少 's'）应该抛出 `AttributeError`，因为正确的属性名是 `shares`。

2. 添加这些测试方法后，保存 `teststock.py` 文件。然后，在终端中使用以下命令运行所有测试：

```bash
python3 teststock.py
```

如果一切正常，你应该会看到输出表明所有 12 个测试都已通过。输出将如下所示：

```
............
----------------------------------------------------------------------
Ran 12 tests in 0.002s

OK
```

这十二个点代表你到目前为止编写的所有测试。上一步有 7 个测试，我们刚刚又添加了 5 个。这个输出表明你的代码正在按预期处理异常，这是一个经过充分测试的程序的良好标志。
