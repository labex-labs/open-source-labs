# Atributos administrados

Un enfoque: introducir métodos accesores.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.set_shares(shares)
        self.price = price

    # Función que implementa la operación "get"
    def get_shares(self):
        return self._shares

    # Función que implementa la operación "set"
    def set_shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Se esperaba un int')
        self._shares = value
```

Qué lástima que esto rompa todo nuestro código existente. `s.shares = 50` se convierte en `s.set_shares(50)`
