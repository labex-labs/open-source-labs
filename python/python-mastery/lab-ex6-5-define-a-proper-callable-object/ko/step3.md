# 함수 주석을 사용한 타입 유효성 검사 구현하기

Python 에서는 함수 매개변수에 타입 주석 (type annotation) 을 추가할 수 있습니다. 이러한 주석은 매개변수와 함수의 반환 값에 대한 예상 데이터 유형을 나타내는 방법으로 사용됩니다. 기본적으로 런타임에 타입을 강제하지 않지만, 유효성 검사 목적으로 사용할 수 있습니다.

예제를 살펴보겠습니다.

```python
def add(x: int, y: int) -> int:
    return x + y
```

이 코드에서 `x: int` 및 `y: int`는 매개변수 `x`와 `y`가 정수여야 함을 알려줍니다. 마지막의 `-> int`는 `add` 함수가 정수를 반환함을 나타냅니다. 이러한 타입 주석은 함수의 `__annotations__` 속성에 저장되며, 이는 매개변수 이름을 해당 주석 처리된 타입에 매핑하는 딕셔너리입니다.

이제 이러한 타입 주석을 유효성 검사에 사용하도록 `ValidatedFunction` 클래스를 개선할 것입니다. 이를 위해 Python 의 `inspect` 모듈을 사용해야 합니다. 이 모듈은 모듈, 클래스, 메서드, 함수 등과 같은 라이브 객체에 대한 정보를 얻는 데 유용한 함수를 제공합니다. 이 경우 함수 인수를 해당 매개변수 이름과 일치시키는 데 사용할 것입니다.

먼저 `validate.py` 파일에서 `ValidatedFunction` 클래스를 수정해야 합니다. 다음 명령을 사용하여 이 파일을 열 수 있습니다.

```bash
code /home/labex/project/validate.py
```

기존 `ValidatedFunction` 클래스를 다음 개선된 버전으로 바꾸십시오.

```python
import inspect

class ValidatedFunction:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __call__(self, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(*args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(*args, **kwargs)
```

이 개선된 버전이 수행하는 작업은 다음과 같습니다.

1. `inspect.signature()`를 사용하여 함수의 매개변수에 대한 정보 (예: 이름, 기본값 및 주석 처리된 타입) 를 얻습니다.
2. 시그니처의 `bind()` 메서드를 사용하여 제공된 인수를 해당 매개변수 이름과 일치시킵니다. 이렇게 하면 각 인수를 함수에서 해당 매개변수와 연결하는 데 도움이 됩니다.
3. 각 인수를 해당 타입 주석 (있는 경우) 과 비교하여 확인합니다. 주석이 발견되면 주석에서 validator 클래스를 검색하고 `check()` 메서드를 사용하여 유효성 검사를 적용합니다.
4. 마지막으로, 유효성 검사를 거친 인수를 사용하여 원래 함수를 호출합니다.

이제 타입 주석에서 validator 클래스를 사용하는 몇 가지 함수로 이 개선된 `ValidatedFunction` 클래스를 테스트해 보겠습니다. 다음 명령을 사용하여 `test_validation.py` 파일을 여십시오.

```bash
code /home/labex/project/test_validation.py
```

파일에 다음 코드를 추가하십시오.

```python
from validate import ValidatedFunction, Integer, String

def greet(name: String, times: Integer):
    return name * times

# Wrap the greet function with ValidatedFunction
validated_greet = ValidatedFunction(greet)

# Valid call
try:
    result = validated_greet("Hello ", 3)
    print(f"Valid call result: {result}")
except TypeError as e:
    print(f"Unexpected error: {e}")

# Invalid call - wrong type for 'name'
try:
    result = validated_greet(123, 3)
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for name: {e}")

# Invalid call - wrong type for 'times'
try:
    result = validated_greet("Hello ", "3")
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for times: {e}")
```

이 코드에서는 `name: String` 및 `times: Integer`의 타입 주석이 있는 `greet` 함수를 정의합니다. 즉, `name` 매개변수는 `String` 클래스를 사용하여 유효성 검사를 받아야 하고, `times` 매개변수는 `Integer` 클래스를 사용하여 유효성 검사를 받아야 합니다. 그런 다음 타입 유효성 검사를 활성화하기 위해 `greet` 함수를 `ValidatedFunction` 클래스로 래핑합니다.

세 가지 테스트 케이스를 수행합니다. 유효한 호출, `name`에 대한 잘못된 타입의 잘못된 호출, `times`에 대한 잘못된 타입의 잘못된 호출입니다. 각 호출은 유효성 검사 중에 발생할 수 있는 `TypeError` 예외를 catch 하기 위해 `try-except` 블록으로 래핑됩니다.

테스트 파일을 실행하려면 다음 명령을 사용하십시오.

```bash
python3 /home/labex/project/test_validation.py
```

다음과 유사한 출력을 볼 수 있습니다.

```
Valid call result: Hello Hello Hello
Expected error for name: Expected <class 'str'>
Expected error for times: Expected <class 'int'>
```

이 출력은 `ValidatedFunction` 호출 가능 객체가 이제 함수 주석을 기반으로 타입 유효성 검사를 적용하고 있음을 보여줍니다. 잘못된 타입의 인수를 전달하면 validator 클래스가 오류를 감지하고 `TypeError`를 발생시킵니다. 이러한 방식으로 함수가 올바른 데이터 타입으로 호출되도록 하여 버그를 방지하고 코드를 더욱 강력하게 만들 수 있습니다.
