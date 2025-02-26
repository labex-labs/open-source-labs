# Las tres operaciones

Todo el sistema de objetos de Python se compone solo de tres operaciones principales: la obtención, la asignación y la eliminación de atributos. Normalmente, se acceden a través del punto (.) de la siguiente manera:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name    #  obtener
'GOOG'
>>> s.shares = 50    # asignar
>>> del s.shares     # eliminar
>>>
```

Las tres operaciones también están disponibles como funciones. Por ejemplo:

```python
>>> getattr(s, 'name')            # Lo mismo que s.name
'GOOG'
>>> setattr(s,'shares', 50)      # Lo mismo que s.shares = 50
>>> delattr(s,'shares')          # Lo mismo que del s.shares
>>>
```

Una función adicional, `hasattr()`, se puede utilizar para comprobar si un objeto tiene un atributo:

```python
>>> hasattr(s, 'name')
True
>>> hasattr(s, 'blah')
False
>>>
```
