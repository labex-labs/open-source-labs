# 练习 7.11：类方法的实际应用

在你的 `report.py` 和 `portfolio.py` 文件中，创建一个 `Portfolio` 对象的过程有点混乱。例如，`report.py` 程序有这样的代码：

```python
def read_portfolio(filename, **opts):
    '''
    将股票投资组合文件读入一个字典列表，字典的键为
    name、shares 和 price。
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

    portfolio = [ Stock(**d) for d in portdicts ]
    return Portfolio(portfolio)
```

而 `portfolio.py` 文件定义 `Portfolio()` 时使用了一个奇怪的初始化器，如下所示：

```python
class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings
  ...
```

坦率地说，责任链有点混乱，因为代码很分散。如果一个 `Portfolio` 类应该包含一个 `Stock` 实例列表，也许你应该把这个类改得更清晰一些。像这样：

```python
# portfolio.py

import stock

class Portfolio:
    def __init__(self):
        self._holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self._holdings.append(holding)
  ...
```

如果你想从 CSV 文件中读取一个投资组合，也许你应该为它创建一个类方法：

```python
# portfolio.py

import fileparse
import stock

class Portfolio:
    def __init__(self):
        self._holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self._holdings.append(holding)

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

        for d in portdicts:
            self.append(stock.Stock(**d))

        return self
```

要使用这个新的 `Portfolio` 类，你现在可以编写如下代码：

```python
>>> from portfolio import Portfolio
>>> with open('portfolio.csv') as lines:
...     port = Portfolio.from_csv(lines)
...
>>>
```

对 `Portfolio` 类进行这些更改，并修改 `report.py` 代码以使用类方法。
