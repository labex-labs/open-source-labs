# Descriptor 를 사용하여 유효성 검사 구현

이 단계에서는 descriptor 를 사용하여 유효성 검사 시스템을 만들 것입니다. 하지만 먼저 descriptor 가 무엇인지, 그리고 왜 사용하는지 이해해 보겠습니다. Descriptor 는 `__get__`, `__set__`, 또는 `__delete__` 메서드를 포함하는 descriptor 프로토콜을 구현하는 Python 객체입니다. 이를 통해 객체에서 속성에 접근, 설정 또는 삭제하는 방식을 사용자 정의할 수 있습니다. 이 경우, descriptor 를 사용하여 데이터 무결성을 보장하는 유효성 검사 시스템을 만들 것입니다. 이는 객체에 저장된 데이터가 특정 유형이거나 양수 값과 같은 특정 기준을 항상 충족함을 의미합니다.

이제 유효성 검사 시스템을 만들기 시작해 보겠습니다. 프로젝트 디렉토리에 `validate.py`라는 새 파일을 생성합니다. 이 파일에는 유효성 검사기를 구현하는 클래스가 포함됩니다.

```python
# validate.py

class Validator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class String(Validator):
    expected_type = str

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return value


class PositiveInteger(Validator):
    expected_type = int

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        if value < 0:
            raise ValueError('Expected a positive value')
        return value


class PositiveFloat(Validator):
    expected_type = float

    @classmethod
    def check(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        return float(value)
```

`validate.py` 파일에서 먼저 `Validator`라는 기본 클래스를 정의합니다. 이 클래스에는 유효성 검사 중인 속성을 식별하는 데 사용될 `name` 매개변수를 사용하는 `__init__` 메서드가 있습니다. `check` 메서드는 단순히 전달된 값을 반환하는 클래스 메서드입니다. `__set__` 메서드는 속성이 객체에 설정될 때 호출되는 descriptor 메서드입니다. `check` 메서드를 호출하여 값을 검증한 다음 검증된 값을 객체의 사전에 저장합니다.

그런 다음 `Validator`의 세 가지 하위 클래스인 `String`, `PositiveInteger`, 그리고 `PositiveFloat`를 정의합니다. 이러한 각 하위 클래스는 특정 유효성 검사를 수행하기 위해 `check` 메서드를 재정의합니다. `String` 클래스는 값이 문자열인지 확인하고, `PositiveInteger` 클래스는 값이 양의 정수인지 확인하며, `PositiveFloat` 클래스는 값이 양의 숫자 (정수 또는 부동 소수점) 인지 확인합니다.

이제 유효성 검사기가 정의되었으므로, 이러한 유효성 검사기를 사용하도록 `Stock` 클래스를 수정해 보겠습니다. `stock_with_validators.py`라는 새 파일을 생성하고 `validate.py` 파일에서 유효성 검사기를 가져옵니다.

```python
# stock_with_validators.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String('name')
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

`stock_with_validators.py` 파일에서 `Stock` 클래스를 정의하고 유효성 검사기를 클래스 속성으로 사용합니다. 즉, 속성이 `Stock` 객체에 설정될 때마다 해당 유효성 검사기의 `__set__` 메서드가 호출되어 값을 검증합니다. `__init__` 메서드는 `Stock` 객체의 속성을 초기화하고, `cost`, `sell`, 그리고 `__repr__` 메서드는 추가 기능을 제공합니다.

이제 유효성 검사기 기반의 `Stock` 클래스를 테스트해 보겠습니다. 터미널을 열고 프로젝트 디렉토리로 이동하여 `stock_with_validators.py` 파일을 대화형 모드로 실행합니다.

```bash
cd ~/project
python3 -i stock_with_validators.py
```

Python 인터프리터가 실행되면 몇 가지 명령을 사용하여 유효성 검사 시스템을 테스트할 수 있습니다.

```python
# Create a stock with valid values
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing to valid values
s.shares = 75
print(s.shares)  # Should return 75

# Try setting invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error setting shares to string: {e}")

try:
    s.shares = -50  # Should raise ValueError
except ValueError as e:
    print(f"Error setting negative shares: {e}")

exit()
```

테스트 코드에서 먼저 유효한 값으로 `Stock` 객체를 생성하고 해당 속성을 인쇄하여 올바르게 설정되었는지 확인합니다. 그런 다음 `shares` 속성을 유효한 값으로 변경하고 다시 인쇄하여 변경 사항을 확인합니다. 마지막으로, `shares` 속성을 유효하지 않은 값 (문자열 및 음수) 으로 설정하고 유효성 검사기에 의해 발생한 예외를 catch 합니다.

이제 코드가 훨씬 더 깔끔해졌음을 알 수 있습니다. `Stock` 클래스는 더 이상 모든 property 메서드를 구현할 필요가 없으며, 유효성 검사기가 모든 유형 검사 및 제약을 처리합니다.

Descriptor 를 사용하면 모든 클래스 속성에 적용할 수 있는 재사용 가능한 유효성 검사 시스템을 만들 수 있었습니다. 이는 애플리케이션 전체에서 데이터 무결성을 유지하기 위한 강력한 패턴입니다.
