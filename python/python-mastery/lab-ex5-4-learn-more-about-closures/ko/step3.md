# 디스크립터를 사용하여 속성 이름 제거

이전 단계에서 타입 속성을 생성할 때 속성 이름을 명시적으로 지정해야 했습니다. 이는 속성 이름이 이미 클래스 정의에 지정되어 있으므로 중복됩니다. 이 단계에서는 디스크립터 (descriptor) 를 사용하여 이러한 중복을 제거합니다.

Python 에서 디스크립터는 속성 접근 방식을 제어하는 특수한 객체입니다. 디스크립터에서 `__set_name__` 메서드를 구현하면 클래스 정의에서 속성 이름을 자동으로 가져올 수 있습니다.

새 파일을 만들어 시작해 보겠습니다.

1. 다음 코드를 사용하여 `improved_typedproperty.py`라는 새 파일을 만듭니다.

```python
# improved_typedproperty.py

class TypedProperty:
    """
    타입 검사를 수행하는 디스크립터입니다.

    이 디스크립터는 클래스 정의에서 속성 이름을 자동으로 캡처합니다.
    """
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        # 이 메서드는 디스크립터가 클래스 속성에 할당될 때 호출됩니다.
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {self.expected_type}')
        instance.__dict__[self.name] = value

# 편의 함수
def String():
    """타입 검사를 사용하여 문자열 속성을 생성합니다."""
    return TypedProperty(str)

def Integer():
    """타입 검사를 사용하여 정수 속성을 생성합니다."""
    return TypedProperty(int)

def Float():
    """타입 검사를 사용하여 부동 소수점 속성을 생성합니다."""
    return TypedProperty(float)
```

이 코드는 속성에 할당된 값의 타입을 확인하는 `TypedProperty`라는 디스크립터 클래스를 정의합니다. `__set_name__` 메서드는 디스크립터가 클래스 속성에 할당될 때 자동으로 호출됩니다. 이를 통해 디스크립터는 속성 이름을 수동으로 지정하지 않고도 캡처할 수 있습니다.

다음으로, 이러한 향상된 타입 속성을 사용하는 클래스를 만들 것입니다.

2. 향상된 타입 속성을 사용하는 `stock_improved.py`라는 새 파일을 만듭니다.

```python
from improved_typedproperty import String, Integer, Float

class Stock:
    """타입 검사된 속성을 가진 주식을 나타내는 클래스입니다."""

    # 더 이상 속성 이름을 지정할 필요가 없습니다.
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

타입 속성을 생성할 때 속성 이름을 지정할 필요가 없다는 점에 유의하십시오. 디스크립터는 클래스 정의에서 자동으로 속성 이름을 가져옵니다.

이제 향상된 클래스를 테스트해 보겠습니다.

3. 향상된 버전을 테스트하기 위해 `test_stock_improved.py`라는 테스트 파일을 만듭니다.

```python
from stock_improved import Stock

# 올바른 타입으로 주식 생성
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# 잘못된 타입으로 속성 설정 시도
try:
    s.name = 123  # Should raise TypeError
    print("Name type check failed")
except TypeError as e:
    print(f"Name type check succeeded: {e}")

try:
    s.shares = "hundred"  # Should raise TypeError
    print("Shares type check failed")
except TypeError as e:
    print(f"Shares type check succeeded: {e}")

try:
    s.price = "490.1"  # Should raise TypeError
    print("Price type check failed")
except TypeError as e:
    print(f"Price type check succeeded: {e}")
```

마지막으로, 모든 것이 예상대로 작동하는지 확인하기 위해 테스트를 실행합니다.

4. 테스트를 실행합니다.

```bash
python3 test_stock_improved.py
```

다음과 유사한 출력을 볼 수 있습니다.

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Name type check succeeded: Expected <class 'str'>
Shares type check succeeded: Expected <class 'int'>
Price type check succeeded: Expected <class 'float'>
```

이 단계에서는 디스크립터와 `__set_name__` 메서드를 사용하여 타입 검사 시스템을 개선했습니다. 이를 통해 중복된 속성 이름 지정을 제거하여 코드를 더 짧게 만들고 오류 발생 가능성을 줄였습니다.

`__set_name__` 메서드는 디스크립터의 매우 유용한 기능입니다. 이를 통해 클래스 정의에서 사용되는 방식에 대한 정보를 자동으로 수집할 수 있습니다. 이를 사용하여 이해하고 사용하기 쉬운 API 를 만들 수 있습니다.
