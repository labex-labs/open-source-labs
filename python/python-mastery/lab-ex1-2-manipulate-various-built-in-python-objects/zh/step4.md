# 第4部分：字典

在前面的几个部分中，你只是处理了股票代码。然而，假设你想将股票代码映射到其他数据，比如价格？那就使用字典：

```python
>>> prices = { 'IBM': 91.1, 'GOOG': 490.1, 'AAPL':312.23 }
>>>
```

字典将键映射到值。以下是访问的方法：

```python
>>> prices['IBM']
91.1
>>> prices['IBM'] = 123.45
>>> prices['HPQ'] = 26.15
>>> prices
{'GOOG': 490.1, 'AAPL': 312.23, 'IBM': 123.45, 'HPQ': 26.15}
>>>
```

要获取键的列表，可以这样做：

```python
>>> list(prices)
['GOOG', 'AAPL', 'IBM', 'HPQ']
>>>
```

要删除一个值，使用 `del`

```python
>>> del prices['AAPL']
>>> prices
{'GOOG': 490.1, 'IBM': 123.45, 'HPQ': 26.15}
>>>
```
