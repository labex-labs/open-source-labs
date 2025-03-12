# 使用类方法实现替代构造函数

在这一步中，你将学习如何使用类方法实现一个替代构造函数。这将使你能够以更优雅的方式从 CSV 行数据创建 `Stock` 对象。

## 什么是替代构造函数？

在 Python 中，替代构造函数是一种实用的模式。通常，你使用标准的 `__init__` 方法来创建对象。然而，替代构造函数为你提供了另一种创建对象的方式。类方法非常适合实现替代构造函数，因为它们可以访问类本身。

## 实现 `from_row()` 类方法

你将为 `Stock` 类添加一个类变量 `types` 和一个类方法 `from_row()`。这将简化从 CSV 数据创建 `Stock` 实例的过程。

让我们通过添加高亮代码来修改 `stock.py` 文件：

```python
# stock.py

class Stock:
    types = (str, int, float)  # Type conversions to apply to CSV data

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    @classmethod
    def from_row(cls, row):
        """
        Create a Stock instance from a row of CSV data.

        Args:
            row: A list of strings [name, shares, price]

        Returns:
            A new Stock instance
        """
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

# The rest of the file remains unchanged
```

现在，让我们逐步了解这段代码的工作原理：

1. 你定义了一个类变量 `types`。它是一个包含类型转换函数 `(str, int, float)` 的元组。这些函数将用于将 CSV 行中的数据转换为适当的类型。
2. 你添加了一个类方法 `from_row()`。`@classmethod` 装饰器将此方法标记为类方法。
3. 此方法的第一个参数是 `cls`，它是对类本身的引用。在普通方法中，你使用 `self` 来引用类的实例，但在这里你使用 `cls`，因为这是一个类方法。
4. `zip()` 函数用于将 `types` 中的每个类型转换函数与 `row` 列表中的相应值配对。
5. 你使用列表推导式将每个转换函数应用于 `row` 列表中的相应值。这样，你将 CSV 行中的字符串数据转换为适当的类型。
6. 最后，你使用转换后的值创建一个新的 `Stock` 类实例并返回它。

## 测试替代构造函数

现在，你将创建一个名为 `test_class_method.py` 的新文件来测试新的类方法。这将帮助你验证替代构造函数是否按预期工作。

```python
# test_class_method.py
from stock import Stock

# Test the from_row() class method
row = ['AA', '100', '32.20']
s = Stock.from_row(row)

print(f"Stock: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost()}")

# Try with a different row
row2 = ['GOOG', '50', '1120.50']
s2 = Stock.from_row(row2)

print(f"\nStock: {s2.name}")
print(f"Shares: {s2.shares}")
print(f"Price: {s2.price}")
print(f"Cost: {s2.cost()}")
```

要查看结果，请在终端中运行以下命令：

```bash
cd ~/project
python test_class_method.py
```

你应该会看到类似于以下的输出：

```
Stock: AA
Shares: 100
Price: 32.2
Cost: 3220.0

Stock: GOOG
Shares: 50
Price: 1120.5
Cost: 56025.0
```

请注意，现在你可以直接从字符串数据创建 `Stock` 实例，而无需在类外部手动进行类型转换。这使你的代码更简洁，并确保数据转换的职责在类内部处理。
