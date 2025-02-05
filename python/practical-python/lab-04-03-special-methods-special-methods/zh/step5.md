# 方法调用

调用方法是一个两步过程。

1. 查找：使用 `.` 运算符
2. 方法调用：使用 `()` 运算符

```python
>>> s = stock.Stock('GOOG',100,490.10)
>>> c = s.cost  # 查找
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()         # 方法调用
49010.0
>>>
```
