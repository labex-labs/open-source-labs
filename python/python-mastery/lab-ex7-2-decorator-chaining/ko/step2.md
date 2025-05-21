# 인수를 사용하는 데코레이터 생성하기

지금까지는 항상 고정된 메시지를 출력하는 `@logged` 데코레이터를 사용했습니다. 하지만 메시지 형식을 사용자 정의하고 싶다면 어떻게 해야 할까요? 이 섹션에서는 인수를 허용하여 데코레이터를 사용하는 방식을 더욱 유연하게 만들어주는 새로운 데코레이터를 만드는 방법을 배우겠습니다.

## 매개변수화된 데코레이터 이해하기

매개변수화된 데코레이터는 특수한 유형의 함수입니다. 다른 함수를 직접 수정하는 대신 데코레이터를 반환합니다. 매개변수화된 데코레이터의 일반적인 구조는 다음과 같습니다.

```python
def decorator_with_args(arg1, arg2, ...):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use arg1, arg2, ... here
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator
```

코드에서 `@decorator_with_args(value1, value2)`를 사용하면 Python 은 먼저 `decorator_with_args(value1, value2)`를 호출합니다. 이 호출은 실제 데코레이터를 반환하며, 이 데코레이터는 `@` 구문 다음에 오는 함수에 적용됩니다. 이 두 단계 프로세스는 매개변수화된 데코레이터가 작동하는 방식의 핵심입니다.

## logformat 데코레이터 생성하기

형식 문자열을 인수로 사용하는 `@logformat(fmt)` 데코레이터를 만들어 보겠습니다. 이렇게 하면 로깅 메시지를 사용자 정의할 수 있습니다.

1. WebIDE 에서 `logcall.py`를 열고 새 데코레이터를 추가합니다. 아래 코드는 기존 `logged` 데코레이터와 새 `logformat` 데코레이터를 모두 정의하는 방법을 보여줍니다.

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

`logformat` 데코레이터에서 외부 함수 `logformat`은 형식 문자열 `fmt`를 인수로 받습니다. 그런 다음 대상 함수를 수정하는 실제 데코레이터인 `decorator` 함수를 반환합니다.

2. 이제 `sample.py`를 수정하여 새 데코레이터를 테스트해 보겠습니다. 다음 코드는 서로 다른 함수에서 `logged` 및 `logformat` 데코레이터를 모두 사용하는 방법을 보여줍니다.

```python
from logcall import logged, logformat

@logged
def add(x, y):
    "Adds two numbers"
    return x + y

@logged
def sub(x, y):
    "Subtracts y from x"
    return x - y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
    "Multiplies two numbers"
    return x * y
```

여기서 `add` 및 `sub` 함수는 `logged` 데코레이터를 사용하고, `mul` 함수는 사용자 정의 형식 문자열과 함께 `logformat` 데코레이터를 사용합니다.

3. 업데이트된 `sample.py`를 실행하여 결과를 확인합니다. 터미널을 열고 다음 명령을 실행합니다.

```bash
cd ~/project
python3 -c "import sample; print(sample.add(2, 3)); print(sample.mul(2, 3))"
```

다음과 유사한 출력을 볼 수 있습니다.

```
Calling add
5
sample.py:mul
6
```

이 출력은 `logged` 데코레이터가 예상대로 함수 이름을 출력하고, `logformat` 데코레이터가 사용자 정의 형식 문자열을 사용하여 파일 이름과 함수 이름을 출력하는 것을 보여줍니다.

## logformat 을 사용하여 logged 데코레이터 재정의하기

이제 더 유연한 `logformat` 데코레이터가 있으므로 이를 사용하여 원래 `logged` 데코레이터를 재정의할 수 있습니다. 이렇게 하면 코드를 재사용하고 일관된 로깅 형식을 유지하는 데 도움이 됩니다.

1. 다음 코드로 `logcall.py`를 업데이트합니다.

```python
from functools import wraps

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Define logged using logformat
logged = lambda func: logformat("Calling {func.__name__}")(func)
```

여기서는 람다 함수를 사용하여 `logformat` 데코레이터를 기준으로 `logged` 데코레이터를 정의합니다. 람다 함수는 함수 `func`를 가져와 특정 형식 문자열과 함께 `logformat` 데코레이터를 적용합니다.

2. 재정의된 `logged` 데코레이터가 여전히 작동하는지 테스트합니다. 터미널을 열고 다음 명령을 실행합니다.

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def greet(name):
    return f'Hello, {name}'
    
print(greet('World'))"
```

다음과 같은 출력을 볼 수 있습니다.

```
Calling greet
Hello, World
```

이는 재정의된 `logged` 데코레이터가 예상대로 작동하며, 일관된 로깅 형식을 달성하기 위해 `logformat` 데코레이터를 성공적으로 재사용했음을 보여줍니다.
