# 为什么使用字典？

当存在 _许多_ 不同的值，并且这些值可能需要修改或操作时，字典就很有用。字典能让你的代码更具可读性。

```python
s['price']
# 对比
s[2]
```

在前几个练习中，你编写了一个程序来读取数据文件 `portfolio.csv`。使用 `csv` 模块，可以很容易地逐行读取文件。

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> next(rows)
['name','shares', 'price']
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

虽然读取文件很容易，但你通常希望对数据进行更多操作，而不仅仅是读取它。例如，也许你想存储它并开始对其进行一些计算。不幸的是，原始的“行”数据不足以让你进行操作。例如，即使是简单的数学计算也无法进行：

```python
>>> row = ['AA', '100', '32.20']
>>> cost = row[1] * row[2]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type'str'
>>>
```

为了进行更多操作，你通常需要以某种方式解释原始数据，并将其转换为更有用的对象类型，以便稍后使用。两个简单的选择是元组或字典。
