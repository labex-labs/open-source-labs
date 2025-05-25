# 인스턴스 메서드 (Instance Methods)

인스턴스 메서드는 객체의 인스턴스에 적용되는 함수입니다.

```python
class Player:
    ...
    # `move` 는 메서드입니다.
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

객체 자체는 항상 첫 번째 인수로 전달됩니다.

```python
>>> a.move(1, 2)

# `a` 를 `self` 에 매칭
# `1` 을 `dx` 에 매칭
# `2` 를 `dy` 에 매칭
def move(self, dx, dy):
```

관례적으로, 인스턴스는 `self`라고 불립니다. 하지만 실제로 사용되는 이름은 중요하지 않습니다. 객체는 항상 첫 번째 인수로 전달됩니다. 이 인수를 `self`라고 부르는 것은 단지 파이썬 프로그래밍 스타일일 뿐입니다.
