# 计算属性的特性

之前，你定义了一个 `Stock` 类。例如：

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>>
```

使用特性将 `cost()` 转换为一个不再需要括号的属性。例如：

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.cost               # 特性。计算成本
49010.0
>>>
```
