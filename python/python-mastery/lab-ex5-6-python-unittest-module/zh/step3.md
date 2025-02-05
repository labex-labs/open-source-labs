# 带有预期错误的单元测试

假设你想要编写一个检查异常的单元测试。以下是你可以做到的方法：

```python
class TestStock(unittest.TestCase):
 ...
    def test_bad_shares(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
             s.shares = '50'
 ...
```

以这个测试为指导，为以下失败模式编写单元测试：

- 测试将`shares`设置为字符串会引发`TypeError`
- 测试将`shares`设置为负数会引发`ValueError`
- 测试将`price`设置为字符串会引发`TypeError`
- 测试将`price`设置为负数会引发`ValueError`
- 测试设置一个不存在的属性`share`会引发`AttributeError`

完成后，你总共应该有大约一打单元测试。

**重要说明**

为了在课程后续使用，你需要有一个能正常工作的`stock.py`和`teststock.py`文件。如果有必要，保存你正在进行的工作，但如果此时代码仍然有问题，强烈建议你从`Solutions/5_6`复制代码。

我们将把`teststock.py`文件用作稍后改进`Stock`代码的工具。你需要保留它，以确保新代码的行为与旧代码相同。
