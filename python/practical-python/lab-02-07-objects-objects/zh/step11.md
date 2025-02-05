# 练习 2.24：一等公民数据

在文件 `portfolio.csv` 中，我们读取的数据按列组织，如下所示：

```csv
name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
```

在之前的代码中，我们使用 `csv` 模块读取文件，但仍需手动进行类型转换。例如：

```python
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

这种转换也可以使用一些列表基本操作以更巧妙的方式完成。

创建一个 Python 列表，其中包含用于将每列转换为适当类型的转换函数名称：

```python
>>> types = [str, int, float]
>>>
```

你之所以能够创建这个列表，是因为 Python 中的一切都是 _一等公民_。所以，如果你想创建一个函数列表，没问题。你创建的列表中的元素是用于将值 `x` 转换为给定类型的函数（例如，`str(x)`、`int(x)`、`float(x)`）。

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

如前所述，这一行数据无法用于计算，因为类型不对。例如：

```python
>>> row[1] * row[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>>
```

不过，也许可以将数据与你在 `types` 中指定的类型进行配对。例如：

```python
>>> types[1]
<type 'int'>
>>> row[1]
'100'
>>>
```

尝试转换其中一个值：

```python
>>> types[1](row[1])     # 等同于 int(row[1])
100
>>>
```

尝试转换另一个值：

```python
>>> types[2](row[2])     # 等同于 float(row[2])
32.2
>>>
```

尝试使用转换后的值进行计算：

```python
>>> types[1](row[1])*types[2](row[2])
3220.0000000000005
>>>
```

将列类型与字段进行 `zip` 操作并查看结果：

```python
>>> r = list(zip(types, row))
>>> r
[(<type 'str'>, 'AA'), (<type 'int'>, '100'), (<type 'float'>,'32.20')]
>>>
```

你会注意到，这将类型转换与值进行了配对。例如，`int` 与值 `'100'` 配对。

如果你想依次对所有值进行转换，这个 `zip` 后的列表会很有用。试试这个：

```python
>>> converted = []
>>> for func, val in zip(types, row):
          converted.append(func(val))
...
>>> converted
['AA', 100, 32.2]
>>> converted[1] * converted[2]
3220.0000000000005
>>>
```

确保你理解上述代码中发生了什么。在循环中，`func` 变量是类型转换函数之一（例如，`str`、`int` 等），`val` 变量是像 `'AA'`、`'100'` 这样的值。表达式 `func(val)` 正在转换一个值（有点像类型转换）。

上述代码可以压缩成一个单行的列表推导式。

```python
>>> converted = [func(val) for func, val in zip(types, row)]
>>> converted
['AA', 100, 32.2]
>>>
```
