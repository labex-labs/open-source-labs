# Corrigiendo los Nombres

Una cosa molesta de los descriptores es la especificación redundante de nombres. Por ejemplo:

```python
class Stock:
  ...
    shares = PositiveInteger('shares')
  ...
```

Podemos arreglar eso. Cambia la clase `Validator` de nivel superior para que incluya un método `__set_name__()` de la siguiente manera:

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
```

Ahora, intenta reescribir tu clase `Stock` para que se vea así:

```python
class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

Ah, mucho mejor. Ten en cuenta que esta capacidad de establecer el nombre es una característica de Python 3.6. No funcionará en versiones anteriores.
