# 实施验证规则

使用特性和私有属性，修改 `Stock` 类的 `shares` 属性，使其只能被赋一个非负整数值。此外，修改 `price` 属性，使其只能被赋一个非负浮点数值。

除了额外的类型和值检查外，新对象的工作方式应与旧对象几乎完全相同。

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.shares = 50          # 可以
>>> s.shares = '50'
Traceback (最近一次调用最后):
...
TypeError: 期望整数
>>> s.shares = -10
Traceback (最近一次调用最后):
...
ValueError: shares 必须 >= 0

>>> s.price = 123.45       # 可以
>>> s.price = '123.45'
Traceback (最近一次调用最后):
...
TypeError: 期望浮点数
>>> s.price = -10.0
Traceback (最近一次调用最后):
...
ValueError: price 必须 >= 0
>>>
```
