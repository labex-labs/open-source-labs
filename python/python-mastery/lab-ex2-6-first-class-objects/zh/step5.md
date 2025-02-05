# 深度思考

在这个练习中，你编写了两个函数，`read_csv_as_dicts()` 和 `read_csv_as_columns()`。这些函数以相同的方式向用户呈现数据。例如：

```python
>>> data1 = read_csv_as_dicts('ctabus.csv', [str, str, str, int])
>>> len(data1)
577563
>>> data1[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data1[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>

>>> data2 = read_csv_as_columns('ctabus.csv', [str, str, str, int])
>>> len(data2)
577563
>>> data2[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data2[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>
```

实际上，你可以在你编写的 CTA 数据分析代码中使用这两个函数中的任何一个。然而，在底层发生的事情却完全不同。`read_csv_as_columns()` 函数以不同的表示形式存储数据。它依靠 Python 序列协议（魔法方法）以更有用的方式向你呈现信息。

这实际上是“数据抽象”这个更大的编程概念的一部分。在编写程序时，数据的呈现方式通常比数据在底层实际的组合方式更重要。虽然我们将数据呈现为字典序列，但在幕后实际实现的方式有很大的灵活性。这是一个强大的概念，在编写你自己的程序时值得思考。
