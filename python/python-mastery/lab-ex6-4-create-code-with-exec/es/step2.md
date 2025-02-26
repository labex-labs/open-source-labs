# Creando una función `__init__()`

En el Ejercicio 6.3, escribió código que inspeccionó la firma del método `__init__()` para establecer los nombres de atributo en una variable de clase `_fields`. Por ejemplo:

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

Stock.set_fields()
```

En lugar de inspeccionar el método `__init__()`, escriba un método de clase `create_init(cls)` que cree un método `__init__()` a partir del valor de `_fields`. Utilice la función `exec()` para hacer esto como se muestra anteriormente. Aquí está cómo un usuario la utilizará:

```python
class Stock(Structure):
    _fields = ('name','shares', 'price')

Stock.create_init()
```

La clase resultante debería funcionar exactamente de la misma manera que antes:

```python
>>> s = Stock(name='GOOG', shares=100, price=490.1)
>>> s
Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 12, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>>
```

Modifique la clase `Stock` en desarrollo para utilizar la función `create_init()` como se muestra. Verifíquelo con sus pruebas unitarias como antes.

Mientras está en eso, elimine los métodos `_init()` y `set_fields()` de la clase `Structure`; ese enfoque era un poco extraño.
