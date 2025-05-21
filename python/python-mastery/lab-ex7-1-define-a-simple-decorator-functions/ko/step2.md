# 유효성 검사 데코레이터 구축하기

이 단계에서는 더 실용적인 데코레이터를 만들 것입니다. Python 의 데코레이터는 다른 함수의 동작을 수정할 수 있는 특수한 유형의 함수입니다. 우리가 만들 데코레이터는 타입 어노테이션 (type annotation) 을 기반으로 함수 인수를 검증합니다. 타입 어노테이션은 함수의 인수와 반환 값에 대해 예상되는 데이터 유형을 지정하는 방법입니다. 이는 함수가 올바른 입력 유형을 수신하도록 보장하여 많은 버그를 방지하는 데 도움이 되므로 실제 응용 프로그램에서 일반적인 사용 사례입니다.

## 유효성 검사 클래스 이해하기

이미 `validate.py`라는 파일을 만들었으며, 여기에는 몇 가지 유효성 검사 클래스가 포함되어 있습니다. 유효성 검사 클래스는 값이 특정 기준을 충족하는지 확인하는 데 사용됩니다. 이 파일의 내용을 보려면 VSCode 편집기에서 열어야 합니다. 터미널에서 다음 명령을 실행하여 이 작업을 수행할 수 있습니다.

```bash
cd /home/labex/project
code validate.py
```

이 파일에는 세 개의 클래스가 있습니다.

1. `Validator` - 이것은 기본 클래스입니다. 기본 클래스는 다른 클래스가 상속할 수 있는 일반적인 프레임워크 또는 구조를 제공합니다. 이 경우 유효성 검사를 위한 기본 구조를 제공합니다.
2. `Integer` - 이 유효성 검사기 클래스는 값이 정수인지 확인하는 데 사용됩니다. 이 유효성 검사기를 사용하는 함수에 정수가 아닌 값을 전달하면 오류가 발생합니다.
3. `PositiveInteger` - 이 유효성 검사기 클래스는 값이 양의 정수인지 확인합니다. 따라서 음의 정수 또는 0 을 전달하면 오류가 발생합니다.

## 유효성 검사 데코레이터 추가하기

이제 `validate.py` 파일에 `validated`라는 데코레이터 함수를 추가할 것입니다. 이 데코레이터는 몇 가지 중요한 작업을 수행합니다.

1. 함수의 타입 어노테이션을 검사합니다. 타입 어노테이션은 함수가 어떤 종류의 데이터를 예상하는지 알려주는 작은 메모와 같습니다.
2. 이러한 타입 어노테이션에 대해 함수에 전달된 인수를 검증합니다. 즉, 함수에 전달된 값이 올바른 유형인지 확인합니다.
3. 또한 함수의 반환 값을 해당 어노테이션에 대해 검증합니다. 따라서 함수가 반환해야 하는 데이터 유형을 반환하는지 확인합니다.
4. 유효성 검사가 실패하면 유용한 오류 메시지를 발생시킵니다. 이러한 메시지는 어떤 인수에 잘못된 유형이 있는지와 같이 정확히 무엇이 잘못되었는지 알려줍니다.

`validate.py` 파일의 끝에 다음 코드를 추가합니다.

```python
# Add to validate.py

import inspect
import functools

def validated(func):
    sig = inspect.signature(func)

    print(f'Validating {func.__name__} {sig}')

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Bind arguments to the signature
        bound = sig.bind(*args, **kwargs)
        errors = []

        # Validate each argument
        for name, value in bound.arguments.items():
            if name in sig.parameters:
                param = sig.parameters[name]
                if param.annotation != inspect.Parameter.empty:
                    try:
                        # Create an instance of the validator and validate the value
                        if isinstance(param.annotation, type) and issubclass(param.annotation, Validator):
                            validator = param.annotation()
                            bound.arguments[name] = validator.validate(value)
                    except Exception as e:
                        errors.append(f'    {name}: {e}')

        # If validation errors, raise an exception
        if errors:
            raise TypeError('Bad Arguments\n' + '\n'.join(errors))

        # Call the function
        result = func(*bound.args, **bound.kwargs)

        # Validate the return value
        if sig.return_annotation != inspect.Signature.empty:
            try:
                if isinstance(sig.return_annotation, type) and issubclass(sig.return_annotation, Validator):
                    validator = sig.return_annotation()
                    result = validator.validate(result)
            except Exception as e:
                raise TypeError(f'Bad return: {e}') from None

        return result

    return wrapper
```

이 코드는 Python 의 `inspect` 모듈을 사용합니다. `inspect` 모듈을 사용하면 함수와 같은 라이브 객체에 대한 정보를 얻을 수 있습니다. 여기서는 함수의 시그니처를 검사하고 타입 어노테이션을 기반으로 인수를 검증하는 데 사용합니다. 또한 `functools.wraps`를 사용합니다. 이것은 이름과 docstring 과 같은 원래 함수의 메타데이터를 보존하는 도우미 함수입니다. 메타데이터는 함수가 수행하는 작업을 이해하는 데 도움이 되는 함수에 대한 추가 정보와 같습니다.

## 유효성 검사 데코레이터 테스트하기

유효성 검사 데코레이터를 테스트할 파일을 만들어 보겠습니다. `test_validate.py`라는 새 파일을 만들고 다음 코드를 추가합니다.

```python
# test_validate.py

from validate import Integer, PositiveInteger, validated

@validated
def add(x: Integer, y: Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y: Integer) -> Integer:
    return x ** y

# Test with a class
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

이제 Python 인터프리터에서 데코레이터를 테스트해 보겠습니다. 먼저 프로젝트 디렉토리로 이동하여 터미널에서 다음 명령을 실행하여 Python 인터프리터를 시작합니다.

```bash
cd /home/labex/project
python3
```

그런 다음 Python 인터프리터에서 다음 코드를 실행하여 데코레이터를 테스트할 수 있습니다.

```python
>>> from test_validate import add, pow, Stock
Validating add (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating pow (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating sell (self, nshares: validate.PositiveInteger) -> <class 'inspect._empty'>
>>>
>>> # Test with valid inputs
>>> add(2, 3)
5
>>>
>>> # Test with invalid inputs
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>
>>>
>>> # Test valid power
>>> pow(2, 3)
8
>>>
>>> # Test with negative exponent (produces non - integer result)
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
>>> # Test with a class
>>> s = Stock("GOOG", 100, 490.1)
>>> s.sell(50)
>>> s.shares
50
>>>
>>> # Test with invalid shares
>>> s.sell(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    nshares: Expected value > 0
>>> exit()
```

보시다시피 `validated` 데코레이터는 함수 인수 및 반환 값에 대한 타입 검사를 성공적으로 적용했습니다. 이는 코드를 더 강력하게 만들기 때문에 매우 유용합니다. 타입 오류가 코드 깊숙이 전파되어 찾기 어려운 버그를 일으키도록 하는 대신, 함수 경계에서 이를 포착합니다.
