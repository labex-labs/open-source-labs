# 练习2.22：数据提取

展示如何构建一个元组列表 `(name, shares)`，其中 `name` 和 `shares` 取自 `portfolio`。

```python
>>> name_shares =[ (s['name'], s['shares']) for s in portfolio ]
>>> name_shares
[('AA', 100), ('IBM', 50), ('CAT', 150), ('MSFT', 200), ('GE', 95), ('MSFT', 50), ('IBM', 100)]
>>>
```

如果你将方括号 (`[`, `]`) 改为花括号 (`{`, `}`)，你将得到所谓的集合推导式。这会给你唯一或不同的值。

例如，这可以确定 `portfolio` 中出现的唯一股票名称集合：

```python
>>> names = { s['name'] for s in portfolio }
>>> names
{ 'AA', 'GE', 'IBM', 'MSFT', 'CAT' }
>>>
```

如果你指定 `键:值` 对，就可以构建一个字典。例如，创建一个将股票名称映射到所持股票总数的字典。

```python
>>> holdings = { name: 0 for name in names }
>>> holdings
{'AA': 0, 'GE': 0, 'IBM': 0, 'MSFT': 0, 'CAT': 0}
>>>
```

后一个特性称为 **字典推导式**。让我们列表如下：

```python
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
{ 'AA': 100, 'GE': 95, 'IBM': 150, 'MSFT':250, 'CAT': 150 }
>>>
```

尝试这个示例，它将 `prices` 字典过滤为只包含 `portfolio` 中出现的那些名称：

```python
>>> portfolio_prices = { name: prices[name] for name in names }
>>> portfolio_prices
{'AA': 9.22, 'GE': 13.48, 'IBM': 106.28, 'MSFT': 20.89, 'CAT': 35.46}
>>>
```
