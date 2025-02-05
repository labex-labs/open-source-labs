# 推导式

列表、集合和字典推导式是处理数据的有用工具。例如，尝试以下操作：

```python
>>> # 找出所有持有量超过100股的股票
>>> [s for s in portfolio if s['shares'] > 100]
[{'name': 'CAT','shares': 150, 'price': 83.44},
 {'name': 'MSFT','shares': 200, 'price': 51.23}]

>>> # 计算总成本（股数 * 价格）
>>> sum([s['shares']*s['price'] for s in portfolio])
44671.15
>>>

>>> # 找出所有唯一的股票名称（集合）
>>> { s['name'] for s in portfolio }
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
>>>

>>> # 计算每种股票的总股数
>>> totals = { s['name']: 0 for s in portfolio }
>>> for s in portfolio:
        totals[s['name']] += s['shares']

>>> totals
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
>>>
```
