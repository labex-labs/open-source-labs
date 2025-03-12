# 增强股票类

在 Python 中，类是组织数据和行为的强大方式。它们允许我们将相关的数据和函数组合在一起。在本节中，我们将通过添加一个显示格式化股票信息的方法来增强我们的 `Stock` 类。这是一个很好的例子，展示了我们如何在类中封装数据和行为。封装意味着将数据与操作该数据的方法捆绑在一起，这有助于使我们的代码更有条理且更易于管理。

1. 首先，你需要在 WebIDE 编辑器中打开 `stock.py` 文件。`stock.py` 文件是我们一直在编写 `Stock` 类的地方。在编辑器中打开它，这样我们就可以对类定义进行修改。

2. 现在，我们将修改 `Stock` 类，添加一个新的 `display()` 方法。这个方法将负责以美观的格式打印出股票信息。以下是具体实现方法：

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def display(self):
        print(f"Stock: {self.name}, Shares: {self.shares}, Price: ${self.price:.2f}, Total Cost: ${self.cost():.2f}")
```

在 `__init__` 方法中，我们初始化了股票的名称、股数和价格。`cost` 方法通过将股数乘以价格来计算股票的总成本。新的 `display` 方法使用 f - 字符串来格式化并打印股票信息，包括名称、股数、价格和总成本。

3. 做出这些更改后，你需要保存文件。你可以通过按下键盘上的 `Ctrl+S` 键，或者点击编辑器中的保存图标来完成保存操作。保存文件可确保你的更改被保留，并且后续可以使用。

4. 接下来，我们将启动一个新的 Python 交互会话。交互会话允许我们立即测试代码。要启动会话，请在终端中运行以下命令：

```bash
python3 -i stock.py
```

`-i` 选项告诉 Python 在执行 `stock.py` 文件后启动一个交互会话。这样，我们就可以立即使用 `Stock` 类及其方法。

5. 现在，让我们创建一个股票对象并使用新的 `display()` 方法。我们将创建一个代表苹果公司股票的对象，然后调用 `display` 方法来查看格式化后的信息。以下是代码：

```python
apple = Stock('AAPL', 200, 154.50)
apple.display()
```

当你在交互会话中运行这段代码时，你将看到以下输出：

```
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

这个输出表明 `display` 方法正常工作，并且按预期格式化了股票信息。

6. 最后，让我们创建一个股票列表并显示所有股票信息。这将展示我们如何对多个股票对象使用 `display` 方法。以下是代码：

```python
stocks = [
    Stock('GOOG', 100, 490.10),
    Stock('IBM', 50, 91.50),
    Stock('AAPL', 200, 154.50)
]

for stock in stocks:
    stock.display()
```

当你运行这段代码时，你将得到以下输出：

```
Stock: GOOG, Shares: 100, Price: $490.10, Total Cost: $49010.00
Stock: IBM, Shares: 50, Price: $91.50, Total Cost: $4575.00
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

通过在类中添加 `display()` 方法，我们将格式化逻辑封装在了类本身中。这使得我们的代码更有条理且更易于维护。如果我们需要更改股票信息的显示方式，我们只需要在一个地方修改 `display` 方法，而不是在整个代码中进行修改。
