# StructureMeta 메타클래스 생성

이제 다음에 할 일에 대해 이야기해 보겠습니다. 모든 검증자 유형을 수집하는 방법을 찾았습니다. 다음 단계는 메타클래스를 만드는 것입니다. 하지만 메타클래스란 정확히 무엇일까요? Python 에서 메타클래스는 특별한 종류의 클래스입니다. 그 인스턴스는 클래스 자체입니다. 즉, 메타클래스는 클래스가 생성되는 방식을 제어할 수 있습니다. 클래스 속성이 정의되는 네임스페이스를 관리할 수 있습니다.

이 상황에서 우리는 `Structure` 하위 클래스를 정의할 때 검증자 유형을 사용할 수 있도록 하는 메타클래스를 만들고 싶습니다. 매번 이러한 검증자 유형을 명시적으로 가져올 필요가 없도록 하려는 것입니다.

`structure.py` 파일을 다시 열어 시작해 보겠습니다. 다음 명령을 사용하여 열 수 있습니다.

```bash
code structure.py
```

파일이 열리면 `Structure` 클래스 정의 앞에 몇 줄의 코드를 추가해야 합니다. 이 코드는 메타클래스를 정의합니다.

```python
from validate import Validator
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        """Prepare the namespace for the class being defined"""
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        """Create the new class using only the local namespace"""
        methods = methods.maps[0]  # Extract the local namespace
        return super().__new__(meta, name, bases, methods)
```

이제 메타클래스를 정의했으므로 이를 사용하도록 `Structure` 클래스를 수정해야 합니다. 이렇게 하면 `Structure`에서 상속받는 모든 클래스가 메타클래스의 기능을 활용할 수 있습니다.

```python
class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

        # Set the remaining keyword arguments
        for name, val in kwargs.items():
            if name not in self._fields:
                raise TypeError(f'Invalid argument: {name}')
            setattr(self, name, val)

    def __repr__(self):
        values = [getattr(self, name) for name in self._fields]
        args_str = ','.join(repr(val) for val in values)
        return f'{type(self).__name__}({args_str})'
```

이 코드가 하는 일을 자세히 살펴보겠습니다.

1. `__prepare__()` 메서드는 Python 의 특수 메서드입니다. 클래스가 생성되기 전에 호출됩니다. 이 메서드의 역할은 클래스 속성이 정의될 네임스페이스를 준비하는 것입니다. 여기서는 `ChainMap`을 사용합니다. `ChainMap`은 계층화된 딕셔너리를 생성하는 유용한 도구입니다. 이 경우 검증자 유형을 포함하여 클래스 네임스페이스에서 액세스할 수 있도록 합니다.

2. `__new__()` 메서드는 새 클래스를 생성하는 역할을 합니다. 로컬 네임스페이스만 추출합니다. 즉, `ChainMap`의 첫 번째 딕셔너리입니다. 네임스페이스에서 검증자 유형을 이미 사용할 수 있도록 했으므로 검증자 딕셔너리는 버립니다.

이 설정을 사용하면 `Structure`에서 상속받는 모든 클래스가 명시적으로 가져올 필요 없이 모든 검증자 유형에 액세스할 수 있습니다.

이제 구현을 테스트해 보겠습니다. 향상된 `Structure` 기본 클래스를 사용하여 `Stock` 클래스를 생성합니다.

```bash
cat > stock.py << EOF
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
EOF
```

메타클래스가 제대로 작동하면 검증자 유형을 가져오지 않고도 `Stock` 클래스를 정의할 수 있어야 합니다. 이는 메타클래스가 이미 네임스페이스에서 사용할 수 있도록 했기 때문입니다.
