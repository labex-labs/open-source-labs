# 데코레이터에서 함수 메타데이터 보존하기

Python 에서 데코레이터는 함수의 동작을 수정할 수 있는 강력한 도구입니다. 하지만 데코레이터를 사용하여 함수를 래핑 (wrapping) 하면 작은 문제가 발생합니다. 기본적으로 원래 함수의 메타데이터, 즉 이름, 문서 문자열 (docstring), 그리고 어노테이션 (annotations) 이 손실됩니다. 메타데이터는 코드의 구조를 검사하는 인트로스펙션 (introspection) 과 문서를 생성하는 데 중요합니다. 먼저 이 문제를 확인해 보겠습니다.

WebIDE 에서 터미널을 엽니다. 데코레이터를 사용할 때 어떤 일이 발생하는지 확인하기 위해 몇 가지 Python 명령을 실행합니다. 다음 명령은 데코레이터로 래핑된 간단한 함수 `add`를 생성한 다음 함수와 docstring 을 출력합니다.

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

이 명령을 실행하면 다음과 유사한 출력이 표시됩니다.

```
<function wrapper at 0x...>
None
```

함수 이름이 `add` 대신 `wrapper`로 표시되는 것을 확인할 수 있습니다. 그리고 docstring 은 `'Adds two things'`여야 하지만 `None`입니다. 이는 인트로스펙션 도구 또는 문서 생성기와 같이 이 메타데이터에 의존하는 도구를 사용할 때 큰 문제가 될 수 있습니다.

## functools.wraps 로 문제 해결하기

Python 의 `functools` 모듈이 해결책을 제시합니다. 이 모듈은 함수 메타데이터를 보존하는 데 도움이 되는 `wraps` 데코레이터를 제공합니다. `logged` 데코레이터를 수정하여 `wraps`를 사용하는 방법을 살펴보겠습니다.

1. 먼저 WebIDE 에서 `logcall.py` 파일을 엽니다. 터미널에서 다음 명령을 사용하여 프로젝트 디렉토리로 이동할 수 있습니다.

```bash
cd ~/project
```

2. 이제 `logcall.py`에서 `logged` 데코레이터를 다음 코드로 업데이트합니다. 여기에서 `@wraps(func)` 데코레이터가 핵심입니다. 이 데코레이터는 원래 함수 `func`의 모든 메타데이터를 래퍼 함수로 복사합니다.

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

3. `@wraps(func)` 데코레이터는 중요한 역할을 합니다. 원래 함수 `func`에서 모든 메타데이터 (이름, docstring, 어노테이션 등) 를 가져와 `wrapper` 함수에 연결합니다. 이렇게 하면 데코레이팅된 함수를 사용할 때 올바른 메타데이터를 갖게 됩니다.

4. 개선된 데코레이터를 테스트해 보겠습니다. 터미널에서 다음 명령을 실행합니다.

```bash
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

이제 다음을 볼 수 있습니다.

```
<function add at 0x...>
Adds two things
```

훌륭합니다! 함수 이름과 docstring 이 보존되었습니다. 즉, 데코레이터가 예상대로 작동하며 원래 함수의 메타데이터가 그대로 유지됩니다.

## validate.py 데코레이터 수정하기

이제 `validate.py`의 `validated` 데코레이터에 동일한 수정을 적용해 보겠습니다. 이 데코레이터는 함수의 어노테이션을 기반으로 함수 인수의 유형과 반환 값을 검증하는 데 사용됩니다.

1. WebIDE 에서 `validate.py`를 엽니다.

2. `@wraps` 데코레이터로 `validated` 데코레이터를 업데이트합니다. 다음 코드는 이를 수행하는 방법을 보여줍니다. `@wraps(func)` 데코레이터는 메타데이터를 보존하기 위해 `validated` 데코레이터 내의 `wrapper` 함수에 추가됩니다.

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
```

3. 이제 `validated` 데코레이터가 메타데이터를 보존하는지 테스트해 보겠습니다. 터미널에서 다음 명령을 실행합니다.

```bash
python3 -c "from validate import validated, Integer; @validated
def multiply(x: Integer, y: Integer) -> Integer:
    'Multiplies two integers'
    return x * y
    
print(multiply)
print(multiply.__doc__)"
```

다음과 같은 출력을 볼 수 있습니다.

```
<function multiply at 0......>
Multiplies two integers
```

이제 `logged`와 `validated` 데코레이터 모두 데코레이팅하는 함수의 메타데이터를 제대로 보존합니다. 이렇게 하면 이러한 데코레이터를 사용할 때 함수가 원래 이름, docstring 및 어노테이션을 유지하므로 코드 가독성과 유지 관리성이 매우 향상됩니다.
