# 将方法转换为属性

在 Python 中，属性（property）是一个强大的特性，它允许你以类似于访问属性的方式来访问计算值。通常，当你想从一个方法中获取值时，你需要使用括号来调用该方法。然而，属性消除了对这些括号的需求，使你的代码看起来更简洁，并且与访问普通属性的方式更加一致。

让我们看看当前的 `Stock` 类。它有一个 `cost()` 方法，用于计算股票的总成本。该方法将股票数量乘以每股价格，从而得出总成本。`cost()` 方法如下所示：

```python
def cost(self):
    return self.shares * self.price
```

要使用这个方法获取成本值，我们必须使用括号调用它，如下所示：

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

但我们可以让代码变得更好。通过将 `cost()` 方法转换为属性，我们可以像访问其他属性一样访问成本值，而无需使用括号。转换后的代码如下所示：

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

## 说明：

1. 首先，你需要在编辑器中打开 `stock.py` 文件。`Stock` 类是在这个文件中定义的，我们将对其进行修改。在终端中使用以下命令：

   ```bash
   code /home/labex/project/stock.py
   ```

2. 在 `stock.py` 文件中，你要将 `cost()` 方法替换为属性。你可以使用 `@property` 装饰器来实现这一点。`@property` 装饰器告诉 Python，接下来的方法应被视为属性。将 `cost()` 方法替换为以下代码：

   ```python
   @property
   def cost(self):
       return self.shares * self.price
   ```

3. 完成修改后，保存 `stock.py` 文件。这样可以确保我们的修改被保存下来，以便后续使用。

4. 现在，你需要创建一个简单的 Python 脚本来测试新的属性。使用以下命令在编辑器中打开一个名为 `test_property.py` 的新文件：

   ```bash
   code /home/labex/project/test_property.py
   ```

5. 在 `test_property.py` 文件中，你要添加一些代码来创建一个 `Stock` 实例并访问 `cost` 属性。你应该添加以下代码：

   ```python
   from stock import Stock

   # Create a stock instance
   s = Stock('GOOG', 100, 490.10)

   # Access cost as a property (no parentheses)
   print(f"Stock: {s.name}")
   print(f"Shares: {s.shares}")
   print(f"Price: {s.price}")
   print(f"Cost: {s.cost}")  # Using the property
   ```

6. 最后，运行测试脚本来查看属性是否按预期工作。在终端中使用以下命令：
   ```bash
   python /home/labex/project/test_property.py
   ```

你应该会看到类似于以下的输出：

```
Stock: GOOG
Shares: 100
Price: 490.1
Cost: 49010.0
```

注意，现在我们可以像访问属性一样（无需括号）访问 `cost`，这使得我们的代码在访问属性（如 `name`、`shares` 和 `price`）时更加一致。这让我们的代码更易于阅读和维护。
