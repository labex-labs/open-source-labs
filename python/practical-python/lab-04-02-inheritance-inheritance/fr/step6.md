# Redéfinition avec appel à la méthode originale

Parfois, une classe étend une méthode existante, mais elle veut utiliser l'implémentation originale à l'intérieur de la redéfinition. Pour ce faire, utilisez `super()` :

```python
class Stock:
  ...
    def cost(self):
        return self.shares * self.price
  ...

class MyStock(Stock):
    def cost(self):
        # Vérifiez l'appel à `super`
        actual_cost = super().cost()
        return 1.25 * actual_cost
```

Utilisez `super()` pour appeler la version précédente.

_Avertissement : En Python 2, la syntaxe était plus verbeuse._

```python
actual_cost = super(MyStock, self).cost()
```
