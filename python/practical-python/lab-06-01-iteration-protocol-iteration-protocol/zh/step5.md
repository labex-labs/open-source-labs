# 练习6.2：支持迭代

有时，你可能希望自己的某个对象支持迭代——特别是当你的对象围绕现有列表或其他可迭代对象进行包装时。在一个新文件 `portfolio.py` 中，定义以下类：

```python
# portfolio.py

class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
```

这个类旨在作为围绕列表的一层包装，但带有一些额外的方法，比如 `total_cost` 属性。修改 `report.py` 中的 `read_portfolio()` 函数，使其像这样创建一个 `Portfolio` 实例：

    # report.py

...

    import fileparse
    from stock import Stock
    from portfolio import Portfolio

    def read_portfolio(filename):
        '''
        将股票投资组合文件读取为一个字典列表，字典的键为
        name、shares 和 price。
        '''
        with open(filename) as file:
            portdicts = fileparse.parse_csv(file,
                                            select=['name','shares','price'],
                                            types=[str,int,float])

        portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
        return Portfolio(portfolio)

...

尝试运行 `report.py` 程序。你会发现它会因 `Portfolio` 实例不可迭代而严重失败。

```python
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... 崩溃...
```

通过修改 `Portfolio` 类以支持迭代来修复此问题：

```python
class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    @property
    def total_cost(self):
        return sum([s.shares*s.price for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
```

做出此更改后，你的 `report.py` 程序应该能再次正常工作。与此同时，修改你的 `pcost.py` 程序以使用新的 `Portfolio` 对象。如下所示：

```python
# pcost.py

import report

def portfolio_cost(filename):
    '''
    计算投资组合文件的总成本（股数 * 价格）
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
...
```

进行测试以确保其正常工作：

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>>
```
