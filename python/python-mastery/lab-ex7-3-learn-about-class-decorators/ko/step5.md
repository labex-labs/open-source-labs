# 메서드 인자 유효성 검사 추가

Python 에서 데이터 유효성 검사는 견고한 코드를 작성하는 데 중요한 부분입니다. 이 섹션에서는 메서드 인자를 자동으로 유효성 검사하여 유효성 검사를 한 단계 더 발전시키겠습니다. `validate.py` 파일에는 이미 `@validated` 데코레이터가 포함되어 있습니다. Python 의 데코레이터는 다른 함수를 수정할 수 있는 특수한 함수입니다. 여기의 `@validated` 데코레이터는 함수 인자를 해당 주석과 비교하여 확인할 수 있습니다. Python 의 주석은 함수 매개변수 및 반환 값에 메타데이터를 추가하는 방법입니다.

이 데코레이터를 주석이 있는 메서드에 적용하도록 코드를 수정해 보겠습니다.

1. 먼저 `validated` 데코레이터가 어떻게 작동하는지 이해해야 합니다. `validate.py` 파일을 열어 검토합니다.

```bash
code ~/project/validate.py
```

`validated` 데코레이터는 함수 주석을 사용하여 인자를 유효성 검사합니다. 함수를 실행하기 전에 각 인자를 해당 주석 유형과 비교하여 확인합니다. 예를 들어 인자가 정수로 주석 처리된 경우 데코레이터는 전달된 값이 실제로 정수인지 확인합니다.

2. 이제 `structure.py`에서 `validate_attributes` 함수를 수정하여 주석이 있는 메서드를 `@validated` 데코레이터로 래핑합니다. 즉, 클래스에 주석이 있는 모든 메서드는 인자가 자동으로 유효성 검사됩니다. `structure.py` 파일을 엽니다.

```bash
code ~/project/structure.py
```

3. `validate_attributes` 함수를 업데이트합니다.

```python
def validate_attributes(cls):
    """
    Class decorator that:
    1. Extracts Validator instances and builds _fields and _types lists
    2. Applies @validated decorator to methods with annotations
    """
    # Import the validated decorator
    from validate import validated

    # Process validator descriptors
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Apply @validated decorator to methods with annotations
    for name, val in vars(cls).items():
        if callable(val) and hasattr(val, '__annotations__'):
            setattr(cls, name, validated(val))

    # Create initialization method
    cls.create_init()

    return cls
```

이 업데이트된 함수는 이제 다음을 수행합니다.

1. 이전과 같이 검증자 디스크립터를 처리합니다. 검증자 디스크립터는 클래스 속성에 대한 유효성 검사 규칙을 정의하는 데 사용됩니다.
2. 클래스에서 주석이 있는 모든 메서드를 찾습니다. 주석은 인자의 예상 유형을 지정하기 위해 메서드 매개변수에 추가됩니다.
3. 해당 메서드에 `@validated` 데코레이터를 적용합니다. 이렇게 하면 이러한 메서드에 전달된 인자가 해당 주석에 따라 유효성 검사됩니다.

4. 이러한 변경을 수행한 후 파일을 저장합니다. 파일을 저장하는 것은 수정 사항이 저장되고 나중에 사용할 수 있도록 하는 데 중요합니다.

5. 이제 `Stock` 클래스의 `sell` 메서드를 업데이트하여 주석을 포함해 보겠습니다. 주석은 `@validated` 데코레이터가 유효성 검사에 사용할 인자의 예상 유형을 지정하는 데 도움이 됩니다. `stock.py` 파일을 엽니다.

```bash
code ~/project/stock.py
```

6. 유형 주석을 포함하도록 `sell` 메서드를 수정합니다.

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

중요한 변경 사항은 `nshares` 매개변수에 `: PositiveInteger`를 추가하는 것입니다. 이렇게 하면 Python(및 `@validated` 데코레이터) 에 `PositiveInteger` 검증자를 사용하여 이 인자를 유효성 검사하도록 지시합니다. 따라서 `sell` 메서드를 호출하면 `nshares` 인자는 양의 정수여야 합니다.

7. 모든 것이 여전히 작동하는지 확인하기 위해 테스트를 다시 실행합니다. 테스트를 실행하는 것은 변경 사항으로 인해 기존 기능이 손상되지 않았는지 확인하는 좋은 방법입니다.

```bash
cd ~/project
python3 teststock.py
```

모든 테스트가 통과되는 것을 볼 수 있습니다.

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

8. 새로운 인자 유효성 검사를 테스트해 보겠습니다. 유효성 검사가 예상대로 작동하는지 확인하기 위해 유효하고 유효하지 않은 인자로 `sell` 메서드를 호출해 보겠습니다.

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); s.sell(25); print(s); try: s.sell(-25); except Exception as e: print(f'Error: {e}')"
```

다음과 유사한 출력이 표시됩니다.

```
Stock('GOOG', 75, 490.1)
Error: Bad Arguments
  nshares: must be >= 0
```

이는 메서드 인자 유효성 검사가 작동하고 있음을 보여줍니다! `sell(25)`에 대한 첫 번째 호출은 `25`가 양의 정수이므로 성공합니다. 그러나 `-25`는 양의 정수가 아니므로 `sell(-25)`에 대한 두 번째 호출은 실패합니다.

이제 다음을 위한 완전한 시스템을 구현했습니다.

1. 디스크립터를 사용하여 클래스 속성을 유효성 검사합니다. 디스크립터는 클래스 속성에 대한 유효성 검사 규칙을 정의하는 데 사용됩니다.
2. 클래스 데코레이터를 사용하여 필드 정보를 자동으로 수집합니다. 클래스 데코레이터는 필드 정보를 수집하는 것처럼 클래스의 동작을 수정할 수 있습니다.
3. 행 데이터를 인스턴스로 변환합니다. 이는 외부 소스의 데이터를 사용할 때 유용합니다.
4. 주석을 사용하여 메서드 인자를 유효성 검사합니다. 주석은 유효성 검사를 위해 인자의 예상 유형을 지정하는 데 도움이 됩니다.

이는 Python 에서 디스크립터와 데코레이터를 결합하여 표현력이 풍부하고 자체 유효성 검사 클래스를 만드는 강력함을 보여줍니다.
