# 练习2.4：元组列表

文件 `portfolio.csv` 包含了一个投资组合中的股票列表。在练习1.30中，你编写了一个函数 `portfolio_cost(filename)`，它读取这个文件并进行了一个简单的计算。

你的代码应该类似于以下这样：

```python
# pcost.py

import csv

def portfolio_cost(filename):
    '''计算投资组合文件的总成本（股数 * 价格）'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost
```

以这段代码为大致指导，创建一个新文件 `report.py`。在那个文件中，定义一个函数 `read_portfolio(filename)`，它打开给定的投资组合文件并将其读入一个元组列表中。为此，你需要对上述代码做一些小的修改。

首先，不是定义 `total_cost = 0`，而是创建一个最初设置为空列表的变量。例如：

```python
portfolio = []
```

接下来，不是计算成本总和，而是像你在上一个练习中那样将每一行转换为一个元组，并将其追加到这个列表中。例如：

```python
for row in rows:
    holding = (row[0], int(row[1]), float(row[2]))
    portfolio.append(holding)
```

最后，返回生成的 `portfolio` 列表。

通过交互式方式试验你的函数（提醒一下，要这样做，你首先必须在解释器中运行 `report.py` 程序）：

_提示：在终端中执行文件时使用 `-i`_

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> portfolio
[('AA', 100, 32.2), ('IBM', 50, 91.1), ('CAT', 150, 83.44), ('MSFT', 200, 51.23),
    ('GE', 95, 40.37), ('MSFT', 50, 65.1), ('IBM', 100, 70.44)]
>>>
>>> portfolio[0]
('AA', 100, 32.2)
>>> portfolio[1]
('IBM', 50, 91.1)
>>> portfolio[1][1]
50
>>> total = 0.0
>>> for s in portfolio:
        total += s[1] * s[2]

>>> print(total)
44671.15
>>>
```

你创建的这个元组列表与二维数组非常相似。例如，你可以使用类似 `portfolio[row][column]` 的查找方式来访问特定的行和列，其中 `row` 和 `column` 是整数。

也就是说，你也可以使用这样的语句重写最后一个 `for` 循环：

```python
>>> total = 0.0
>>> for name, shares, price in portfolio:
            total += shares*price

>>> print(total)
44671.15
>>>
```
