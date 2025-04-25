# 练习 2.23：从 CSV 文件中提取数据

了解如何使用列表、集合和字典推导式的各种组合在各种形式的数据处理中可能会很有用。下面是一个示例，展示了如何从 CSV 文件中提取选定的列。

首先，从 CSV 文件中读取一行标题信息：

```python
>>> import csv
>>> f = open('portfoliodate.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'date', 'time','shares', 'price']
>>>
```

接下来，定义一个变量，列出你实际关心的列：

```python
>>> select = ['name','shares', 'price']
>>>
```

现在，在源 CSV 文件中找到上述列的索引：

```python
>>> indices = [ headers.index(colname) for colname in select ]
>>> indices
[0, 3, 4]
>>>
```

最后，读取一行数据，并使用字典推导式将其转换为字典：

```python
>>> row = next(rows)
>>> record = { colname: row[index] for colname, index in zip(select, indices) }   # dict-comprehension
>>> record
{'price': '32.20', 'name': 'AA','shares': '100'}
>>>
```

如果你对刚才发生的事情感觉很熟悉了，那就读取文件的其余部分：

```python
>>> portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
>>> portfolio
[{'price': '91.10', 'name': 'IBM','shares': '50'}, {'price': '83.44', 'name': 'CAT','shares': '150'},
  {'price': '51.23', 'name': 'MSFT','shares': '200'}, {'price': '40.37', 'name': 'GE','shares': '95'},
  {'price': '65.10', 'name': 'MSFT','shares': '50'}, {'price': '70.44', 'name': 'IBM','shares': '100'}]
>>>
```

哇哦，你刚刚把 `read_portfolio()` 函数的大部分内容简化为了一条语句。
