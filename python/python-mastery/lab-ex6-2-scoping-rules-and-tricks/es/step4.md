# Combinando Todo

Tomando las ideas de las dos primeras partes, elimina el método `__init__()` que originalmente era parte de la clase `Structure`. A continuación, agrega un método `_init()` como este:

```python
# structure.py
import sys

class Structure:
  ...
    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
  ...
```

Nota: La razón por la cual esto se define como un `@staticmethod` es que el argumento `self` se obtiene de los locales, no es necesario que se le pase adicionalmente como argumento al método en sí (es cierto que esto es un poco sutil).

Ahora, modifica tu clase `Stock` de modo que se vea como la siguiente:

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name','shares','price')
    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= shares
```

Verifica que la clase funcione correctamente, soporte argumentos con palabras clave y tenga una firma de ayuda adecuada.

```python
>>> s = Stock(name='GOOG', price=490.1, shares=50)
>>> s.name
'GOOG'
>>> s.shares
50
>>> s.price
490.1
>>> help(Stock)
... mira la salida...
>>>
```

Ejecuta tus pruebas unitarias en `teststock.py` nuevamente. Deberías ver que al menos una prueba más pasa. ¡Hurra!

En este punto, puede parecer que acabamos de dar un gran paso atrás. No solo las clases necesitan el método `__init__()`, también necesitan la variable `_fields` para que algunos de los otros métodos funcionen (`__repr__()` y `__setattr__()`). Además, el uso de `self._init()` parece bastante chapucero. Trabajaremos en esto, pero sé paciente.
