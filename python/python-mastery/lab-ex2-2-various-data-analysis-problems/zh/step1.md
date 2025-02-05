# 准备工作

首先，让我们用一个稍微简单一点的数据集——一个股票投资组合，来回顾一些基础知识。创建一个文件 `readport.py` 并将以下代码放入其中：

```python
# readport.py

import csv

# 一个将文件读取为字典列表的函数
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name' : row[0],
               'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

此文件读取 `portfolio.csv` 文件中的一些简单股票市场数据。使用该函数读取文件并查看结果：

打开一个 Python shell 并尝试以下操作：

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2,'shares': 100},
 {'name': 'IBM', 'price': 91.1,'shares': 50},
 {'name': 'CAT', 'price': 83.44,'shares': 150},
 {'name': 'MSFT', 'price': 51.23,'shares': 200},
 {'name': 'GE', 'price': 40.37,'shares': 95},
 {'name': 'MSFT', 'price': 65.1,'shares': 50},
 {'name': 'IBM', 'price': 70.44,'shares': 100}]
>>>
```

在这些数据中，每行包含股票名称、持有股票数量和购买价格。某些股票名称（如 MSFT 和 IBM）有多个条目。
