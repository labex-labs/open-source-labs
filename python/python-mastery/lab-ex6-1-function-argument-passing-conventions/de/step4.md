# Einschränkung der Attributnamen

Geben Sie der `Structure`-Klasse eine `__setattr__()`-Methode, die die erlaubten Attribute auf die in der `_fields`-Variable aufgeführten beschränkt. Es sollte jedoch immer noch beliebige "private" Attribute (z.B. Namen, die mit `_` beginnen) setzen können.

Beispielsweise:

```python
>>> s = Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 13, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>> s._shares = 100     # Private attribute. OK
>>>
```
