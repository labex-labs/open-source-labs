# Modificando Instancias

Las operaciones que modifican un objeto actualizan el diccionario subyacente.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{ 'name':'GOOG','shares': 100, 'price': 490.1 }
>>> s.shares = 50       # Estableciendo
>>> s.date = '6/7/2007' # Estableciendo
>>> s.__dict__
{ 'name': 'GOOG','shares': 50, 'price': 490.1, 'date': '6/7/2007' }
>>> del s.shares        # Eliminando
>>> s.__dict__
{ 'name': 'GOOG', 'price': 490.1, 'date': '6/7/2007' }
>>>
```
