# Redéfinition d'une méthode existante

```python
class MyStock(Stock):
    def cost(self):
        return 1.25 * self.shares * self.price
```

Exemple d'utilisation.

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.cost()
61262.5
>>>
```

La nouvelle méthode remplace l'ancienne. Les autres méthodes ne sont pas affectées. C'est formidable.
