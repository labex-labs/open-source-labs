# Aplicando Decoradores a través de la Herencia

Tener que especificar el decorador de clase en sí mismo es un poco molesto. Modifica la clase `Structure` con el siguiente método `__init_subclass__()`:

```python
# structure.py

class Structure:
 ...
    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

Una vez que hayas hecho este cambio, deberías poder eliminar completamente el decorador y confiar únicamente en la herencia. ¡Es herencia más un poco de magia oculta!

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

    def sell(self, nshares):
        self.shares -= nshares
```

Ahora, el código realmente está empezando a evolucionar. De hecho, casi parece normal. Sigue empujándolo.
