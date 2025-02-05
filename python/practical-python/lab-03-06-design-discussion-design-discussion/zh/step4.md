# 练习3.17：从文件名到类文件对象

你现在已经创建了一个名为 `fileparse.py` 的文件，其中包含一个函数 `parse_csv()`。该函数的工作方式如下：

```python
>>> import fileparse
>>> portfolio = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>>
```

目前，该函数期望传入一个文件名。然而，你可以让代码更灵活。修改该函数，使其能与任何类文件/可迭代对象一起工作。例如：

```python
>>> import fileparse
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as file:
...      port = fileparse.parse_csv(file, types=[str,int,float])
...
>>> lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
>>> port = fileparse.parse_csv(lines, types=[str,int,float])
>>>
```

在这段新代码中，如果你像之前那样传入一个文件名会发生什么？

```python
>>> port = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>> port
... 查看输出（应该会很奇怪）...
>>>
```

是的，你需要小心。你能添加一个安全检查来避免这种情况吗？
