# Restringiendo los nombres de atributos

Dale a la clase `Structure` un método `__setattr__()` que restringa el conjunto de atributos permitidos a aquellos enumerados en la variable `_fields`. Sin embargo, todavía debe permitir que se establezcan cualquier atributo "privado" (por ejemplo, nombre que empiece con `_`).

Por ejemplo:

```python
>>> s = Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 13, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>> s._shares = 100     # Atributo privado. Está bien
>>>
```
