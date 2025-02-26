# Die `class`-Anweisung

Verwenden Sie die `class`-Anweisung, um ein neues Objekt zu definieren.

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

Kurz gesagt ist eine Klasse eine Menge von Funktionen, die verschiedene Operationen auf sogenannten _Instanzen_ ausführen.
