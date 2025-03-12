# 扩展你的测试用例

既然你已经创建了一个基本的测试用例，现在是时候扩大你的测试范围了。添加更多的测试将有助于你覆盖 `Stock` 类的其余功能。这样，你可以确保该类的所有方面都能按预期工作。我们将修改 `TestStock` 类，以包含对几个方法和属性的测试。

1. 打开 `teststock.py` 文件。在 `TestStock` 类中，我们将添加一些新的测试方法。这些方法将测试 `Stock` 类的不同部分。以下是你需要添加的代码：

```python
def test_create_keyword_args(self):
    s = stock.Stock(name='GOOG', shares=100, price=490.1)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_cost(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s.cost, 49010.0)

def test_sell(self):
    s = stock.Stock('GOOG', 100, 490.1)
    s.sell(20)
    self.assertEqual(s.shares, 80)

def test_from_row(self):
    row = ['GOOG', '100', '490.1']
    s = stock.Stock.from_row(row)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_repr(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

def test_eq(self):
    s1 = stock.Stock('GOOG', 100, 490.1)
    s2 = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s1, s2)
```

让我们仔细看看这些测试各自的作用：

- `test_create_keyword_args`：此测试检查你是否可以使用关键字参数创建一个 `Stock` 对象。它验证对象的属性是否设置正确。
- `test_cost`：此测试检查 `Stock` 对象的 `cost` 属性是否返回正确的值，该值是通过股数乘以价格计算得出的。
- `test_sell`：此测试检查 `Stock` 对象的 `sell()` 方法在卖出部分股票后是否正确更新股数。
- `test_from_row`：此测试检查 `from_row()` 类方法是否可以从数据行创建一个新的 `Stock` 实例。
- `test_repr`：此测试检查 `Stock` 对象的 `__repr__()` 方法是否返回预期的字符串表示形式。
- `test_eq`：此测试检查 `__eq__()` 方法是否能正确比较两个 `Stock` 对象是否相等。

2. 添加这些测试方法后，保存 `teststock.py` 文件。然后，在终端中使用以下命令再次运行测试：

```bash
python3 teststock.py
```

如果所有测试都通过，你应该会看到如下输出：

```
......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

输出中的七个点代表每个测试。每个点表示一个测试已成功通过。所以，如果你看到七个点，就意味着所有七个测试都通过了。
