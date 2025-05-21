# 상속을 통한 데코레이터 적용

2 단계에서 코드를 단순화하는 클래스 데코레이터를 만들었습니다. 클래스 데코레이터는 클래스를 인수로 받아 수정된 클래스를 반환하는 특수한 유형의 함수입니다. 이는 원래 코드를 수정하지 않고 클래스에 기능을 추가하는 데 유용한 Python 도구입니다. 그러나 여전히 각 클래스에 `@validate_attributes` 데코레이터를 명시적으로 적용해야 합니다. 즉, 유효성 검사가 필요한 새 클래스를 만들 때마다 이 데코레이터를 추가하는 것을 기억해야 하며, 이는 다소 번거로울 수 있습니다.

상속을 통해 데코레이터를 자동으로 적용하여 이를 더욱 개선할 수 있습니다. 상속은 서브클래스가 상위 클래스에서 속성과 메서드를 상속받을 수 있는 객체 지향 프로그래밍의 기본 개념입니다. Python 의 `__init_subclass__` 메서드는 Python 3.6 에 도입되어 상위 클래스가 서브클래스의 초기화를 사용자 정의할 수 있도록 했습니다. 즉, 서브클래스가 생성될 때 상위 클래스가 서브클래스에 대해 일부 작업을 수행할 수 있습니다. 이 기능을 사용하여 `Structure`에서 상속받는 모든 클래스에 데코레이터를 자동으로 적용할 수 있습니다.

이를 구현해 보겠습니다.

1. `structure.py` 파일을 엽니다.

```bash
code ~/project/structure.py
```

여기서는 `code` 명령을 사용하여 코드 편집기에서 `structure.py` 파일을 엽니다. 이 파일에는 `Structure` 클래스의 정의가 포함되어 있으며, `__init_subclass__` 메서드를 사용하도록 수정할 것입니다.

2. `__init_subclass__` 메서드를 `Structure` 클래스에 추가합니다.

```python
class Structure:
    _fields = ()
    _types = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f'{type(self).__name__}({values})'

    @classmethod
    def create_init(cls):
        '''
        Create an __init__ method from _fields
        '''
        body = 'def __init__(self, %s):\n' % ', '.join(cls._fields)
        for name in cls._fields:
            body += f'    self.{name} = {name}\n'

        # Execute the function creation code
        namespace = {}
        exec(body, namespace)
        setattr(cls, '__init__', namespace['__init__'])

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

`__init_subclass__` 메서드는 클래스 메서드입니다. 즉, 클래스의 인스턴스가 아닌 클래스 자체에서 호출할 수 있습니다. `Structure`의 서브클래스가 생성되면 이 메서드가 자동으로 호출됩니다. 이 메서드 내에서 서브클래스 `cls`에 `validate_attributes` 데코레이터를 호출합니다. 이렇게 하면 `Structure`의 모든 서브클래스가 자동으로 유효성 검사 동작을 갖게 됩니다.

3. 파일을 저장합니다.

`structure.py` 파일을 변경한 후에는 변경 사항을 적용하기 위해 저장해야 합니다.

4. 이제 이 새로운 기능을 활용하도록 `stock.py` 파일을 업데이트해 보겠습니다.

```bash
code ~/project/stock.py
```

`stock.py` 파일을 열어 수정합니다. 이 파일에는 `Stock` 클래스의 정의가 포함되어 있으며, 자동 데코레이터 적용을 사용하기 위해 `Structure` 클래스에서 상속받도록 만들 것입니다.

5. 명시적 데코레이터를 제거하도록 `stock.py` 파일을 수정합니다.

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

    def sell(self, nshares):
        self.shares -= nshares
```

다음 사항에 유의하십시오.

- 데코레이터가 상속을 통해 자동으로 적용되므로 더 이상 명시적으로 가져올 필요가 없으므로 `validate_attributes` 가져오기를 제거했습니다.
- `Structure` 클래스의 `__init_subclass__` 메서드가 이를 적용하므로 `@validate_attributes` 데코레이터를 제거했습니다.
- 이제 코드는 유효성 검사 동작을 얻기 위해 `Structure`에서 상속받는 데만 의존합니다.

6. 모든 것이 여전히 작동하는지 확인하기 위해 테스트를 다시 실행합니다.

```bash
cd ~/project
python3 teststock.py
```

테스트를 실행하는 것은 변경 사항으로 인해 아무것도 손상되지 않았는지 확인하는 데 중요합니다. 모든 테스트가 통과되면 상속을 통한 자동 데코레이터 적용이 올바르게 작동하고 있음을 의미합니다.

모든 테스트가 통과되는 것을 볼 수 있습니다.

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

`Stock` 클래스가 예상대로 작동하는지 다시 테스트해 보겠습니다.

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

이 명령은 `Stock` 클래스의 인스턴스를 생성하고 해당 표현과 비용을 출력합니다. 출력이 예상대로 나오면 `Stock` 클래스가 자동 데코레이터 적용으로 올바르게 작동하고 있음을 의미합니다.

출력:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

이 구현은 훨씬 더 깔끔합니다! `__init_subclass__`를 사용함으로써 데코레이터를 명시적으로 적용할 필요가 없어졌습니다. `Structure`에서 상속받는 모든 클래스는 자동으로 유효성 검사 동작을 얻습니다.
