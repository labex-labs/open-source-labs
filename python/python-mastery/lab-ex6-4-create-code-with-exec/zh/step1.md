# 理解 `exec()` 的基础知识

在 Python 中，`exec()` 函数是一个强大的工具，它允许你执行在运行时动态创建的代码。这意味着你可以根据特定的输入或配置动态生成代码，这在许多编程场景中非常有用。

让我们从探索 `exec()` 函数的基本用法开始。为此，我们将打开一个 Python 交互式环境。打开你的终端并输入 `python3`。这个命令将启动交互式 Python 解释器，你可以在其中直接运行 Python 代码。

```bash
python3
```

现在，我们将把一段 Python 代码定义为一个字符串，然后使用 `exec()` 函数来执行它。以下是具体操作方法：

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
```

在这个示例中：

1. 首先，我们定义了一个名为 `code` 的字符串。这个字符串包含一个 Python 的 `for` 循环。该循环设计为迭代 `n` 次，并打印每次迭代的数字。
2. 然后，我们定义了一个变量 `n` 并将其赋值为 10。这个变量用作循环中 `range()` 函数的上限。
3. 之后，我们调用 `exec()` 函数，并将 `code` 字符串作为参数传入。`exec()` 函数会将该字符串作为 Python 代码执行。
4. 最后，循环运行并打印出从 0 到 9 的数字。

当我们使用 `exec()` 函数创建更复杂的代码结构（如函数或方法）时，它的真正强大之处就更加明显了。让我们尝试一个更高级的示例，在这个示例中，我们将为一个类动态创建一个 `__init__()` 方法。

```python
>>> class Stock:
...     _fields = ('name', 'shares', 'price')
...
>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
...     code += f'    self.{name} = {name}\n'
...
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # Now try the class
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
```

在这个更复杂的示例中：

1. 我们首先定义了一个 `Stock` 类，该类有一个 `_fields` 属性。这个属性是一个元组，包含了类的属性名称。
2. 然后，我们创建了一个字符串，该字符串表示 `__init__` 方法的 Python 代码。这个方法用于初始化对象的属性。
3. 接下来，我们使用 `exec()` 函数来执行代码字符串。我们还将一个空字典 `locs` 传递给 `exec()`。执行结果得到的函数会存储在这个字典中。
4. 之后，我们将字典中存储的函数赋值给 `Stock` 类的 `__init__` 方法。
5. 最后，我们创建了一个 `Stock` 类的实例，并通过访问对象的属性来验证 `__init__` 方法是否正常工作。

这个示例展示了如何使用 `exec()` 函数根据运行时可用的数据动态创建方法。
