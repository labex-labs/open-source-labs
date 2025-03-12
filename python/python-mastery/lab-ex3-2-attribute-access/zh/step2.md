# 使用 `getattr()` 进行通用对象处理

`getattr()` 函数是 Python 中的一个强大工具，它允许你以动态方式访问对象的属性。当你想以通用方式处理对象时，这尤其有用。你可以使用 `getattr()` 处理任何具有所需属性的对象，而不是编写特定于某一对象类型的代码。这种灵活性使你的代码更具可复用性和适应性。

## 处理多个属性

让我们先学习如何使用 `getattr()` 函数访问对象的多个属性。当你需要从对象中提取特定信息时，这是一种常见的场景。

首先，如果你关闭了之前的 Python 交互式 shell，请重新打开它。你可以在终端中运行以下命令来实现：

```python
# Open a Python interactive shell if you closed the previous one
python3
```

接下来，我们将导入 `Stock` 类并创建一个 `Stock` 对象。`Stock` 类表示一支股票，具有 `name`、`shares` 和 `price` 等属性。

```python
# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.1)
```

现在，我们将定义一个要访问的属性名列表。这个列表将帮助我们遍历这些属性并打印它们的值。

```python
# Define a list of attribute names
fields = ['name', 'shares', 'price']
```

最后，我们将使用 `for` 循环遍历属性名列表，并使用 `getattr()` 访问每个属性。每次迭代时，我们将打印属性名及其值。

```python
# Access each attribute using getattr()
for name in fields:
    print(f"{name}: {getattr(s, 'name')}" if name == 'name' else f"{name}: {getattr(s, name)}")
```

运行这段代码时，你将看到以下输出：

```
name: GOOG
shares: 100
price: 490.1
```

这个输出表明，我们能够使用 `getattr()` 函数访问并打印 `Stock` 对象的多个属性的值。

## `getattr()` 的默认值

`getattr()` 函数还提供了一个有用的特性：当你尝试访问的属性不存在时，你可以指定一个默认值。这可以防止你的代码引发 `AttributeError`，使代码更加健壮。

让我们看看这是如何工作的。首先，我们将尝试访问 `Stock` 对象中不存在的属性。我们将使用 `getattr()` 并提供一个默认值 `'N/A'`。

```python
# Try to access an attribute that doesn't exist
print(getattr(s, 'symbol', 'N/A'))  # Output: 'N/A'
```

在这种情况下，由于 `Stock` 对象中不存在 `symbol` 属性，`getattr()` 返回默认值 `'N/A'`。

现在，让我们将其与访问现有属性进行比较。我们将访问 `Stock` 对象中确实存在的 `name` 属性。

```python
# Compare with an existing attribute
print(getattr(s, 'name', 'N/A'))    # Output: 'GOOG'
```

在这里，`getattr()` 返回 `name` 属性的实际值，即 `'GOOG'`。

## 处理对象集合

当你需要处理对象集合时，`getattr()` 函数会变得更加强大。让我们看看如何使用它来处理股票投资组合。

首先，我们将从 `stock` 模块导入 `read_portfolio` 函数。这个函数从 CSV 文件中读取股票投资组合，并返回一个 `Stock` 对象列表。

```python
# Import the portfolio reading function
from stock import read_portfolio
```

接下来，我们将使用 `read_portfolio` 函数从名为 `portfolio.csv` 的 CSV 文件中读取投资组合。

```python
# Read the portfolio from CSV file
portfolio = read_portfolio('portfolio.csv')
```

最后，我们将使用 `for` 循环遍历投资组合中的 `Stock` 对象列表。对于每支股票，我们将使用 `getattr()` 访问 `name` 和 `shares` 属性并打印它们的值。

```python
# Print the name and shares of each stock
for stock in portfolio:
    print(f"Stock: {getattr(stock, 'name')}, Shares: {getattr(stock, 'shares')}")
```

这种方法使你的代码更具灵活性，因为你可以将属性名作为字符串处理。这些字符串可以作为参数传递或存储在数据结构中，这样你就可以轻松更改要访问的属性，而无需修改代码的核心逻辑。
