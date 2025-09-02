# 디스크립터를 사용한 타입 검사 구현

이 단계에서는 타입 검사를 위해 디스크립터를 사용하는 `Stock` 클래스를 생성합니다. 하지만 먼저 디스크립터가 무엇인지 이해해 봅시다. 디스크립터는 Python 의 매우 강력한 기능입니다. 클래스에서 속성에 접근하는 방식을 제어할 수 있게 해줍니다.

디스크립터는 다른 객체에서 속성에 접근하는 방식을 정의하는 객체입니다. 이는 `__get__`, `__set__`, `__delete__`와 같은 특별한 메서드를 구현함으로써 이루어집니다. 이러한 메서드를 통해 디스크립터는 속성을 검색, 설정 및 삭제하는 방식을 관리할 수 있습니다. 디스크립터는 유효성 검사, 타입 검사 및 계산된 속성 (computed properties) 을 구현하는 데 매우 유용합니다. 예를 들어, 디스크립터를 사용하여 속성이 항상 양수이거나 특정 형식의 문자열인지 확인할 수 있습니다.

`validate.py` 파일에는 이미 검증자 클래스들 (`String`, `PositiveInteger`, `PositiveFloat`) 이 있습니다. 이러한 클래스를 사용하여 `Stock` 클래스의 속성을 검증할 수 있습니다.

이제 디스크립터를 사용하여 `Stock` 클래스를 만들어 보겠습니다.

1. 먼저 편집기에서 `stock.py` 파일을 엽니다.

2. 파일이 열리면 플레이스홀더 내용을 다음 코드로 바꿉니다.

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

# _fields 를 기반으로 __init__ 메서드 생성
Stock.create_init()
```

이 코드가 무엇을 하는지 자세히 살펴보겠습니다. `_fields` 튜플은 `Stock` 클래스의 속성을 정의합니다. 이것들은 `Stock` 객체가 가질 속성의 이름입니다.

`name`, `shares`, `price` 속성은 디스크립터 객체로 정의됩니다. `String()` 디스크립터는 `name` 속성이 문자열인지 확인합니다. `PositiveInteger()` 디스크립터는 `shares` 속성이 양의 정수인지 확인합니다. 그리고 `PositiveFloat()` 디스크립터는 `price` 속성이 양의 부동소수점 숫자인지 보장합니다.

`cost` 속성은 계산된 속성입니다. 주식 수와 주당 가격을 기반으로 주식의 총 비용을 계산합니다.

`sell` 메서드는 주식 수를 줄이는 데 사용됩니다. 판매할 주식 수를 인자로 이 메서드를 호출하면 해당 숫자를 `shares` 속성에서 차감합니다.

`Stock.create_init()` 줄은 클래스에 대한 `__init__` 메서드를 동적으로 생성합니다. 이 메서드를 통해 `name`, `shares`, `price` 속성에 대한 값을 전달하여 `Stock` 객체를 생성할 수 있습니다.

3. 코드를 추가한 후 파일을 저장합니다. 이렇게 하면 변경 사항이 저장되어 테스트를 실행할 때 사용할 수 있습니다.

4. 이제 테스트를 실행하여 구현을 확인해 봅시다. 먼저 다음 명령을 실행하여 디렉토리를 `~/project` 디렉토리로 변경합니다.

```bash
cd ~/project
```

그런 다음 다음 명령을 사용하여 테스트를 실행합니다.

```bash
python3 teststock.py
```

구현이 올바르다면 다음과 유사한 출력이 표시됩니다.

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

이 출력은 모든 테스트가 통과했음을 의미합니다. 디스크립터가 각 속성의 타입을 성공적으로 검증하고 있습니다!

Python 인터프리터에서 `Stock` 객체를 생성해 봅시다. 먼저 `~/project` 디렉토리에 있는지 확인합니다. 그런 다음 다음 명령을 실행합니다.

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

다음과 같은 출력이 표시되어야 합니다.

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

타입 검사를 위한 디스크립터를 성공적으로 구현했습니다! 이제 이 코드를 더 개선해 봅시다.
