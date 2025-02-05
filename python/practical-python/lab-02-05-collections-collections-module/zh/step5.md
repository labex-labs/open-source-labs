# 练习2.18：使用计数器制表

假设你想要统计每只股票的总股数。使用 `Counter` 对象很容易做到这一点。试试看：

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> from collections import Counter
>>> holdings = Counter()
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

仔细观察 `portfolio` 中 `MSFT` 和 `IBM` 的多个条目在这里是如何合并为一个条目的。

你可以像使用字典一样使用计数器来获取单个值：

```python
>>> holdings['IBM']
150
>>> holdings['MSFT']
250
>>>
```

如果你想对这些值进行排序，可以这样做：

```python
>>> # 获取持有量最多的三只股票
>>> holdings.most_common(3)
[('MSFT', 250), ('IBM', 150), ('CAT', 150)]
>>>
```

让我们获取另一个股票投资组合并创建一个新的计数器：

```python
>>> portfolio2 = read_portfolio('portfolio2.csv')
>>> holdings2 = Counter()
>>> for s in portfolio2:
          holdings2[s['name']] += s['shares']

>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>>
```

最后，让我们通过一个简单的操作将所有持有量合并起来：

```python
>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>> combined = holdings + holdings2
>>> combined
Counter({'MSFT': 275, 'HPQ': 250, 'GE': 220, 'AA': 150, 'IBM': 150, 'CAT': 150})
>>>
```

这只是计数器功能的一小部分。然而，如果你发现自己需要对值进行制表，你应该考虑使用它。
