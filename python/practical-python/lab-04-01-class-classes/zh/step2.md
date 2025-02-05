# `class` 语句

使用 `class` 语句来定义一个新对象。

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

简而言之，一个类是一组对所谓的“实例”执行各种操作的函数。
