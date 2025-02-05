# 上一个实验

在上一个实验中定义的 `Stock` 类的实例通常按如下方式创建：

```python
>>> s = Stock('GOOG', 100, 490.1)
>>>
```

不过，`read_portfolio()` 函数也会根据从文件读取的行数据来创建实例。例如，会使用如下代码：

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> s = Stock(row[0], int(row[1]), float(row[2]))
>>>
```
