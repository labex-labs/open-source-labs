# 挑战

当你对行程数据进行切片时会发生什么？

```python
>>> r = rows[0:10]
>>> r
...查看结果...
>>>
```

结果可能看起来有点奇怪。你能修改 `RideData` 类，使其生成一个看起来像字典列表的正确切片吗？例如，像这样：

```python
>>> rows = readrides.read_rides_as_columns('ctabus.csv')
>>> rows
<readrides.RideData object at 0x10f5054a8>
>>> len(rows)
577563
>>> r = rows[0:10]
>>> r
<readrides.RideData object at 0x10f5068c8>
>>> len(r)
10
>>> r[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> r[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>
```
