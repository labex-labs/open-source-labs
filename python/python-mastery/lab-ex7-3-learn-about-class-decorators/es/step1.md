# Repaso de los Descriptores

En el Ejercicio 4.3 definiste algunos descriptores que permitían a un usuario definir clases con atributos con comprobación de tipo como este:

```python
from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()
 ...
```

Modifica tu clase `Stock` para que incluya los descriptores anteriores y ahora se vea así (ver Ejercicio 6.4):

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name','shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

Stock.create_init()
```

Ejecuta las pruebas unitarias en `teststock.py`. Deberías ver que una gran cantidad de pruebas pasan con la adición de la comprobación de tipo. Excelente.
