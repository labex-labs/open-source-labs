# `__init__` et héritage

Si `__init__` est redéfini, il est essentiel d'initialiser le parent.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # Vérifiez l'appel à `super` et `__init__`
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()
```

Vous devriez appeler la méthode `__init__()` sur `super` qui est le moyen d'appeler la version précédente comme montré précédemment.
