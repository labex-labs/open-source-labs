# 상속 (Inheritance) 사용하기

상속은 때때로 관련 객체를 구성하는 데 사용됩니다.

```python
class Shape:
    ...

class Circle(Shape):
    ...

class Rectangle(Shape):
    ...
```

논리적 계층 구조 또는 분류 체계를 생각해 보세요. 그러나 더 일반적이고 실용적인 사용법은 재사용 가능하거나 확장 가능한 코드를 만드는 것과 관련이 있습니다. 예를 들어, 프레임워크는 기본 클래스를 정의하고 이를 사용자 정의하도록 지시할 수 있습니다.

```python
class CustomHandler(TCPHandler):
    def handle_request(self):
        ...
        # Custom processing
```

기본 클래스에는 몇 가지 범용 코드가 포함되어 있습니다. 사용자의 클래스는 특정 부분을 상속받아 사용자 정의합니다.
