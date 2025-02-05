# 练习5.7：属性与设置器

修改`shares`属性，使其值存储在一个私有属性中，并使用一对属性函数来确保它始终被设置为整数值。以下是预期行为的示例：

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG',100,490.10)
>>> s.shares = 50
>>> s.shares = 'a lot'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: expected an integer
>>>
```
