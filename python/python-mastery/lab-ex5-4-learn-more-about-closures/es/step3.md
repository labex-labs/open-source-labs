# Desafío: eliminando nombres

Modifica el código de `typedproperty.py` de modo que ya no sea necesario los nombres de atributos:

```python
from typedproperty import String, Integer, Float

class Stock:
    name = String()
    shares = Integer()
    price = Float()
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Pista: Para hacer esto, recuerda el método `__set_name__()` de los objetos descriptor que se llama cuando los descriptores se colocan en una definición de clase.
