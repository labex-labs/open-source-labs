# 在 `Structure` 类中实现高级初始化

我们刚刚学习了两种强大的访问函数参数的技术。现在，我们将使用这些技术来更新我们的 `Structure` 类。首先，让我们了解一下为什么要这样做。这些技术将使我们的类更加灵活，更易于使用，特别是在处理不同类型的参数时。

在代码编辑器中打开 `structure.py` 文件。你可以在终端中运行以下命令来完成此操作。`cd` 命令用于将目录更改为项目文件夹，`code` 命令用于在代码编辑器中打开 `structure.py` 文件。

```bash
cd ~/project
code structure.py
```

将文件内容替换为以下代码。这段代码定义了一个包含多个方法的 `Structure` 类。让我们逐部分分析，了解它的功能。

```python
import sys

class Structure:
    _fields = ()

    @staticmethod
    def _init():
        # Get the caller's frame (the __init__ method that called this)
        frame = sys._getframe(1)

        # Get the local variables from that frame
        locs = frame.f_locals

        # Extract self and set other variables as attributes
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({values})'

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'{type(self).__name__!r} has no attribute {name!r}')
```

以下是我们在代码中所做的操作：

1. 我们移除了旧的 `__init__()` 方法。由于子类将定义自己的 `__init__` 方法，因此我们不再需要旧的方法。
2. 我们添加了一个新的 `_init()` 静态方法。此方法使用帧检查（frame inspection）自动捕获所有参数并将其设置为属性。帧检查允许我们访问调用方法的局部变量。
3. 我们保留了 `__repr__()` 方法。此方法为对象提供了一个良好的字符串表示形式，这对于调试和打印非常有用。
4. 我们添加了一个 `__setattr__()` 方法。此方法执行属性验证，确保只能为对象设置有效的属性。

现在，让我们更新 `Stock` 类。使用以下命令打开 `stock.py` 文件：

```bash
code stock.py
```

将其内容替换为以下代码：

```python
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()  # This magically captures and sets all parameters!

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

这里的关键更改是，我们的 `__init__` 方法现在调用 `self._init()`，而不是手动设置每个属性。`_init()` 方法使用帧检查自动捕获所有参数并将其设置为属性。这使得代码更加简洁，更易于维护。

让我们通过运行单元测试来测试我们的实现。单元测试将帮助我们确保代码按预期工作。在终端中运行以下命令：

```bash
cd ~/project
python3 teststock.py
```

你应该会看到所有测试都通过了，包括之前失败的关键字参数测试。这意味着我们的实现是正确的。

让我们还查看一下 `Stock` 类的帮助文档。帮助文档提供了有关类及其方法的信息。在终端中运行以下命令：

```bash
python3 -c "from stock import Stock; help(Stock)"
```

现在你应该会看到 `__init__` 方法的正确签名，显示所有参数名称。这使得其他开发人员更容易理解如何使用该类。

最后，让我们交互式地测试关键字参数是否按预期工作。在终端中运行以下命令：

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

你应该会看到 `Stock` 对象已使用指定的属性正确创建。这证实了我们的类初始化系统支持关键字参数。

通过这种实现，我们实现了一个更加灵活、用户友好的类初始化系统，它：

1. 在文档中保留了正确的函数签名，使开发人员更容易理解如何使用该类。
2. 支持位置参数和关键字参数，在创建对象时提供了更多的灵活性。
3. 减少了子类中的样板代码，减少了你需要编写的代码量。
