# 练习2.21：数据查询

尝试以下各种数据查询示例。

首先，列出所有持有股份超过100股的投资组合。

```python
>>> more100 = [ s for s in portfolio if s['shares'] > 100 ]
>>> more100
[{'price': 83.44, 'name': 'CAT','shares': 150}, {'price': 51.23, 'name': 'MSFT','shares': 200}]
>>>
```

所有持有微软（MSFT）和IBM股票的投资组合。

```python
>>> msftibm = [ s for s in portfolio if s['name'] in {'MSFT', 'IBM'} ]
>>> msftibm
[{'price': 91.1, 'name': 'IBM','shares': 50}, {'price': 51.23, 'name': 'MSFT','shares': 200},
  {'price': 65.1, 'name': 'MSFT','shares': 50}, {'price': 70.44, 'name': 'IBM','shares': 100}]
>>>
```

列出所有成本超过10000美元的投资组合。

```python
>>> cost10k = [ s for s in portfolio if s['shares'] * s['price'] > 10000 ]
>>> cost10k
[{'price': 83.44, 'name': 'CAT','shares': 150}, {'price': 51.23, 'name': 'MSFT','shares': 200}]
>>>
```
