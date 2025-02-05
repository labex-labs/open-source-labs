# 关于灵活性的思考

目前，`reader.py`中的两个函数被硬编码为处理直接传递给`open()`的文件名。重构代码，使其能与任何生成行的可迭代对象一起工作。为此，创建两个新函数`csv_as_dicts(lines, types)`和`csv_as_instances(lines, cls)`，用于转换任何行的可迭代序列。例如：

```python
>>> file = open('portfolio.csv')
>>> port = reader.csv_as_dicts(file, [str, int, float])
>>> port
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1},
 {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23},
 {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1},
 {'name': 'IBM','shares': 100, 'price': 70.44}]
>>>
```

这样做的全部意义在于能够处理不同类型的输入源。例如：

```python
>>> import gzip
>>> import stock
>>> file = gzip.open('portfolio.csv.gz')
>>> port = reader.csv_as_instances(file, stock.Stock)
>>> port
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44),
 Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1),
 Stock('IBM', 100, 70.44)]
>>>
```

为了保持与旧代码的向后兼容性，编写函数`read_csv_as_dicts()`和`read_csv_as_instances()`，它们像以前一样接受文件名。这些函数应该对提供的文件名调用`open()`，并对生成的文件使用新的`csv_as_dicts()`或`csv_as_instances()`函数。
