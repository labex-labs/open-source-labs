# 使用列表、集合和字典推导式

Python 推导式是一种非常实用且简洁的方式，用于基于现有的集合创建新的集合。Python 中的集合可以是列表、集合或字典，它们就像容器一样，用于存储不同类型的数据。推导式允许你过滤掉某些数据、以某种方式转换数据，并更高效地组织数据。在这部分，我们将使用投资组合数据来探索这些推导式的工作原理。

首先，你需要打开一个 Python 终端，就像你在上一步中所做的那样。终端打开后，你将逐个输入以下示例。这种实践方法将帮助你理解推导式在实际中的工作方式。

## 列表推导式

列表推导式是 Python 中的一种特殊语法，用于创建新的列表。它通过对现有集合中的每个元素应用一个表达式来实现这一点。

让我们从一个示例开始。首先，我们将导入一个函数来读取我们的投资组合数据。然后，我们将使用列表推导式从投资组合中过滤出某些持仓。

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

# Find all holdings with more than 100 shares
>>> large_holdings = [s for s in portfolio if s['shares'] > 100]
>>> print(large_holdings)
[{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}]
```

在这段代码中，我们首先导入 `read_portfolio` 函数，并使用它从 CSV 文件中读取投资组合数据。然后，列表推导式 `[s for s in portfolio if s['shares'] > 100]` 遍历 `portfolio` 集合中的每个元素 `s`。只有当该持仓的股票数量大于 100 时，才会将元素 `s` 包含在新列表 `large_holdings` 中。

列表推导式还可用于执行计算。以下是一些示例：

```python
# Calculate the total cost of each holding (shares * price)
>>> holding_costs = [s['shares'] * s['price'] for s in portfolio]
>>> print(holding_costs)
[3220.0, 4555.0, 12516.0, 10246.0, 3835.15, 3255.0, 7044.0]

# Calculate the total cost of the entire portfolio
>>> total_portfolio_cost = sum([s['shares'] * s['price'] for s in portfolio])
>>> print(total_portfolio_cost)
44671.15
```

在第一个示例中，列表推导式 `[s['shares'] * s['price'] for s in portfolio]` 通过将 `portfolio` 中每个元素的股票数量乘以价格，计算出每个持仓的总成本。在第二个示例中，我们结合使用 `sum` 函数和列表推导式来计算整个投资组合的总成本。

## 集合推导式

集合推导式用于从现有集合创建一个集合。集合是一种只包含唯一值的集合。

让我们看看它在我们的投资组合数据中是如何工作的：

```python
# Find all unique stock names
>>> unique_stocks = {s['name'] for s in portfolio}
>>> print(unique_stocks)
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
```

在这段代码中，集合推导式 `{s['name'] for s in portfolio}` 遍历 `portfolio` 中的每个元素 `s`，并将股票名称 (`s['name']`) 添加到集合 `unique_stocks` 中。由于集合只存储唯一值，因此我们最终得到了投资组合中所有不同股票的列表，且没有重复项。

## 字典推导式

字典推导式通过应用表达式来创建键值对，从而创建一个新的字典。

以下是一个使用字典推导式计算投资组合中每只股票总股数的示例：

```python
# Create a dictionary to count total shares for each stock
>>> totals = {s['name']: 0 for s in portfolio}
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
```

在第一行中，字典推导式 `{s['name']: 0 for s in portfolio}` 创建了一个字典，其中每个股票名称 (`s['name']`) 是一个键，每个键的初始值为 0。然后，我们使用一个 `for` 循环遍历 `portfolio` 中的每个元素。对于每个元素，我们将股票数量 (`s['shares']`) 添加到 `totals` 字典中相应键的值上。

这些推导式非常强大，因为它们允许你仅用几行代码就可以转换和分析数据。它们是你 Python 编程工具包中的一个很棒的工具。
