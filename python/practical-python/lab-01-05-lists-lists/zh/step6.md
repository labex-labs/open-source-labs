# 列表与数学运算

**注意：列表并非为数学运算而设计。**

```python
>>> nums = [1, 2, 3, 4, 5]
>>> nums * 2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> nums + [10, 11, 12, 13, 14]
[1, 2, 3, 4, 5, 10, 11, 12, 13, 14]
```

具体来说，列表并不像在MATLAB、Octave、R等语言中那样表示向量/矩阵。不过，有一些包可以帮助你进行相关操作（例如 [numpy](https://numpy.org)）。

在本实验中，我们将探索Python的列表数据类型。在上一部分中，你处理过包含股票代码的字符串。

```python
>>> symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
```

使用字符串的 `split()` 操作将其拆分为一个名称列表：

```python
>>> symlist = symbols.split(',')
```
