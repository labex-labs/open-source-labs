# Empezando de nuevo

Crea un nuevo archivo `stock.py` (o borra todo tu código anterior). Empieza de nuevo definiendo `Stock` de la siguiente manera:

```python
# stock.py

from structure import Structure

class Stock(Structure):
    _fields = ('name','shares', 'price')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Una vez que hayas hecho esto, ejecuta tus pruebas unitarias de `teststock.py`. Deberías obtener muchos fallos, pero al menos algunos de los tests deberían pasar.
