# 练习2.6：将字典作为容器

字典是一种很有用的方式，可用于跟踪那些你希望使用整数以外的索引来查找条目的情况。在Python shell中，尝试操作一个字典：

```python
>>> prices = { }
>>> prices['IBM'] = 92.45
>>> prices['MSFT'] = 45.12
>>> prices
... 查看结果...
>>> prices['IBM']
92.45
>>> prices['AAPL']
... 查看结果...
>>> 'AAPL' in prices
False
>>>
```

文件 `prices.csv` 包含一系列股票价格的行。该文件看起来如下所示：

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
"C",3.72
...
```

编写一个函数 `read_prices(filename)`，它将这样一组价格读入一个字典，其中字典的键是股票名称，字典中的值是股票价格。

要做到这一点，从一个空字典开始，然后像上面那样开始向其中插入值。不过，现在你是从文件中读取值。

我们将使用这个数据结构来快速查找给定股票名称的价格。

这部分你需要一些小提示。首先，确保像之前一样使用 `csv` 模块 —— 这里无需重新发明轮子。

```python
>>> import csv
>>> f = open('/home/labex/project/prices.csv', 'r')
>>> rows = csv.reader(f)
>>> for row in rows:
        print(row)


['AA', '9.22']
['AXP', '24.85']
...
[]
>>>
```

另一个小麻烦是 `prices.csv` 文件中可能有一些空行。注意上面数据的最后一行是一个空列表 —— 这意味着该行没有数据。

这有可能导致你的程序因异常而崩溃。使用 `try` 和 `except` 语句来适当地捕获这种情况。思考一下：用 `if` 语句来防范错误数据会不会更好呢？

一旦你编写了 `read_prices()` 函数，通过交互式方式测试它，以确保它能正常工作：

```python
>>> prices = read_prices('/home/labex/project/prices.csv')
>>> prices['IBM']
106.28
>>> prices['MSFT']
20.89
>>>
```
