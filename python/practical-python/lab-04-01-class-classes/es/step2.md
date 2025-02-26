# La declaración `class`

Utiliza la declaración `class` para definir un nuevo objeto.

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

En resumen, una clase es un conjunto de funciones que realizan diversas operaciones sobre los llamados _instancias_.
