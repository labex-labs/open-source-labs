# `class` 宣言

新しいオブジェクトを定義するには、`class` 宣言を使用します。

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

要するに、クラスは、いわゆる「インスタンス」に対して様々な操作を行う関数のセットです。
