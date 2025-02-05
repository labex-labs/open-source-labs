# 集合模块

`collections` 模块有各种用于更特殊数据处理的类。例如，最后一个示例可以用 `Counter` 解决，如下所示：

```python
>>> from collections import Counter
>>> totals = Counter()
>>> for s in portfolio:
        totals[s['name']] += s['shares']

>>> totals
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

`Counter` 的有趣之处在于它支持其他类型的操作，比如排序和数学运算。例如：

```python
>>> # 获取持有量最多的两种股票
>>> totals.most_common(2)
[('MSFT', 250), ('IBM', 150)]
>>>

>>> # 将计数器相加
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> more
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})
>>> totals
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>> totals + more
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
>>>
```

`defaultdict` 对象可用于对数据进行分组。例如，假设你想轻松找到给定名称（如 IBM）的所有匹配项。试试这个：

```python
>>> from collections import defaultdict
>>> byname = defaultdict(list)
>>> for s in portfolio:
        byname[s['name']].append(s)

>>> byname['IBM']
[{'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]
>>> byname['AA']
[{'name': 'AA','shares': 100, 'price': 32.2}]
>>>
```

使其起作用的关键特性是 `defaultdict` 会自动为你初始化元素——允许将新元素的插入和 `append()` 操作组合在一起。
