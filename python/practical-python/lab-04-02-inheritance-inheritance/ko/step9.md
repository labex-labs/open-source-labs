# "is a" 관계

상속은 타입 관계를 설정합니다.

```python
class Shape:
    ...

class Circle(Shape):
    ...
```

객체 인스턴스를 확인합니다.

```python
>>> c = Circle(4.0)
>>> isinstance(c, Shape)
True
>>>
```

_중요: 이상적으로, 부모 클래스의 인스턴스로 작동하는 모든 코드는 자식 클래스의 인스턴스로도 작동합니다._
