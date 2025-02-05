# 特别挑战项目

在练习 2.5 中，我们创建了一个 `RideData` 类，它将所有公交数据存储在列中，但实际上以字典序列的形式向用户呈现数据。通过各种神奇的方式，它节省了大量内存。

你能将这个想法进行泛化吗？具体来说，你能创建一个通用函数 `read_csv_as_columns()`，使其按如下方式工作吗：

```python
>>> data = read_csv_as_columns('ctabus.csv', types=[str, str, str, int])
>>> data
<__main__.DataCollection object at 0x102b45048>
>>> len(data)
577563
>>> data[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>> data[2]
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
>>>
```

这个函数应该是通用的 —— 你可以给它任何文件和列类型列表，它将读取数据。数据被读入一个 `DataCollection` 类，该类在内部将数据存储为列。然而，当访问数据时，它会以字典序列的形式呈现。

尝试在最后一部分中使用字符串实习技巧来使用这个函数。现在存储所有行程数据需要多少内存？你还能在早期的 CTA 分析代码中使用这个函数吗？

## 注意：

在 `colreader.py` 文件中完成 `read_csv_as_columns()` 函数。
