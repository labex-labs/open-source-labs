# 创建一个简单的股票类

在这一步中，我们将创建一个简单的类来表示股票。理解如何创建类是 Python 编程的基础，因为它使我们能够对现实世界的对象及其行为进行建模。这个简单的股票类将是我们探索 Python 对象内部工作原理的起点。

首先，你需要打开一个 Python 交互式 shell。Python 交互式 shell 是试验 Python 代码的好地方。你可以逐个输入并执行 Python 命令。要打开它，请在终端中输入以下命令：

```bash
python3
```

输入命令后，你会看到 Python 提示符 (`>>>`)。这表明你现在已进入 Python 交互式 shell，可以开始编写 Python 代码了。

现在，让我们定义一个 `SimpleStock` 类。Python 中的类就像是创建对象的蓝图。它定义了该类对象将具有的属性（数据）和方法（函数）。以下是如何定义具有必要属性和方法的 `SimpleStock` 类：

```python
>>> class SimpleStock:
...     def __init__(self, name, shares, price):
...         self.name = name
...         self.shares = shares
...         self.price = price
...     def cost(self):
...         return self.shares * self.price
...
```

在上面的代码中，`__init__` 方法是 Python 类中的一个特殊方法。它被称为构造函数，用于在创建对象时初始化对象的属性。`self` 参数指的是正在创建的类的实例。`cost` 方法通过将股票数量乘以每股价格来计算股票的总成本。

定义类之后，我们可以创建 `SimpleStock` 类的实例。实例是根据类蓝图创建的实际对象。让我们创建两个实例来表示不同的股票：

```python
>>> goog = SimpleStock('GOOG', 100, 490.10)
>>> ibm = SimpleStock('IBM', 50, 91.23)
```

这些实例分别表示 100 股每股价格为 490.10 美元的谷歌股票和 50 股每股价格为 91.23 美元的 IBM 股票。每个实例都有自己的一组属性值。

让我们验证一下我们的实例是否正常工作。你可以通过检查它们的属性并计算它们的成本来完成。这将帮助我们确认类及其方法是否按预期运行。

```python
>>> goog.name
'GOOG'
>>> goog.shares
100
>>> goog.price
490.1
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
```

`cost()` 方法将股票数量乘以每股价格来计算持有这些股票的总成本。通过运行这些命令，我们可以看到实例具有正确的属性值，并且 `cost` 方法能够准确计算成本。
