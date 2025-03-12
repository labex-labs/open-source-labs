# 类变量与继承

在这一步中，我们将探讨类变量如何与继承相互作用，以及它们如何作为一种定制机制。在 Python 中，继承允许子类从基类继承属性和方法。类变量是属于类本身的变量，而不是类的任何特定实例。理解它们如何协同工作对于创建灵活且可维护的代码至关重要。

## 继承中的类变量

当子类从基类继承时，它会自动访问基类的类变量。然而，子类可以覆盖这些类变量。通过这样做，子类可以改变其行为而不影响基类。这是一个非常强大的特性，因为它允许你根据特定需求定制子类的行为。

## 创建专门的 Stock 类

让我们创建 `Stock` 类的一个子类。我们将其命名为 `DStock`，代表 Decimal Stock（十进制股票）。`DStock` 与常规 `Stock` 类的主要区别在于，`DStock` 将使用 `Decimal` 类型来表示价格值，而不是 `float`。在金融计算中，精度极其重要，与 `float` 相比，`Decimal` 类型提供了更精确的十进制算术。

要创建这个子类，我们将创建一个名为 `decimal_stock.py` 的新文件。以下是你需要放在该文件中的代码：

```python
# decimal_stock.py
from decimal import Decimal
from stock import Stock

class DStock(Stock):
    """
    A specialized version of Stock that uses Decimal for prices
    """
    types = (str, int, Decimal)  # Override the types class variable

# Test the subclass
if __name__ == "__main__":
    # Create a DStock from row data
    row = ['AA', '100', '32.20']
    ds = DStock.from_row(row)

    print(f"DStock: {ds.name}")
    print(f"Shares: {ds.shares}")
    print(f"Price: {ds.price} (type: {type(ds.price).__name__})")
    print(f"Cost: {ds.cost()} (type: {type(ds.cost()).__name__})")

    # For comparison, create a regular Stock from the same data
    s = Stock.from_row(row)
    print(f"\nRegular Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price} (type: {type(s.price).__name__})")
    print(f"Cost: {s.cost()} (type: {type(s.cost()).__name__})")
```

在你使用上述代码创建了 `decimal_stock.py` 文件后，你需要运行它以查看结果。打开你的终端并按照以下步骤操作：

```bash
cd ~/project
python decimal_stock.py
```

你应该会看到类似于以下的输出：

```
DStock: AA
Shares: 100
Price: 32.20 (type: Decimal)
Cost: 3220.0 (type: Decimal)

Regular Stock: AA
Shares: 100
Price: 32.2 (type: float)
Cost: 3220.0 (type: float)
```

## 关于类变量和继承的关键点

从这个例子中，我们可以得出几个重要的结论：

1. `DStock` 类继承了 `Stock` 类的所有方法，例如 `cost()` 方法，而无需重新定义它们。这是继承的主要优点之一，因为它避免了你编写冗余代码。
2. 只需覆盖 `types` 类变量，我们就改变了创建 `DStock` 新实例时数据的转换方式。这展示了类变量如何用于定制子类的行为。
3. 基类 `Stock` 保持不变，仍然使用 `float` 值。这意味着我们对子类所做的更改不会影响基类，这是一个良好的设计原则。
4. `from_row()` 类方法在 `Stock` 和 `DStock` 类中都能正常工作。这展示了继承的强大之处，因为同一个方法可以用于不同的子类。

这个例子清楚地展示了类变量如何作为一种配置机制。子类可以覆盖这些变量来定制其行为，而无需重写方法。

## 设计讨论

让我们考虑另一种方法，即将类型转换放在 `__init__` 方法中：

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

使用这种方法，我们可以从一行数据创建一个 `Stock` 对象，如下所示：

```python
row = ['AA', '100', '32.20']
s = Stock(*row)
```

虽然这种方法乍一看可能更简单，但它有几个缺点：

1. 它将两个不同的关注点结合在一起：对象初始化和数据转换。这使得代码更难理解和维护。
2. `__init__` 方法变得不那么灵活，因为它总是转换输入，即使它们已经是正确的类型。
3. 它限制了子类定制转换过程的方式。如果转换逻辑嵌入在 `__init__` 方法中，子类将更难改变转换逻辑。
4. 代码变得更脆弱。如果任何转换失败，对象就无法创建，这可能会导致程序出错。

另一方面，类方法方法将这些关注点分开。这使得代码更易于维护和灵活，因为代码的每个部分都有单一的职责。
