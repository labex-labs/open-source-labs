# 重写 Stock 类

既然我们已经有了一个定义良好的 `Structure` 基类，现在是时候重写我们的 `Stock` 类了。通过使用这个基类，我们可以简化代码并使其更有条理。`Structure` 类提供了一组通用功能，我们可以在 `Stock` 类中复用这些功能，这对代码的可维护性和可读性非常有帮助。

## 创建新的 Stock 类

让我们从创建一个名为 `stock.py` 的新文件开始。这个文件将包含我们重写后的 `Stock` 类。以下是你需要放在 `stock.py` 文件中的代码：

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        """
        Calculate the cost as shares * price
        """
        return self.shares * self.price

    def sell(self, nshares):
        """
        Sell a number of shares
        """
        self.shares -= nshares
```

让我们来详细分析这个新的 `Stock` 类的功能：

1. 它继承自 `Structure` 类。这意味着 `Stock` 类可以使用 `Structure` 类提供的所有特性。其中一个好处是，我们不需要自己编写 `__init__` 方法，因为 `Structure` 类会自动处理属性赋值。
2. 我们定义了 `_fields`，它是一个元组，指定了 `Stock` 类的属性。这些属性是 `name`、`shares` 和 `price`。
3. 定义了 `cost` 属性，用于计算股票的总成本。它将 `shares` 的数量乘以 `price`。
4. `sell` 方法用于减少股票的数量。当你调用这个方法并传入要卖出的股票数量时，它会从当前的股票数量中减去该数量。

## 测试新的 Stock 类

为了确保我们的新 `Stock` 类按预期工作，我们需要创建一个测试文件。让我们创建一个名为 `test_stock.py` 的文件，代码如下：

```python
# test_stock.py
from stock import Stock

# Create a stock
s = Stock('GOOG', 100, 490.1)

# Check the attributes
print(f"Stock: {s}")
print(f"Name: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost}")

# Sell some shares
print("\nSelling 20 shares...")
s.sell(20)
print(f"Shares after selling: {s.shares}")
print(f"Cost after selling: {s.cost}")

# Try to set an invalid attribute
print("\nTrying to set an invalid attribute:")
try:
    s.prices = 500  # Invalid attribute (should be 'price')
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

在这个测试文件中，我们首先从 `stock.py` 文件中导入 `Stock` 类。然后，我们创建一个 `Stock` 类的实例，名称为 'GOOG'，有 100 股，价格为 490.1。我们打印出股票的属性，以检查它们是否设置正确。之后，我们卖出 20 股，并打印出新的股票数量和新的成本。最后，我们尝试设置一个无效的属性 `prices`（应该是 `price`）。如果我们的 `Stock` 类工作正常，它应该会引发一个 `AttributeError`。

要运行测试，请打开终端并输入以下命令：

```bash
python3 test_stock.py
```

预期输出如下：

```
Stock: Stock('GOOG', 100, 490.1)
Name: GOOG
Shares: 100
Price: 490.1
Cost: 49010.0

Selling 20 shares...
Shares after selling: 80
Cost after selling: 39208.0

Trying to set an invalid attribute:
Error correctly caught: No attribute prices
```

## 运行单元测试

如果你有之前练习中的单元测试，可以针对新的实现运行这些测试。在终端中输入以下命令：

```bash
python3 teststock.py
```

请注意，有些测试可能会失败。这可能是因为它们期望特定的行为或方法，而我们尚未实现这些。别担心！我们将在未来的练习中继续在此基础上进行构建。

## 回顾我们的进展

让我们花点时间回顾一下到目前为止我们所取得的成果：

1. 我们创建了一个可复用的 `Structure` 基类。这个类：

   - 自动处理属性赋值，这让我们无需编写大量重复的代码。
   - 提供了良好的字符串表示，使打印和调试对象变得更加容易。
   - 限制属性名称以防止错误，这使我们的代码更加健壮。

2. 我们重写了 `Stock` 类。它：
   - 继承自 `Structure` 类以复用通用功能。
   - 仅定义字段和特定领域的方法，这使类的关注点更加集中和简洁。
   - 设计清晰简单，易于理解和维护。

这种方法为我们的代码带来了几个好处：

- 更易于维护，因为重复代码更少。如果我们需要更改通用功能中的某些内容，只需在 `Structure` 类中进行更改。
- 更健壮，因为 `Structure` 类提供了更好的错误检查。
- 更具可读性，因为每个类的职责都很明确。

在未来的练习中，我们将继续在此基础上构建一个更复杂的股票投资组合管理系统。
