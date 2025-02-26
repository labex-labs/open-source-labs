# Ключевое слово `class`

Используйте ключевое слово `class` для определения нового объекта.

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

Вкратце, класс - это набор функций, которые выполняют различные операции над так называемыми _экземплярами_.
