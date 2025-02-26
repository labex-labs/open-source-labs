# L'instruction `class`

Utilisez l'instruction `class` pour définir un nouvel objet.

```python
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def damage(self, pts):
        self.health -= pts
```

En résumé, une classe est un ensemble de fonctions qui effectuent diverses opérations sur des soi-disant _instances_.
