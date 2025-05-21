# 유효성 검사를 위한 클래스 데코레이터 생성

이전 단계에서 구현은 작동했지만 중복이 있었습니다. `_fields` 튜플과 디스크립터 속성을 모두 지정해야 했습니다. 이는 그다지 효율적이지 않으며 개선할 수 있습니다. Python 에서 클래스 데코레이터는 이 프로세스를 단순화하는 데 도움이 되는 강력한 도구입니다. 클래스 데코레이터는 클래스를 인수로 받아 어떤 방식으로든 수정하고 수정된 클래스를 반환하는 함수입니다. 클래스 데코레이터를 사용하면 디스크립터에서 필드 정보를 자동으로 추출할 수 있으므로 코드가 더 깔끔하고 유지 관리하기 쉬워집니다.

코드를 단순화하기 위해 클래스 데코레이터를 만들어 보겠습니다. 따라야 할 단계는 다음과 같습니다.

1. 먼저 `structure.py` 파일을 엽니다. 터미널에서 다음 명령을 사용할 수 있습니다.

```bash
code ~/project/structure.py
```

이 명령은 코드 편집기에서 `structure.py` 파일을 엽니다.

2. 다음으로, 모든 import 문 바로 뒤, `structure.py` 파일의 맨 위에 다음 코드를 추가합니다. 이 코드는 클래스 데코레이터를 정의합니다.

```python
from validate import Validator

def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields list automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

이 데코레이터가 하는 일을 자세히 살펴보겠습니다.

- 먼저 `validators`라는 빈 목록을 만듭니다. 그런 다음 `vars(cls).items()`를 사용하여 클래스의 모든 속성을 반복합니다. 속성이 `Validator` 클래스의 인스턴스인 경우 해당 속성을 `validators` 목록에 추가합니다.
- 그 후 클래스의 `_fields` 속성을 설정합니다. `validators` 목록의 검증자에서 이름 목록을 만들고 이를 `cls._fields`에 할당합니다.
- 마지막으로 클래스의 `create_init()` 메서드를 호출하여 `__init__` 메서드를 생성한 다음 수정된 클래스를 반환합니다.

3. 코드를 추가한 후 `structure.py` 파일을 저장합니다. 파일을 저장하면 변경 사항이 유지됩니다.

4. 이제 이 새로운 데코레이터를 사용하도록 `stock.py` 파일을 수정해야 합니다. 다음 명령을 사용하여 `stock.py` 파일을 엽니다.

```bash
code ~/project/stock.py
```

5. `validate_attributes` 데코레이터를 사용하도록 `stock.py` 파일을 업데이트합니다. 기존 코드를 다음으로 바꿉니다.

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

변경 사항을 확인하십시오.

- `@validate_attributes` 데코레이터를 `Stock` 클래스 정의 바로 위에 추가했습니다. 이렇게 하면 Python 이 `validate_attributes` 데코레이터를 `Stock` 클래스에 적용하도록 지시합니다.
- 데코레이터가 자동으로 처리하므로 명시적인 `_fields` 선언을 제거했습니다.
- 데코레이터가 `__init__` 메서드 생성을 처리하므로 `Stock.create_init()`에 대한 호출도 제거했습니다.

결과적으로 클래스가 더 간단하고 깔끔해졌습니다. 데코레이터는 수동으로 처리했던 모든 세부 사항을 처리합니다.

6. 이러한 변경을 수행한 후 모든 것이 예상대로 작동하는지 확인해야 합니다. 다음 명령을 사용하여 테스트를 다시 실행합니다.

```bash
cd ~/project
python3 teststock.py
```

모든 것이 올바르게 작동하면 다음 출력이 표시됩니다.

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

이 출력은 모든 테스트가 성공적으로 통과되었음을 나타냅니다.

`Stock` 클래스를 대화식으로 테스트해 보겠습니다. 터미널에서 다음 명령을 실행합니다.

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

다음 출력이 표시됩니다.

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

훌륭합니다! 필드 선언 및 초기화를 자동으로 처리하여 코드를 단순화하는 클래스 데코레이터를 성공적으로 구현했습니다. 이렇게 하면 코드가 더 효율적이고 유지 관리하기 쉬워집니다.
