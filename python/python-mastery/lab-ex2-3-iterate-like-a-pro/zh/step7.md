# 节省大量内存

在练习2.1中，你编写了一个函数 `read_rides_as_dicts()`，它将芝加哥交通管理局（CTA）的公交数据读取到一个字典列表中。使用这个函数需要大量内存。例如，让我们找出22路公交车载客量最大的日期：

```python
>>> import tracemalloc
>>> tracemalloc.start()
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('ctabus.csv')
>>> rt22 = [row for row in rows if row['route'] == '22']
>>> max(rt22, key=lambda row: row['rides'])
{'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
>>> tracemalloc.get_traced_memory()
... 查看结果。应该在220MB左右
>>>
```

现在，让我们尝试一个涉及生成器的例子。重启Python并尝试这个：

```python
>>> # RESTART
>>> import tracemalloc
>>> tracemalloc.start()
>>> import csv
>>> f = open('ctabus.csv')
>>> f_csv = csv.reader(f)
>>> headers = next(f_csv)
>>> rows = (dict(zip(headers,row)) for row in f_csv)
>>> rt22 = (row for row in rows if row['route'] == '22')
>>> max(rt22, key=lambda row: int(row['rides']))
{'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
>>> tracemalloc.get_traced_memory()
... 查看结果。应该比之前小很多
>>>
```

请记住，你刚刚处理了整个数据集，就好像它是作为一个字典序列存储的一样。然而，你实际上并没有创建和存储一个字典列表。并非所有问题都能以这种方式构建，但如果你能以迭代的方式处理数据，生成器表达式可以节省大量内存。
