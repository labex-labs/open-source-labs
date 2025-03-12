# 理解类变量和类方法

在第一步中，我们将深入探讨 Python 中的类变量和类方法的概念。这些重要的概念将帮助你编写更高效、更有条理的代码。在开始使用类变量和类方法之前，让我们先看看目前是如何创建 `Stock` 类的实例的。这将为我们提供一个基础理解，并让我们知道可以在哪些方面进行改进。

## 什么是类变量？

类变量是 Python 中一种特殊类型的变量。它们由类的所有实例共享。为了更好地理解这一点，让我们将它们与实例变量进行比较。实例变量对于类的每个实例都是唯一的。例如，如果你有一个类的多个实例，每个实例的实例变量都可以有自己的值。另一方面，类变量是在类级别定义的。这意味着该类的所有实例都可以访问并共享类变量的相同值。

## 什么是类方法？

类方法是作用于类本身，而不是类的单个实例的方法。它们与类绑定，这意味着可以直接在类上调用它们，而无需创建实例。在 Python 中定义类方法时，我们使用 `@classmethod` 装饰器。与将实例 (`self`) 作为第一个参数不同，类方法将类 (`cls`) 作为其第一个参数。这使它们能够操作类级别的数据，并执行与整个类相关的操作。

## 当前创建 Stock 实例的方法

让我们首先看看目前是如何创建 `Stock` 类的实例的。在编辑器中打开 `stock.py` 文件，观察当前的实现：

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
```

这个类的实例通常通过以下方式之一创建：

1. 直接用值初始化：

   ```python
   s = Stock('GOOG', 100, 490.1)
   ```

   在这里，我们通过为 `name`、`shares` 和 `price` 属性提供值，直接创建了 `Stock` 类的一个实例。当你事先知道这些值时，这是一种直接创建实例的方法。

2. 从 CSV 文件读取的数据创建：
   ```python
   import csv
   with open('portfolio.csv') as f:
       rows = csv.reader(f)
       headers = next(rows)  # Skip the header
       row = next(rows)      # Get the first data row
       s = Stock(row[0], int(row[1]), float(row[2]))
   ```
   当我们从 CSV 文件中读取数据时，这些值最初是字符串格式。因此，当从 CSV 数据创建 `Stock` 实例时，我们需要手动将字符串值转换为适当的类型。例如，`shares` 值需要转换为整数，`price` 值需要转换为浮点数。

让我们来试试这个。在 `~/project` 目录下创建一个名为 `test_stock.py` 的新 Python 文件，内容如下：

```python
# test_stock.py
from stock import Stock
import csv

# Method 1: Direct creation
s1 = Stock('GOOG', 100, 490.1)
print(f"Stock: {s1.name}, Shares: {s1.shares}, Price: {s1.price}")
print(f"Cost: {s1.cost()}")

# Method 2: Creation from CSV row
with open('portfolio.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Skip the header
    row = next(rows)      # Get the first data row
    s2 = Stock(row[0], int(row[1]), float(row[2]))
    print(f"\nStock from CSV: {s2.name}, Shares: {s2.shares}, Price: {s2.price}")
    print(f"Cost: {s2.cost()}")
```

运行这个文件以查看结果：

```bash
cd ~/project
python test_stock.py
```

你应该会看到类似于以下的输出：

```
Stock: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0

Stock from CSV: AA, Shares: 100, Price: 32.2
Cost: 3220.0
```

这种手动转换方法可行，但有一些缺点。我们需要知道数据的确切格式，并且每次从 CSV 数据创建实例时都必须进行转换。这可能容易出错且耗时。在下一步中，我们将使用类方法创建一个更优雅的解决方案。
