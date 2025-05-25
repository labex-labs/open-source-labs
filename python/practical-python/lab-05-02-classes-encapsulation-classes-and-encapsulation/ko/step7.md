# 프로퍼티 (Properties)

이전 패턴에 대한 대안적인 접근 방식이 있습니다.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
```

이제 일반적인 속성 접근은 `@property` 및 `@shares.setter` 아래에서 getter 및 setter 메서드를 트리거합니다.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares         # Triggers @property
50
>>> s.shares = 75    # Triggers @shares.setter
>>>
```

이 패턴을 사용하면 소스 코드에 _변경 사항이 필요하지 않습니다_. 새로운 *setter*는 `__init__()` 메서드 내부를 포함하여 클래스 내에서 할당이 있을 때도 호출됩니다.

```python
class Stock:
    def __init__(self, name, shares, price):
        ...
        # This assignment calls the setter below
        self.shares = shares
        ...

    ...
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
```

프로퍼티와 private 이름 사용 사이에는 종종 혼란이 있습니다. 프로퍼티는 내부적으로 `_shares`와 같은 private 이름을 사용하지만, 클래스의 나머지 부분 (프로퍼티가 아닌 부분) 은 `shares`와 같은 이름을 계속 사용할 수 있습니다.

프로퍼티는 계산된 데이터 속성에도 유용합니다.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
    ...
```

이를 통해 추가 괄호를 없애고 실제로는 메서드라는 사실을 숨길 수 있습니다.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares # Instance variable
100
>>> s.cost   # Computed Value
49010.0
>>>
```
