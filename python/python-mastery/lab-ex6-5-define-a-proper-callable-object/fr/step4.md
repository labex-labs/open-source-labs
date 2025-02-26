# Utilisation comme une méthode (Défi)

Un appelable personnalisé peut souvent poser des problèmes s'il est utilisé comme une méthode personnalisée. Par exemple, essayez ceci :

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
    sell = ValidatedFunction(sell)     # Fails
```

Vous constaterez que l'enveloppement de `sell()` échoue lamentablement :

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

Bonus : Trouvez pourquoi cela échoue - mais ne passez pas trop de temps à vous amuser avec ça.
