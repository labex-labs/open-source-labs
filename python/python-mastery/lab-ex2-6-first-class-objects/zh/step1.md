# 一等数据

在 `portfolio.csv` 文件中，你读取的数据按列组织，如下所示：

```python
"AA",100,32.20
"IBM",50,91.10
...
```

在之前的代码中，通过硬编码所有类型转换来处理这些数据。例如：

```python
rows = csv.reader(f)
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

也可以使用一些列表操作以更巧妙的方式执行这种转换。创建一个 Python 列表，其中包含你要对每列执行的转换：

```python
>>> coltypes = [str, int, float]
>>>
```

你甚至可以创建这个列表的原因是 Python 中的一切都是“一等的”。所以，如果你想要一个函数列表，那也没问题。

现在，从上述文件中读取一行数据：

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

将列类型与行进行拉链操作并查看结果：

```python
>>> r = list(zip(coltypes, row))
>>> r
[(<class'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>,'32.20')]
>>>
```

你会注意到这将类型转换与一个值配对。例如，`int` 与值 `'100'` 配对。现在，试试这个：

```python
>>> record = [func(val) for func, val in zip(coltypes, row)]
>>> record
['AA', 100, 32.2]
>>>
```

确保你理解上述代码中发生的事情。在循环中，`func` 变量是类型转换函数之一（例如，`str`、`int` 等），而 `val` 变量是像 `'AA'`、`'100'` 这样的值之一。表达式 `func(val)` 正在转换一个值（有点像类型转换）。

你可以更进一步，通过使用列标题来创建字典。例如：

```python
>>> dict(zip(headers, record))
{'name': 'AA','shares': 100, 'price': 32.2}
>>>
```

如果你愿意，你可以使用字典推导式一次性执行所有这些步骤：

```python
>>> { name:func(val) for name, func, val in zip(headers, coltypes, row) }
{'name': 'AA','shares': 100, 'price': 32.2}
>>>
```
