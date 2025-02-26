# Verificación de Argumentos de Métodos

¿Recuerdas el decorador `@validated` que escribiste en la última parte? Modifiquemos el decorador `@validate_attributes` para que cualquier método en la clase con anotaciones se envuelva automáticamente con `@validated`. Esto te permite poner anotaciones obligatorias en métodos como el método `sell()`:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Verás que `sell()` ahora fuerza el argumento.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.sell(25)
>>> s.sell(-25)
Traceback (most recent call last):
...
TypeError: Bad Arguments
  nshares: must be >= 0
>>>
```

Sí, esto está empezando a resultar muy interesante ahora. La combinación de un decorador de clase y la herencia es una fuerza poderosa.
