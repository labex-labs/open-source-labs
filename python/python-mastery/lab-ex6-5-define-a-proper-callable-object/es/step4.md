# Uso como método (Desafío)

Un objeto llamable personalizado a menudo presenta problemas si se utiliza como un método personalizado. Por ejemplo, prueba esto:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares:Integer):
        self.shares -= nshares
    sell = ValidatedFunction(sell)     # Falla
```

Verás que la función `sell()` envuelta falla miserablemente:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.sell(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 64, in __call__
    bound = self.signature.bind(*args, **kwargs)
  File "/usr/local/lib/python3.6/inspect.py", line 2933, in bind
    return args[0]._bind(args[1:], kwargs)
  File "/usr/local/lib/python3.6/inspect.py", line 2848, in _bind
    raise TypeError(msg) from None
TypeError: missing a required argument: 'nshares'
>>>
```

Bono: Descubre por qué falla, pero no te demores demasiado tiempo en jugar con ello.
