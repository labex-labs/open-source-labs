# 使用 `__repr__` 改进对象表示

在 Python 中，对象可以通过两种不同的方式表示为字符串。这两种表示方式有不同的用途，并且在各种场景中都很有用。

第一种类型是**字符串表示**。这是由 `str()` 函数创建的，当你使用 `print()` 函数时，它会自动被调用。字符串表示的设计目的是便于人类阅读。它以一种我们易于理解和解释的格式呈现对象。

第二种类型是**代码表示**。这是由 `repr()` 函数生成的。代码表示展示了你为重新创建该对象所需编写的代码。它更侧重于提供一种精确且明确的方式，在代码中表示对象。

让我们使用 Python 的内置 `date` 类来看一个具体的例子。这将帮助你直观地看到字符串表示和代码表示之间的区别。

```python
>>> from datetime import date
>>> d = date(2008, 7, 5)
>>> print(d)              # Uses str()
2008-07-05
>>> d                     # Uses repr()
datetime.date(2008, 7, 5)
```

在这个例子中，当我们使用 `print(d)` 时，Python 会对 `date` 对象 `d` 调用 `str()` 函数，我们会得到一个格式为 `YYYY-MM-DD` 的易读日期。当我们在交互式 shell 中直接输入 `d` 时，Python 会调用 `repr()` 函数，我们会看到重新创建该 `date` 对象所需的代码。

你可以通过多种方式显式地获取 `repr()` 字符串。以下是一些示例：

```python
>>> print('The date is', repr(d))
The date is datetime.date(2008, 7, 5)
>>> print(f'The date is {d!r}')
The date is datetime.date(2008, 7, 5)
>>> print('The date is %r' % d)
The date is datetime.date(2008, 7, 5)
```

现在，让我们将这个概念应用到我们的 `Stock` 类中。我们将通过实现 `__repr__` 方法来改进这个类。当 Python 需要对象的代码表示时，会调用这个特殊方法。

为此，在你的编辑器中打开 `stock.py` 文件。然后，将 `__repr__` 方法添加到 `Stock` 类中。`__repr__` 方法应该返回一个字符串，该字符串展示了重新创建 `Stock` 对象所需的代码。

```python
def __repr__(self):
    return f"Stock('{self.name}', {self.shares}, {self.price})"
```

添加 `__repr__` 方法后，你完整的 `Stock` 类现在应该如下所示：

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
```

现在，让我们测试我们修改后的 `Stock` 类。在你的终端中运行以下命令来打开 Python 交互式 shell：

```bash
python3
```

交互式 shell 打开后，尝试以下命令：

```python
>>> import stock
>>> goog = stock.Stock('GOOG', 100, 490.10)
>>> goog
Stock('GOOG', 100, 490.1)
```

你还可以看看 `__repr__` 方法在股票投资组合中是如何工作的。以下是一个示例：

```python
>>> import reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> portfolio
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44), Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1), Stock('IBM', 100, 70.44)]
```

如你所见，`__repr__` 方法让我们的 `Stock` 对象在交互式 shell 或调试器中显示时更具信息性。它现在展示了重新创建每个对象所需的代码，这对于调试和理解对象的状态非常有用。

测试完成后，你可以通过运行以下命令退出 Python 解释器：

```python
>>> exit()
```
