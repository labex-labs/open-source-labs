# 练习 2.26：整体概览

运用本练习中的技巧，你可以编写语句，轻松地将几乎任何按列组织的数据文件中的字段转换为 Python 字典。

为了说明这一点，假设你从另一个数据文件中读取数据，如下所示：

```python
>>> f = open('dowstocks.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> headers
['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
>>> row
['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']
>>>
```

让我们使用类似的技巧来转换这些字段：

```python
>>> types = [str, float, str, str, float, float, float, float, int]
>>> converted = [func(val) for func, val in zip(types, row)]
>>> record = dict(zip(headers, converted))
>>> record
{'volume': 181800, 'name': 'AA', 'price': 39.48, 'high': 39.69,
'low': 39.45, 'time': '9:36am', 'date': '6/11/2007', 'open': 39.67,
'change': -0.18}
>>> record['name']
'AA'
>>> record['price']
39.48
>>>
```

额外挑战：你将如何修改这个示例，以额外地将 `date` 条目解析为类似 `(6, 11, 2007)` 这样的元组？

花些时间思考你在这个练习中所做的事情。我们稍后会再次探讨这些概念。
