# Muéstrame tus variables locales

Primero, intenta un experimento definiendo la siguiente clase:

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            print(locals())

>>>
```

Ahora, intenta ejecutar esto:

```python
>>> s = Stock('GOOG', 100, 490.1)
{'self': <__main__.Stock object at 0x100699b00>, 'price': 490.1, 'name': 'GOOG','shares': 100}
>>>
```

Observa cómo el diccionario de variables locales contiene todos los argumentos pasados a `__init__()`. Eso es interesante. Ahora, define las siguientes definiciones de función y clase:

```python
>>> def _init(locs):
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

>>> class Stock:
        def __init__(self, name, shares, price):
            _init(locals())
```

En este código, la función `_init()` se utiliza para inicializar automáticamente un objeto a partir de un diccionario de variables locales pasadas. Verás que `help(Stock)` y los argumentos con palabras clave funcionan perfectamente.

```python
>>> s = Stock(name='GOOG', price=490.1, shares=50)
>>> s.name
'GOOG'
>>> s.shares
50
>>> s.price
490.1
>>>
```
