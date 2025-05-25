# A declaração `class`

Use a declaração `class` para definir um novo objeto.

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

Em poucas palavras, uma classe é um conjunto de funções que realizam várias operações nas chamadas _instâncias_.
