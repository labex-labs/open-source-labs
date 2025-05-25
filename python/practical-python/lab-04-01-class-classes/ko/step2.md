# `class` 문

새로운 객체를 정의하려면 `class` 문을 사용합니다.

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

간단히 말해서, 클래스는 소위 *인스턴스*에 대해 다양한 연산을 수행하는 함수들의 집합입니다.
