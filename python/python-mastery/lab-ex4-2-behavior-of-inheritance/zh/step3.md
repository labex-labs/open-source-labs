# 将验证器应用于股票类

在这一步中，我们将了解我们的验证器在实际场景中是如何工作的。验证器就像是小检查器，确保我们使用的数据符合特定规则。我们将创建一个 `Stock` 类。类就像是创建对象的蓝图。在这种情况下，`Stock` 类将代表股票市场中的一支股票，我们将使用验证器来确保其属性的值（如股票数量和价格）是有效的。

## 创建股票类

首先，我们需要创建一个新文件。在 WebIDE 中，创建一个名为 `stock.py` 的新文件。这个文件将包含我们 `Stock` 类的代码。现在，将以下代码添加到 `stock.py` 文件中：

```python
# stock.py
from validate import PositiveInteger, PositiveFloat

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = PositiveFloat.check(value)

    def cost(self):
        return self.shares * self.price
```

让我们来详细分析这段代码的功能：

1. 我们首先从 `validate` 模块导入 `PositiveInteger` 和 `PositiveFloat` 验证器。这些验证器将帮助我们确保股票数量是正整数，价格是正浮点数。
2. 然后我们定义了一个 `Stock` 类。在类内部，我们有一个 `__init__` 方法。当我们创建一个新的 `Stock` 对象时，会调用这个方法。它接受三个参数：`name`、`shares` 和 `price`，并将它们赋值给对象的属性。
3. 我们使用属性（property）和设置器（setter）来验证 `shares` 和 `price` 的值。属性是一种控制对属性访问的方式，而设置器是当我们尝试设置该属性的值时会调用的方法。当我们设置 `shares` 属性时，会调用 `PositiveInteger.check` 方法，以确保该值是正整数。同样，当我们设置 `price` 属性时，会调用 `PositiveFloat.check` 方法，以确保该值是正浮点数。
4. 最后，我们有一个 `cost` 方法。这个方法通过将股票数量乘以价格来计算股票的总成本。

## 测试股票类

现在我们已经创建了 `Stock` 类，需要对其进行测试，以查看验证器是否正常工作。打开一个新的终端并启动 Python 解释器。你可以通过运行以下命令来实现：

```bash
python3
```

Python 解释器启动后，我们可以导入并测试 `Stock` 类。在 Python 解释器中输入以下代码：

```python
from stock import Stock

# Create a valid stock
s = Stock('GOOG', 100, 490.10)
print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
print(f"Cost: {s.cost()}")

# Try setting an invalid shares value
try:
    s.shares = -10
except ValueError as e:
    print(f"Error setting shares: {e}")

# Try setting an invalid price value
try:
    s.price = "not a price"
except TypeError as e:
    print(f"Error setting price: {e}")
```

运行这段代码时，你应该会看到类似于以下的输出：

```
Name: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0
Error setting shares: Expected >= 0
Error setting price: Expected <class 'float'>
```

这个输出表明我们的验证器按预期工作。`Stock` 类不允许我们为 `shares` 和 `price` 设置无效的值。当我们尝试设置无效值时，会抛出一个错误，我们可以捕获并打印该错误。

## 理解继承的作用

使用我们的验证器的一个优点是，我们可以轻松地组合不同的验证规则。继承是 Python 中一个强大的概念，它允许我们基于现有的类创建新的类。通过多继承，我们可以使用 `super()` 函数调用多个父类的方法。

例如，如果我们想确保股票名称不为空，可以按照以下步骤操作：

1. 从 `validate` 模块导入 `NonEmptyString` 验证器。这个验证器将帮助我们检查股票名称是否不是空字符串。
2. 在 `Stock` 类中为 `name` 属性添加一个属性设置器。这个设置器将使用 `NonEmptyString.check()` 方法来验证股票名称。

这展示了继承，特别是结合 `super()` 函数的多继承，如何让我们构建灵活且可通过不同组合方式复用的组件。

测试完成后，你可以运行以下命令退出 Python 解释器：

```python
exit()
```
