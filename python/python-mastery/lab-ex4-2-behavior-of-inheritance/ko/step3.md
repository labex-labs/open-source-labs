# 주식 클래스에 검사기 적용하기

이 단계에서는 실제 상황에서 검사기가 어떻게 작동하는지 살펴보겠습니다. 검사기는 우리가 사용하는 데이터가 특정 규칙을 충족하는지 확인하는 작은 검사기와 같습니다. `Stock` 클래스를 만들 것입니다. 클래스는 객체를 생성하기 위한 청사진과 같습니다. 이 경우 `Stock` 클래스는 주식 시장의 주식을 나타내며, 속성 (예: 주식 수 및 가격) 의 값이 유효한지 확인하기 위해 검사기를 사용합니다.

## Stock 클래스 생성

먼저, 새 파일을 만들어야 합니다. WebIDE 에서 `stock.py`라는 새 파일을 만듭니다. 이 파일에는 `Stock` 클래스에 대한 코드가 포함됩니다. 이제 다음 코드를 `stock.py` 파일에 추가합니다.

```python
# stock.py
from validate import PositiveInteger, PositiveFloat

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
        self._shares = PositiveInteger.check(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = PositiveFloat.check(value)

    def cost(self):
        return self.shares * self.price
```

이 코드가 수행하는 작업을 자세히 살펴보겠습니다.

1. 먼저 `validate` 모듈에서 `PositiveInteger` 및 `PositiveFloat` 검사기를 가져옵니다. 이러한 검사기는 주식 수가 양의 정수이고 가격이 양의 부동 소수점인지 확인하는 데 도움이 됩니다.
2. 그런 다음 `Stock` 클래스를 정의합니다. 클래스 내부에 `__init__` 메서드가 있습니다. 이 메서드는 새 `Stock` 객체를 만들 때 호출됩니다. `name`, `shares`, `price`의 세 가지 매개변수를 사용하고 이를 객체의 속성에 할당합니다.
3. 속성 (property) 과 setter 를 사용하여 `shares` 및 `price`의 값을 검사합니다. 속성은 속성에 대한 액세스를 제어하는 방법이며, setter 는 해당 속성의 값을 설정하려고 할 때 호출되는 메서드입니다. `shares` 속성을 설정하면 `PositiveInteger.check` 메서드가 호출되어 값이 양의 정수인지 확인합니다. 마찬가지로 `price` 속성을 설정하면 `PositiveFloat.check` 메서드가 호출되어 값이 양의 부동 소수점인지 확인합니다.
4. 마지막으로 `cost` 메서드가 있습니다. 이 메서드는 주식 수에 가격을 곱하여 주식의 총 비용을 계산합니다.

## Stock 클래스 테스트

이제 `Stock` 클래스를 만들었으므로 검사기가 제대로 작동하는지 테스트해야 합니다. 새 터미널을 열고 Python 인터프리터를 시작합니다. 다음 명령을 실행하여 이 작업을 수행할 수 있습니다.

```bash
python3
```

Python 인터프리터가 실행되면 `Stock` 클래스를 가져와 테스트할 수 있습니다. 다음 코드를 Python 인터프리터에 입력합니다.

```python
from stock import Stock

# Create a valid stock
s = Stock('GOOG', 100, 490.10)
print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
print(f"Cost: {s.cost()}")

# Try setting an invalid shares value
try:
    s.shares = -10
except ValueError as e:
    print(f"Error setting shares: {e}")

# Try setting an invalid price value
try:
    s.price = "not a price"
except TypeError as e:
    print(f"Error setting price: {e}")
```

이 코드를 실행하면 다음과 유사한 출력이 표시됩니다.

```
Name: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0
Error setting shares: Expected >= 0
Error setting price: Expected <class 'float'>
```

이 출력은 검사기가 예상대로 작동함을 보여줍니다. `Stock` 클래스는 `shares` 및 `price`에 대해 유효하지 않은 값을 설정하는 것을 허용하지 않습니다. 유효하지 않은 값을 설정하려고 하면 오류가 발생하며, 해당 오류를 catch 하여 출력할 수 있습니다.

## 상속이 어떻게 도움이 되는지 이해하기

검사기를 사용하는 것의 가장 좋은 점 중 하나는 다양한 유효성 검사 규칙을 쉽게 결합할 수 있다는 것입니다. 상속은 Python 에서 기존 클래스를 기반으로 새로운 클래스를 만들 수 있게 해주는 강력한 개념입니다. 다중 상속을 사용하면 `super()` 함수를 사용하여 여러 부모 클래스의 메서드를 호출할 수 있습니다.

예를 들어, 주식 이름이 비어 있지 않은지 확인하려면 다음 단계를 따를 수 있습니다.

1. `validate` 모듈에서 `NonEmptyString` 검사기를 가져옵니다. 이 검사기는 주식 이름이 빈 문자열이 아닌지 확인하는 데 도움이 됩니다.
2. `Stock` 클래스에서 `name` 속성에 대한 속성 setter 를 추가합니다. 이 setter 는 `NonEmptyString.check()` 메서드를 사용하여 주식 이름을 검사합니다.

이것은 상속, 특히 `super()` 함수를 사용한 다중 상속을 통해 유연하고 다양한 조합으로 재사용할 수 있는 구성 요소를 구축할 수 있음을 보여줍니다.

테스트를 마쳤으면 다음 명령을 실행하여 Python 인터프리터를 종료할 수 있습니다.

```python
exit()
```
