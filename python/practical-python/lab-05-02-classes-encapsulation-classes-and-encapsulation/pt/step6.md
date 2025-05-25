# Atributos Gerenciados

Uma abordagem: introduzir métodos acessores (accessor methods).

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.set_shares(shares)
        self.price = price

    # Function that layers the "get" operation
    def get_shares(self):
        return self._shares

    # Function that layers the "set" operation
    def set_shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value
```

É uma pena que isso quebre todo o nosso código existente. `s.shares = 50` torna-se `s.set_shares(50)`
