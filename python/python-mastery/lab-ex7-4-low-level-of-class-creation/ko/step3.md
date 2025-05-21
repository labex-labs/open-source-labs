# 효율적인 클래스 생성

이제 `type()` 함수를 사용하여 클래스를 생성하는 방법을 이해했으므로, 여러 개의 유사한 클래스를 생성하는 더 효율적인 방법을 살펴보겠습니다. 이 방법은 시간을 절약하고 코드 중복을 줄여 프로그래밍 프로세스를 더욱 원활하게 만듭니다.

## 현재 유효성 검사기 클래스 이해

먼저 WebIDE 에서 `validate.py` 파일을 열어야 합니다. 이 파일에는 이미 여러 유효성 검사기 클래스가 포함되어 있으며, 이는 값이 특정 조건을 충족하는지 확인하는 데 사용됩니다. 이러한 클래스에는 `Validator`, `Positive`, `PositiveInteger`, `PositiveFloat`가 포함됩니다. 이 파일에 `Typed` 기본 클래스와 여러 형식 관련 유효성 검사기를 추가할 것입니다.

파일을 열려면 터미널에서 다음 명령을 실행합니다.

```bash
cd ~/project
```

## Typed 유효성 검사기 클래스 추가

`Typed` 유효성 검사기 클래스를 추가하는 것으로 시작해 보겠습니다. 이 클래스는 값이 예상되는 형식인지 확인하는 데 사용됩니다.

```python
class Typed(Validator):
    expected_type = object  # Default, will be overridden in subclasses

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        super().check(value)
```

이 코드에서 `expected_type`은 기본적으로 `object`로 설정됩니다. 하위 클래스는 이를 확인하려는 특정 형식으로 재정의합니다. `check` 메서드는 `isinstance` 함수를 사용하여 값이 예상되는 형식인지 확인합니다. 그렇지 않은 경우 `TypeError`를 발생시킵니다.

기존에는 다음과 같이 형식 관련 유효성 검사기를 생성했습니다.

```python
class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

그러나 이 접근 방식은 반복적입니다. `type()` 생성자를 사용하여 이러한 클래스를 동적으로 생성하여 더 나은 결과를 얻을 수 있습니다.

## 형식 유효성 검사기 동적 생성

개별 클래스 정의를 보다 효율적인 접근 방식으로 대체합니다.

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str)
]

globals().update((name, type(name, (Typed,), {'expected_type': ty}))
                 for name, ty in _typed_classes)
```

이 코드가 수행하는 작업은 다음과 같습니다.

1. 튜플 목록을 정의합니다. 각 튜플에는 클래스 이름과 해당 Python 형식이 포함되어 있습니다.
2. `type()` 함수와 함께 제너레이터 표현식을 사용하여 각 클래스를 생성합니다. `type()` 함수는 클래스 이름, 기본 클래스 튜플 및 클래스 속성의 딕셔너리, 이렇게 세 개의 인수를 사용합니다.
3. `globals().update()`를 사용하여 새로 생성된 클래스를 전역 네임스페이스에 추가합니다. 이렇게 하면 모듈 전체에서 클래스에 액세스할 수 있습니다.

완성된 `validate.py` 파일은 다음과 같이 표시됩니다.

```python
# Basic validator classes

class Validator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.name] = value

    @classmethod
    def check(cls, value):
        pass

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value <= 0:
            raise ValueError('Expected a positive value')
        super().check(value)

class PositiveInteger(Positive):
    @classmethod
    def check(cls, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        super().check(value)

class PositiveFloat(Positive):
    @classmethod
    def check(cls, value):
        if not isinstance(value, float):
            raise TypeError('Expected a float')
        super().check(value)

class Typed(Validator):
    expected_type = object  # Default, will be overridden in subclasses

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        super().check(value)

# Generate type validators dynamically
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str)
]

globals().update((name, type(name, (Typed,), {'expected_type': ty}))
                 for name, ty in _typed_classes)
```

## 동적으로 생성된 클래스 테스트

이제 동적으로 생성된 유효성 검사기 클래스를 테스트해 보겠습니다. 먼저 Python 대화형 셸을 엽니다.

```bash
cd ~/project
python3
```

Python 셸에 들어가면 유효성 검사기를 가져와 테스트합니다.

```python
from validate import Integer, Float, String

# Test the Integer validator
i = Integer()
i.__set_name__(None, 'test_int')
try:
    i.check("not an integer")
    print("Error: Check passed when it should have failed")
except TypeError as e:
    print(f"Integer validation: {e}")

# Test the String validator
s = String()
s.__set_name__(None, 'test_str')
try:
    s.check(123)
    print("Error: Check passed when it should have failed")
except TypeError as e:
    print(f"String validation: {e}")

# Add a new validator class to the list
import sys
print("Current validator classes:", [cls for cls in dir() if cls in ['Integer', 'Float', 'String']])
```

형식 유효성 검사 오류를 보여주는 출력이 표시됩니다. 이는 동적으로 생성된 클래스가 올바르게 작동하고 있음을 나타냅니다.

테스트를 마쳤으면 Python 셸을 종료합니다.

```python
exit()
```

## 동적 클래스 생성 확장

더 많은 형식 유효성 검사기를 추가하려면 `validate.py`에서 `_typed_classes` 목록을 업데이트하면 됩니다.

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str),
    ('List', list),
    ('Dict', dict),
    ('Bool', bool)
]
```

이 접근 방식은 반복적인 코드를 작성하지 않고 여러 개의 유사한 클래스를 생성하는 강력하고 효율적인 방법을 제공합니다. 요구 사항이 증가함에 따라 애플리케이션을 쉽게 확장할 수 있습니다.
