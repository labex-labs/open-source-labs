# 限制属性名称

为`Structure`类添加一个`__setattr__()`方法，将允许设置的属性限制为`_fields`变量中列出的那些。不过，它仍应允许设置任何“私有”属性（例如，以`_`开头的名称）。

例如：

```python
>>> s = Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 13, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>> s._shares = 100     # 私有属性。可以
>>>
```
