# Usando Decoradores de Clase para Completar Detalles

Un aspecto molesto del código anterior es que hay detalles adicionales como la variable `_fields` y el último paso de `Stock.create_init()`. Gran parte de esto podría empaquetarse en un decorador de clase en lugar de eso.

En el archivo `structure.py`, crea un decorador de clase `@validate_attributes` que examine el cuerpo de la clase en busca de instancias de Validators y complete la variable `_fields`. Por ejemplo:

```python
# structure.py

from validate import Validator

def validate_attributes(cls):
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
    cls._fields = [val.name for val in validators]
    return cls
```

Este código se basa en el hecho de que los diccionarios de clase están ordenados a partir de Python 3.6. Por lo tanto, encontrará los diferentes descriptores `Validator` en el orden en que se enumeran. Usando este orden, luego puede completar la variable `_fields`. Esto le permite escribir código como este:

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
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

Una vez que tengas esto funcionando, modifica el decorador `@validate_attributes` para realizar adicionalmente el último paso de llamar a `Stock.create_init()`. Esto reducirá la clase a la siguiente:

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
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
