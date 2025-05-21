# 상속을 사용한 유효성 검사 시스템 구축

이 단계에서는 상속을 사용하여 실용적인 유효성 검사 시스템을 구축할 것입니다. 상속은 프로그래밍에서 기존 클래스를 기반으로 새로운 클래스를 만들 수 있게 해주는 강력한 개념입니다. 이러한 방식으로 코드를 재사용하고 더 체계적이고 모듈화된 프로그램을 만들 수 있습니다. 이 유효성 검사 시스템을 구축함으로써 상속이 다양한 방식으로 결합될 수 있는 재사용 가능한 코드 구성 요소를 만드는 데 어떻게 사용될 수 있는지 알 수 있습니다.

## 기본 검사기 클래스 생성

먼저, 검사기를 위한 기본 클래스를 만들어야 합니다. 이를 위해 WebIDE 에서 새 파일을 만들 것입니다. 방법은 다음과 같습니다. "File" > "New File"을 클릭하거나 키보드 단축키를 사용할 수 있습니다. 새 파일이 열리면 이름을 `validate.py`로 지정합니다.

이제 이 파일에 코드를 추가하여 기본 `Validator` 클래스를 만들어 보겠습니다. 이 클래스는 다른 모든 검사기의 기반 역할을 합니다.

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

이 코드에서는 `check` 메서드가 있는 `Validator` 클래스를 정의했습니다. `check` 메서드는 값을 인수로 받아 변경 없이 그대로 반환합니다. `@classmethod` 데코레이터는 이 메서드를 클래스 메서드로 만듭니다. 즉, 클래스의 인스턴스를 만들 필요 없이 클래스 자체에서 이 메서드를 호출할 수 있습니다.

## 유형 검사기 추가

다음으로, 값의 유형을 확인하는 몇 가지 검사기를 추가하겠습니다. 이러한 검사기는 방금 만든 `Validator` 클래스에서 상속됩니다. `validate.py` 파일로 돌아가서 다음 코드를 추가합니다.

```python
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

`Typed` 클래스는 `Validator`의 서브클래스입니다. `expected_type` 속성이 있으며, 초기에는 `object`로 설정됩니다. `Typed` 클래스의 `check` 메서드는 주어진 값이 예상 유형인지 확인합니다. 그렇지 않은 경우 `TypeError`를 발생시킵니다. 유형이 올바르면 `super().check(value)`를 사용하여 부모 클래스의 `check` 메서드를 호출합니다.

`Integer`, `Float`, `String` 클래스는 `Typed`에서 상속받아 확인해야 하는 정확한 유형을 지정합니다. 예를 들어, `Integer` 클래스는 값이 정수인지 확인합니다.

## 유형 검사기 테스트

이제 유형 검사기를 만들었으므로 테스트해 보겠습니다. 새 터미널을 열고 다음 명령을 실행하여 Python 인터프리터를 시작합니다.

```bash
python3
```

Python 인터프리터가 실행되면 검사기를 가져와 테스트할 수 있습니다. 다음은 이를 테스트하기 위한 코드입니다.

```python
from validate import Integer, String

Integer.check(10)  # Should return 10

try:
    Integer.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

String.check('10')  # Should return '10'
```

이 코드를 실행하면 다음과 같은 내용이 표시됩니다.

```
10
Error: Expected <class 'int'>
'10'
```

이러한 검사기를 함수에서도 사용할 수 있습니다. 시도해 보겠습니다.

```python
def add(x, y):
    Integer.check(x)
    Integer.check(y)
    return x + y

add(2, 2)  # Should return 4

try:
    add('2', '3')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

이 코드를 실행하면 다음이 표시됩니다.

```
4
Error: Expected <class 'int'>
```

## 값 검사기 추가

지금까지 값의 유형을 확인하는 검사기를 만들었습니다. 이제 유형이 아닌 값 자체를 확인하는 몇 가지 검사기를 추가해 보겠습니다. `validate.py` 파일로 돌아가서 다음 코드를 추가합니다.

```python
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
```

`Positive` 검사기는 값이 음수가 아닌지 확인합니다. 값이 0 보다 작으면 `ValueError`를 발생시킵니다. `NonEmpty` 검사기는 값의 길이가 0 이 아닌지 확인합니다. 길이가 0 이면 `ValueError`를 발생시킵니다.

## 다중 상속을 사용한 검사기 구성

이제 다중 상속을 사용하여 검사기를 결합할 것입니다. 다중 상속을 사용하면 클래스가 둘 이상의 부모 클래스에서 상속받을 수 있습니다. `validate.py` 파일로 돌아가서 다음 코드를 추가합니다.

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

이러한 새 클래스는 유형 검사와 값 검사를 결합합니다. 예를 들어, `PositiveInteger` 클래스는 값이 정수이고 음수가 아닌지 확인합니다. 여기서 상속 순서가 중요합니다. 검사기는 클래스 정의에 지정된 순서대로 확인됩니다.

## 구성된 검사기 테스트

구성된 검사기를 테스트해 보겠습니다. Python 인터프리터에서 다음 코드를 실행합니다.

```python
from validate import PositiveInteger, PositiveFloat, NonEmptyString

PositiveInteger.check(10)  # Should return 10

try:
    PositiveInteger.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    PositiveInteger.check(-10)  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

NonEmptyString.check('hello')  # Should return 'hello'

try:
    NonEmptyString.check('')  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")
```

이 코드를 실행하면 다음이 표시됩니다.

```
10
Error: Expected <class 'int'>
Error: Expected >= 0
'hello'
Error: Must be non-empty
```

이것은 검사기를 결합하여 더 복잡한 유효성 검사 규칙을 만들 수 있는 방법을 보여줍니다.

테스트를 마쳤으면 다음 명령을 실행하여 Python 인터프리터를 종료할 수 있습니다.

```python
exit()
```
