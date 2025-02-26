# 属性名の制限

`Structure` クラスに `__setattr__()` メソッドを与え、許可される属性のセットを `_fields` 変数にリストされているものに制限します。ただし、「プライベート」属性（たとえば、`_` で始まる名前）は設定可能なままでなければなりません。

たとえば：

```python
>>> s = Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 13, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>> s._shares = 100     # プライベート属性。OK
>>>
```
