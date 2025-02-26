# Données d'instance

Chaque instance a ses propres données locales.

```python
>>> a.x
2
>>> b.x
10
```

Ces données sont initialisées par `__init__()`.

```python
class Player:
    def __init__(self, x, y):
        # Toute valeur stockée dans `self` est une donnée d'instance
        self.x = x
        self.y = y
        self.health = 100
```

Il n'y a pas de restrictions quant au nombre total ou au type d'attributs stockés.
