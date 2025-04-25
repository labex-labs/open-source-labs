# 类型注释

你还可以向函数定义添加可选的类型提示。

```python
def read_prices(filename: str) -> dict:
    '''
    从包含名称、价格数据的 CSV 文件中读取价格
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

这些提示在操作上没有任何作用。它们纯粹是提供信息的。然而，集成开发环境（IDE）、代码检查器和其他工具可能会利用它们做更多的事情。

在第 2 节中，你编写了一个名为 `report.py` 的程序，它打印出一份显示股票投资组合表现的报告。这个程序由一些函数组成。例如：

```python
# report.py
import csv

def read_portfolio(filename):
    '''
    将股票投资组合文件读入一个字典列表，字典的键为
    name、shares 和 price。
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name' : record['name'],
               'shares' : int(record['shares']),
                'price' : float(record['price'])
            }
            portfolio.append(stock)
    return portfolio
...
```

然而，程序中也有一些部分只是执行了一系列按脚本编写的计算。这段代码出现在程序的末尾附近。例如：

```python
...

# 输出报告

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s'  % headers)
print(('-' * 10 +'') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
...
```

在这个练习中，我们将采用这个程序，并围绕函数的使用对其进行更严格的组织。
