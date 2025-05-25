# 클래스 스코핑 (Class Scoping)

클래스는 이름의 스코프를 정의하지 않습니다.

```python
class Player:
    ...
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def left(self, amt):
        move(-amt, 0)       # NO. 전역 `move` 함수를 호출합니다.
        self.move(-amt, 0)  # YES. 위의 메서드 `move` 를 호출합니다.
```

인스턴스에 대해 작업을 수행하려면 항상 명시적으로 참조해야 합니다 (예: `self`).

이 일련의 연습부터 이전 섹션의 기존 코드에 일련의 변경 사항을 적용하기 시작합니다. 시작하려면 Exercise 3.18 의 작동하는 버전이 있는 것이 중요합니다. 그렇지 않은 경우, `Solutions/3_18` 디렉토리에서 찾을 수 있는 솔루션 코드를 사용하십시오. 복사해도 괜찮습니다.
