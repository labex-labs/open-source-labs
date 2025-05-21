# 형식화된 구조 도우미 생성

이 단계에서는 더 실용적인 예제를 구축할 것입니다. 형식 유효성 검사를 사용하여 클래스를 생성하는 함수를 구현합니다. 형식 유효성 검사는 클래스 속성에 할당된 데이터가 특정 기준 (예: 특정 데이터 형식 또는 특정 범위 내) 을 충족하는지 확인하므로 매우 중요합니다. 이를 통해 오류를 조기에 포착하고 코드를 더욱 강력하게 만들 수 있습니다.

## Structure 클래스 이해

먼저 WebIDE 편집기에서 `structure.py` 파일을 열어야 합니다. 이 파일에는 기본 `Structure` 클래스가 포함되어 있습니다. 이 클래스는 구조화된 객체를 초기화하고 나타내는 기본적인 기능을 제공합니다. 초기화는 제공된 데이터로 객체를 설정하는 것을 의미하고, 표현은 객체를 인쇄할 때 객체가 표시되는 방식에 관한 것입니다.

파일을 열려면 터미널에서 다음 명령을 사용합니다.

```bash
cd ~/project
```

이 명령을 실행하면 `structure.py` 파일이 있는 올바른 디렉토리에 있게 됩니다. 파일을 열면 기본 `Structure` 클래스를 볼 수 있습니다. 우리의 목표는 이 클래스를 확장하여 형식 유효성 검사를 지원하는 것입니다.

## typed_structure 함수 구현

이제 `typed_structure` 함수를 `structure.py` 파일에 추가해 보겠습니다. 이 함수는 `Structure` 클래스에서 상속하고 지정된 유효성 검사기를 포함하는 새 클래스를 생성합니다. 상속은 새 클래스가 `Structure` 클래스의 모든 기능을 갖게 되며 자체 기능을 추가할 수도 있음을 의미합니다. 유효성 검사기는 클래스 속성에 할당된 값이 유효한지 확인하는 데 사용됩니다.

다음은 `typed_structure` 함수의 코드입니다.

```python
def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

`clsname` 매개변수는 새 클래스에 지정하려는 이름입니다. `validators` 매개변수는 키가 속성 이름이고 값이 유효성 검사기 객체인 딕셔너리입니다. `type()` 함수는 새 클래스를 동적으로 생성하는 데 사용됩니다. 클래스 이름, 기본 클래스 튜플 (이 경우 `Structure` 클래스만 해당) 및 클래스 속성 (유효성 검사기) 의 딕셔너리, 이렇게 세 개의 인수를 사용합니다.

이 함수를 추가한 후 `structure.py` 파일은 다음과 같이 표시됩니다.

```python
# Structure class definition

class Structure:
    _fields = ()

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        attrs = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({attrs})'

def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

## typed_structure 함수 테스트

`validate.py` 파일의 유효성 검사기를 사용하여 `typed_structure` 함수를 테스트해 보겠습니다. 이러한 유효성 검사기는 클래스 속성에 할당된 값이 올바른 형식인지 확인하고 다른 기준을 충족하는지 확인하는 데 사용됩니다.

먼저 Python 대화형 셸을 엽니다. 터미널에서 다음 명령을 사용합니다.

```bash
cd ~/project
python3
```

첫 번째 명령은 올바른 디렉토리로 이동하고, 두 번째 명령은 Python 대화형 셸을 시작합니다.

이제 필요한 구성 요소를 가져와서 형식화된 구조를 생성합니다.

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import typed_structure

# Create a Stock class with type validation
Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())

# Create a stock instance
s = Stock('GOOG', 100, 490.1)

# Test the instance
print(s.name)
print(s)

# Test validation
try:
    invalid_stock = Stock('AAPL', -10, 150.25)  # Should raise an error
except ValueError as e:
    print(f"Validation error: {e}")
```

`validate.py` 파일에서 `String`, `PositiveInteger`, `PositiveFloat` 유효성 검사기를 가져옵니다. 그런 다음 `typed_structure` 함수를 사용하여 형식 유효성 검사가 있는 `Stock` 클래스를 생성합니다. `Stock` 클래스의 인스턴스를 생성하고 속성을 인쇄하여 테스트합니다. 마지막으로 유효성 검사를 테스트하기 위해 잘못된 주식 인스턴스를 생성하려고 합니다.

다음과 유사한 출력이 표시됩니다.

```
GOOG
Stock('GOOG', 100, 490.1)
Validation error: Expected a positive value
```

테스트를 마쳤으면 Python 셸을 종료합니다.

```python
exit()
```

이 예제는 `type()` 함수를 사용하여 특정 유효성 검사 규칙이 있는 사용자 정의 클래스를 생성하는 방법을 보여줍니다. 이 접근 방식은 클래스를 프로그래밍 방식으로 생성할 수 있으므로 매우 강력하며, 이는 많은 시간을 절약하고 코드를 더 유연하게 만들 수 있습니다.
