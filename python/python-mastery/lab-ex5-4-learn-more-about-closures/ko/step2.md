# 코드 생성기로서의 클로저

이 단계에서는 클로저를 사용하여 동적으로 코드를 생성하는 방법을 배우겠습니다. 특히, 클로저를 사용하여 클래스 속성에 대한 타입 검사 시스템을 구축할 것입니다.

먼저, 클로저가 무엇인지 이해해 보겠습니다. 클로저는 메모리에 존재하지 않더라도 외부 범위 (enclosing scope) 의 값을 기억하는 함수 객체입니다. Python 에서 클로저는 중첩된 함수가 외부 함수의 값을 참조할 때 생성됩니다.

이제 타입 검사 시스템을 구현하기 시작해 보겠습니다.

1. `/home/labex/project` 디렉토리에 다음 코드를 사용하여 `typedproperty.py`라는 새 파일을 만듭니다.

```python
# typedproperty.py

def typedproperty(name, expected_type):
    """
    타입 검사를 사용하여 속성을 생성합니다.

    인수:
        name: 속성의 이름
        expected_type: 속성 값의 예상 타입

    반환값:
        타입 검사를 수행하는 속성 객체
    """
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value
```

이 코드에서 `typedproperty` 함수는 클로저입니다. `name`과 `expected_type`의 두 인수를 받습니다. `@property` 데코레이터는 개인 속성의 값을 검색하는 속성에 대한 getter 메서드를 생성하는 데 사용됩니다. `@value.setter` 데코레이터는 설정되는 값이 예상 타입인지 확인하는 setter 메서드를 생성합니다. 그렇지 않으면 `TypeError`를 발생시킵니다.

2. 이제 이러한 타입 속성을 사용하는 클래스를 만들어 보겠습니다. 다음 코드를 사용하여 `stock.py`라는 파일을 만듭니다.

```python
from typedproperty import typedproperty

class Stock:
    """타입 검사된 속성을 가진 주식을 나타내는 클래스입니다."""

    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

`Stock` 클래스에서 `typedproperty` 함수를 사용하여 `name`, `shares`, 및 `price`에 대한 타입 검사된 속성을 생성합니다. `Stock` 클래스의 인스턴스를 생성하면 타입 검사가 자동으로 적용됩니다.

3. 이 동작을 확인하기 위해 테스트 파일을 만들어 보겠습니다. 다음 코드를 사용하여 `test_stock.py`라는 파일을 만듭니다.

```python
from stock import Stock

# 올바른 타입으로 주식 생성
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# 잘못된 타입으로 속성을 설정하려고 시도
try:
    s.shares = "hundred"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

이 테스트 파일에서 먼저 올바른 타입으로 `Stock` 객체를 생성합니다. 그런 다음 `shares` 속성을 문자열로 설정하려고 시도합니다. 예상 타입이 정수이므로 `TypeError`가 발생해야 합니다.

4. 테스트 파일을 실행합니다.

```bash
python3 test_stock.py
```

다음과 유사한 출력을 볼 수 있습니다.

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'int'>
```

이 출력은 타입 검사가 올바르게 작동하고 있음을 보여줍니다.

5. 이제 일반적인 타입에 대한 편의 함수를 추가하여 `typedproperty.py`를 향상시켜 보겠습니다. 파일 끝에 다음 코드를 추가합니다.

```python
def String(name):
    """타입 검사를 사용하여 문자열 속성을 생성합니다."""
    return typedproperty(name, str)

def Integer(name):
    """타입 검사를 사용하여 정수 속성을 생성합니다."""
    return typedproperty(name, int)

def Float(name):
    """타입 검사를 사용하여 부동 소수점 속성을 생성합니다."""
    return typedproperty(name, float)
```

이러한 함수는 `typedproperty` 함수를 래핑하여 일반적인 타입의 속성을 더 쉽게 생성할 수 있도록 합니다.

6. 이러한 편의 함수를 사용하는 `stock_enhanced.py`라는 새 파일을 만듭니다.

```python
from typedproperty import String, Integer, Float

class Stock:
    """타입 검사된 속성을 가진 주식을 나타내는 클래스입니다."""

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

이 `Stock` 클래스는 편의 함수를 사용하여 타입 검사된 속성을 생성하므로 코드를 더 읽기 쉽게 만듭니다.

7. 향상된 버전을 테스트하기 위해 `test_stock_enhanced.py`라는 테스트 파일을 만듭니다.

```python
from stock_enhanced import Stock

# 올바른 타입으로 주식 생성
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# 잘못된 타입으로 속성을 설정하려고 시도
try:
    s.price = "490.1"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

이 테스트 파일은 이전 파일과 유사하지만 향상된 `Stock` 클래스를 테스트합니다.

8. 테스트를 실행합니다.

```bash
python3 test_stock_enhanced.py
```

다음과 유사한 출력을 볼 수 있습니다.

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'float'>
```

이 단계에서는 클로저를 사용하여 코드를 생성하는 방법을 시연했습니다. `typedproperty` 함수는 타입 검사를 수행하는 속성 객체를 생성하고, `String`, `Integer`, 및 `Float` 함수는 일반적인 타입에 대한 특수화된 속성을 생성합니다.
