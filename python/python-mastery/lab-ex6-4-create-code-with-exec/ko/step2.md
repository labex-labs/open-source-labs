# 동적 **init**() 메서드 생성

이제 `exec()` 함수에 대해 배운 내용을 실제 프로그래밍 시나리오에 적용해 보겠습니다. Python 에서 `exec()` 함수를 사용하면 문자열에 저장된 Python 코드를 실행할 수 있습니다. 이 단계에서는 `Structure` 클래스를 수정하여 `__init__()` 메서드를 동적으로 생성합니다. `__init__()` 메서드는 Python 클래스에서 객체가 인스턴스화될 때 호출되는 특수한 메서드입니다. 이 메서드의 생성은 클래스의 필드 이름 목록을 포함하는 `_fields` 클래스 변수를 기반으로 합니다.

먼저, 기존의 `structure.py` 파일을 살펴보겠습니다. 이 파일에는 `Structure` 클래스와 이를 상속하는 `Stock` 클래스의 현재 구현이 포함되어 있습니다. 파일의 내용을 보려면 다음 명령을 사용하여 WebIDE 에서 엽니다.

```bash
cat /home/labex/project/structure.py
```

출력에서 현재 구현이 객체의 초기화를 처리하기 위해 수동적인 접근 방식을 사용하고 있음을 알 수 있습니다. 즉, 객체의 속성을 초기화하는 코드가 동적으로 생성되는 대신 명시적으로 작성됩니다.

이제 `Structure` 클래스를 수정하겠습니다. `__init__()` 메서드를 동적으로 생성하는 `create_init()` 클래스 메서드를 추가합니다. 이러한 변경을 하려면 WebIDE 편집기에서 `structure.py` 파일을 열고 다음 단계를 따르세요.

1. `Structure` 클래스에서 기존의 `_init()` 및 `set_fields()` 메서드를 제거합니다. 이러한 메서드는 수동 초기화 접근 방식의 일부이며, 동적 접근 방식을 사용할 것이므로 더 이상 필요하지 않습니다.

2. `create_init()` 클래스 메서드를 `Structure` 클래스에 추가합니다. 메서드에 대한 코드는 다음과 같습니다.

```python
@classmethod
def create_init(cls):
    """Dynamically create an __init__ method based on _fields."""
    # Create argument string from field names
    argstr = ','.join(cls._fields)

    # Create the function code as a string
    code = f'def __init__(self, {argstr}):\n'
    for name in cls._fields:
        code += f'    self.{name} = {name}\n'

    # Execute the code and get the generated function
    locs = {}
    exec(code, locs)

    # Set the function as the __init__ method of the class
    setattr(cls, '__init__', locs['__init__'])
```

이 메서드에서 먼저 쉼표로 구분된 모든 필드 이름을 포함하는 문자열 `argstr`을 생성합니다. 이 문자열은 `__init__()` 메서드의 인수 목록으로 사용됩니다. 그런 다음, `__init__()` 메서드에 대한 코드를 문자열로 생성합니다. 필드 이름을 반복하고 각 인수를 해당 객체 속성에 할당하는 코드를 추가합니다. 그 후, `exec()` 함수를 사용하여 코드를 실행하고 생성된 함수를 `locs` 딕셔너리에 저장합니다. 마지막으로, `setattr()` 함수를 사용하여 생성된 함수를 클래스의 `__init__()` 메서드로 설정합니다.

3. 이 새로운 접근 방식을 사용하도록 `Stock` 클래스를 수정합니다.

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

여기에서 `Stock` 클래스에 대한 `_fields`를 정의한 다음 `create_init()` 메서드를 호출하여 `Stock` 클래스에 대한 `__init__()` 메서드를 생성합니다.

완성된 `structure.py` 파일은 다음과 같이 표시됩니다.

```python
class Structure:
    # Restrict attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")

    # String representation for debugging
    def __repr__(self):
        args = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f"{type(self).__name__}({args})"

    @classmethod
    def create_init(cls):
        """Dynamically create an __init__ method based on _fields."""
        # Create argument string from field names
        argstr = ','.join(cls._fields)

        # Create the function code as a string
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'

        # Execute the code and get the generated function
        locs = {}
        exec(code, locs)

        # Set the function as the __init__ method of the class
        setattr(cls, '__init__', locs['__init__'])

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

이제 구현이 올바르게 작동하는지 테스트해 보겠습니다. 모든 테스트가 통과하는지 확인하기 위해 단위 테스트 파일을 실행합니다. 다음 명령을 사용합니다.

```bash
cd /home/labex/project
python3 -m unittest test_structure.py
```

구현이 올바르면 모든 테스트가 통과하는 것을 볼 수 있습니다. 이는 동적으로 생성된 `__init__()` 메서드가 예상대로 작동하고 있음을 의미합니다.

Python 셸에서 클래스를 수동으로 테스트할 수도 있습니다. 방법은 다음과 같습니다.

```python
>>> from structure import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s
Stock('GOOG', 100, 490.1)
>>> s.shares = 50
>>> s.share = 50  # This should raise an AttributeError
Traceback (most recent call last):
  ...
AttributeError: No attribute share
```

Python 셸에서 먼저 `structure.py` 파일에서 `Stock` 클래스를 가져옵니다. 그런 다음, `Stock` 클래스의 인스턴스를 생성하고 인쇄합니다. 객체의 `shares` 속성을 수정할 수도 있습니다. 그러나 `_fields` 목록에 없는 속성을 설정하려고 하면 `AttributeError`가 발생해야 합니다.

축하합니다! `exec()` 함수를 사용하여 클래스 속성을 기반으로 `__init__()` 메서드를 동적으로 생성하는 데 성공했습니다. 이 접근 방식은 특히 가변적인 수의 속성을 가진 클래스를 처리할 때 코드를 더 유연하고 유지 관리하기 쉽게 만들 수 있습니다.
