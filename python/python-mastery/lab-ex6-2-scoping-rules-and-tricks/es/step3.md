# Manipulación de Pila de Llamadas

Una queja sobre la última parte es que la función `__init__()` ahora parece bastante extraña con esa llamada a `locals()` insertada en ella. Sin embargo, puedes evitar eso si estás dispuesto a hacer un poco de manipulación de la pila de llamadas. Prueba esta variante de la función `_init()`:

```python
>>> import sys
>>> def _init():
        locs = sys._getframe(1).f_locals   # Obtener variables locales del llamador
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
>>>
```

En este código, las variables locales se extraen de la pila de llamadas del llamador. Aquí está una definición de clase modificada:

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            _init()

>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>>
```

En este punto, probablemente te estés sintiendo bastante inquieto. Sí, acabas de escribir una función que accedió a la pila de llamadas de otra función y examinó sus variables locales.
