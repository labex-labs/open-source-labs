# 인수를 사용하여 유형 강제 데코레이터 생성하기

이전 단계에서 `@validated` 데코레이터에 대해 배웠습니다. 이 데코레이터는 Python 함수에서 유형 주석을 적용하는 데 사용됩니다. 유형 주석은 함수 인수와 반환 값의 예상 유형을 지정하는 방법입니다. 이제 한 단계 더 나아가겠습니다. 유형 사양을 인수로 허용할 수 있는 더 유연한 데코레이터를 만들 것입니다. 즉, 각 인수와 반환 값에 대해 원하는 유형을 보다 명시적으로 정의할 수 있습니다.

## 목표 이해하기

우리의 목표는 `@enforce()` 데코레이터를 만드는 것입니다. 이 데코레이터를 사용하면 키워드 인수를 사용하여 유형 제약 조건을 지정할 수 있습니다. 작동 방식의 예는 다음과 같습니다.

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

이 예에서는 `@enforce` 데코레이터를 사용하여 `add` 함수의 `x` 및 `y` 인수가 `Integer` 유형이어야 하고 반환 값도 `Integer` 유형이어야 함을 지정합니다. 이 데코레이터는 이전 `@validated` 데코레이터와 유사하게 작동하지만 유형 사양을 더 많이 제어할 수 있습니다.

## enforce 데코레이터 생성하기

1. 먼저 WebIDE 에서 `validate.py` 파일을 엽니다. 이 파일에 새 데코레이터를 추가합니다. 추가할 코드는 다음과 같습니다.

```python
from functools import wraps

class Integer:
    @classmethod
    def __instancecheck__(cls, x):
        return isinstance(x, int)

def validated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get function annotations
        annotations = func.__annotations__
        # Check arguments against annotations
        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            if arg_name in annotations and not isinstance(arg_value, annotations[arg_name]):
                raise TypeError(f'Expected {arg_name} to be {annotations[arg_name].__name__}')

        # Run the function and get the result
        result = func(*args, **kwargs)

        # Check the return value
        if 'return' in annotations and not isinstance(result, annotations['return']):
            raise TypeError(f'Expected return value to be {annotations["return"].__name__}')

        return result
    return wrapper

def enforce(**type_specs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check argument types
            for arg_name, arg_value in zip(func.__code__.co_varnames, args):
                if arg_name in type_specs and not isinstance(arg_value, type_specs[arg_name]):
                    raise TypeError(f'Expected {arg_name} to be {type_specs[arg_name].__name__}')

            # Run the function and get the result
            result = func(*args, **kwargs)

            # Check the return value
            if 'return_' in type_specs and not isinstance(result, type_specs['return_']):
                raise TypeError(f'Expected return value to be {type_specs["return_"].__name__}')

            return result
        return wrapper
    return decorator
```

이 코드가 수행하는 작업을 분석해 보겠습니다. `Integer` 클래스는 사용자 지정 유형을 정의하는 데 사용됩니다. `validated` 데코레이터는 함수의 유형 주석을 기반으로 함수 인수와 반환 값의 유형을 확인합니다. `enforce` 데코레이터는 우리가 만들고 있는 새 데코레이터입니다. 각 인수와 반환 값에 대한 유형을 지정하는 키워드 인수를 사용합니다. `enforce` 데코레이터의 `wrapper` 함수 내부에서 인수와 반환 값의 유형이 지정된 유형과 일치하는지 확인합니다. 그렇지 않은 경우 `TypeError`를 발생시킵니다.

2. 이제 새 `@enforce` 데코레이터를 테스트해 보겠습니다. 예상대로 작동하는지 확인하기 위해 몇 가지 테스트 케이스를 실행합니다. 테스트를 실행하는 코드는 다음과 같습니다.

```bash
cd ~/project
python3 -c "from validate import enforce, Integer

@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y

# This should work
print(add(2, 3))

# This should raise a TypeError
try:
    print(add('2', 3))
except TypeError as e:
    print(f'Error: {e}')

# This should raise a TypeError
try:
    @enforce(x=Integer, y=Integer, return_=Integer)
    def bad_add(x, y):
        return str(x + y)
    print(bad_add(2, 3))
except TypeError as e:
    print(f'Error: {e}')"
```

이 테스트 코드에서는 먼저 `@enforce` 데코레이터가 있는 `add` 함수를 정의합니다. 그런 다음 오류 없이 작동해야 하는 유효한 인수로 `add` 함수를 호출합니다. 다음으로, `TypeError`를 발생시켜야 하는 잘못된 인수로 `add` 함수를 호출합니다. 마지막으로, 잘못된 유형의 값을 반환하는 `bad_add` 함수를 정의합니다. 이 함수도 `TypeError`를 발생시켜야 합니다.

이 테스트 코드를 실행하면 다음과 유사한 출력을 볼 수 있습니다.

```
5
Error: Expected x to be Integer
Error: Expected return value to be Integer
```

이 출력은 `@enforce` 데코레이터가 올바르게 작동하고 있음을 보여줍니다. 인수 또는 반환 값의 유형이 지정된 유형과 일치하지 않으면 `TypeError`를 발생시킵니다.

## 두 가지 접근 방식 비교

`@validated` 및 `@enforce` 데코레이터는 모두 유형 제약 조건을 적용하는 동일한 목표를 달성하지만 다른 방식으로 수행합니다.

1. `@validated` 데코레이터는 Python 의 내장 유형 주석을 사용합니다. 예는 다음과 같습니다.

   ```python
   @validated
   def add(x: Integer, y: Integer) -> Integer:
       return x + y
   ```

   이 접근 방식을 사용하면 유형 주석을 사용하여 함수 정의에서 직접 유형을 지정합니다. 이것은 Python 의 내장 기능이며 통합 개발 환경 (IDE) 에서 더 나은 지원을 제공합니다. IDE 는 이러한 유형 주석을 사용하여 코드 완성, 유형 검사 및 기타 유용한 기능을 제공할 수 있습니다.

2. 반면에 `@enforce` 데코레이터는 키워드 인수를 사용하여 유형을 지정합니다. 예는 다음과 같습니다.

   ```python
   @enforce(x=Integer, y=Integer, return_=Integer)
   def add(x, y):
       return x + y
   ```

   이 접근 방식은 데코레이터에 유형 사양을 직접 인수로 전달하기 때문에 더 명시적입니다. 다른 주석 시스템에 의존하는 라이브러리로 작업할 때 유용할 수 있습니다.

각 접근 방식에는 고유한 장점이 있습니다. 유형 주석은 Python 의 기본 부분이며 더 나은 IDE 지원을 제공하는 반면, `@enforce` 접근 방식은 더 많은 유연성과 명시성을 제공합니다. 작업 중인 프로젝트에 따라 요구 사항에 가장 적합한 접근 방식을 선택할 수 있습니다.
