# Agregando `__slots__`

Modifica tu nueva clase `Stock` para utilizar `__slots__`. Verás que tendrás que utilizar un conjunto diferente de nombres de atributos que antes - específicamente, tendrás que listar los nombres de los atributos privados (por ejemplo, si una propiedad está almacenando un valor en un atributo `_shares`, ese es el nombre que listas en `__slots__`). Verifica que la clase siga funcionando y que ya no puedas agregar nuevos atributos.

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.spam = 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Stock' object has no attribute 'spam'
>>>
```
