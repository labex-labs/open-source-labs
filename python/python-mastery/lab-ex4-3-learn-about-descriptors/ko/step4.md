# Descriptor 구현 개선

이 단계에서는 descriptor 구현을 개선할 것입니다. 경우에 따라 이름을 중복해서 지정해 왔다는 것을 눈치챘을 수 있습니다. 이는 코드를 약간 지저분하게 만들고 유지 관리를 더 어렵게 만들 수 있습니다. 이 문제를 해결하기 위해 Python 3.6 에서 도입된 유용한 기능인 `__set_name__` 메서드를 사용합니다.

`__set_name__` 메서드는 클래스가 정의될 때 자동으로 호출됩니다. 주요 역할은 descriptor 의 이름을 설정하는 것이므로 매번 수동으로 수행할 필요가 없습니다. 이렇게 하면 코드가 더 깔끔하고 효율적으로 됩니다.

이제 `__set_name__` 메서드를 포함하도록 `validate.py` 파일을 업데이트해 보겠습니다. 업데이트된 코드는 다음과 같습니다.

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        # This gets called when the class is defined
        # It automatically sets the name of the descriptor
        if self.name is None:
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

위 코드에서 `Validator` 클래스의 `__set_name__` 메서드는 `name` 속성이 `None`인지 확인합니다. 그렇다면 `name`을 클래스 정의에 사용된 실제 속성 이름으로 설정합니다. 이렇게 하면 descriptor 클래스의 인스턴스를 생성할 때 이름을 명시적으로 지정할 필요가 없습니다.

이제 `validate.py` 파일을 업데이트했으므로 개선된 버전의 `Stock` 클래스를 만들 수 있습니다. 이 새 버전에서는 이름을 중복해서 지정할 필요가 없습니다. 개선된 `Stock` 클래스에 대한 코드는 다음과 같습니다.

```python
# improved_stock.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String()  # No need to specify 'name' anymore
    shares = PositiveInteger()
    price = PositiveFloat()

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

이 `Stock` 클래스에서는 이름을 지정하지 않고 `String`, `PositiveInteger`, 그리고 `PositiveFloat` descriptor 클래스의 인스턴스를 생성합니다. `Validator` 클래스의 `__set_name__` 메서드가 자동으로 이름을 설정합니다.

개선된 `Stock` 클래스를 테스트해 보겠습니다. 먼저 터미널을 열고 프로젝트 디렉토리로 이동합니다. 그런 다음 `improved_stock.py` 파일을 대화형 모드로 실행합니다. 다음은 그렇게 하기 위한 명령입니다.

```bash
cd ~/project
python3 -i improved_stock.py
```

대화형 Python 세션에 들어가면 다음 명령을 시도하여 `Stock` 클래스의 기능을 테스트할 수 있습니다.

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing values
s.shares = 75
print(s.shares)  # Should return 75

# Try invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    s.price = -10.5  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

exit()
```

이러한 명령은 `Stock` 클래스의 인스턴스를 생성하고, 해당 속성을 인쇄하고, 속성의 값을 변경한 다음, 적절한 오류가 발생하는지 확인하기 위해 유효하지 않은 값을 설정하려고 시도합니다.

`__set_name__` 메서드는 클래스가 정의될 때 descriptor 의 이름을 자동으로 설정합니다. 이렇게 하면 속성 이름을 두 번 지정할 필요가 없으므로 코드가 더 깔끔하고 중복이 줄어듭니다.

이 개선 사항은 Python 의 descriptor 프로토콜이 어떻게 계속 발전하여 깔끔하고 유지 관리 가능한 코드를 더 쉽게 작성할 수 있는지 보여줍니다.
