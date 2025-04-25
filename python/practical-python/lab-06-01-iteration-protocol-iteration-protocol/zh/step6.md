# 练习 6.3：创建一个更合适的容器

如果要创建一个容器类，你通常需要做的不仅仅是支持迭代。修改 `Portfolio` 类，使其具有一些其他特殊方法，如下所示：

```python
class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any([s.name == name for s in self._holdings])

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

现在，使用这个新类进行一些实验：

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> len(portfolio)
7
>>> portfolio[0]
Stock('AA', 100, 32.2)
>>> portfolio[1]
Stock('IBM', 50, 91.1)
>>> portfolio[0:3]
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44)]
>>> 'IBM' in portfolio
True
>>> 'AAPL' in portfolio
False
>>>
```

关于这一点有一个重要的观察结果——一般来说，如果代码使用了 Python 其他部分通常使用的通用词汇，那么它就被认为是“Pythonic”的。对于容器对象来说，支持迭代、索引、包含性检查以及其他类型的操作符是其中的一个重要部分。
