# 기본 호출 가능 객체 생성하기

Python 에서 호출 가능 객체 (callable object) 는 함수처럼 사용할 수 있는 객체입니다. 일반 함수를 호출하는 방식과 유사하게, 괄호를 붙여서 "호출"할 수 있는 것으로 생각할 수 있습니다. Python 에서 클래스가 호출 가능 객체처럼 작동하게 하려면 `__call__`이라는 특수 메서드를 구현해야 합니다. 이 메서드는 함수를 호출할 때와 마찬가지로, 괄호와 함께 객체를 사용할 때 자동으로 호출됩니다.

`validate.py` 파일을 수정하여 시작해 보겠습니다. 이 파일에 `ValidatedFunction`이라는 새 클래스를 추가할 것이며, 이 클래스가 우리의 호출 가능 객체가 될 것입니다. 코드 편집기에서 파일을 열려면 터미널에서 다음 명령을 실행하십시오.

```bash
code /home/labex/project/validate.py
```

파일이 열리면 파일 끝으로 스크롤하여 다음 코드를 추가하십시오.

```python
class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        result = self.func(*args, **kwargs)
        return result
```

이 코드가 무엇을 하는지 자세히 살펴보겠습니다. `ValidatedFunction` 클래스에는 생성자인 `__init__` 메서드가 있습니다. 이 클래스의 인스턴스를 생성할 때 함수를 전달합니다. 이 함수는 `self.func`라는 인스턴스의 속성으로 저장됩니다.

`__call__` 메서드는 이 클래스를 호출 가능하게 만드는 핵심 부분입니다. `ValidatedFunction` 클래스의 인스턴스를 호출하면 이 `__call__` 메서드가 실행됩니다. 단계별로 살펴보면 다음과 같습니다.

1. 호출되는 함수를 알려주는 메시지를 출력합니다. 이는 디버깅 및 진행 상황 이해에 유용합니다.
2. 인스턴스를 호출할 때 전달한 인수를 사용하여 `self.func`에 저장된 함수를 호출합니다. `*args` 및 `**kwargs`를 사용하면 임의의 수의 위치 및 키워드 인수를 전달할 수 있습니다.
3. 함수 호출의 결과를 반환합니다.

이제 이 `ValidatedFunction` 클래스를 테스트해 보겠습니다. 테스트 코드를 작성하기 위해 `test_callable.py`라는 새 파일을 만들 것입니다. 코드 편집기에서 이 새 파일을 열려면 다음 명령을 실행하십시오.

```bash
code /home/labex/project/test_callable.py
```

`test_callable.py` 파일에 다음 코드를 추가하십시오.

```python
from validate import ValidatedFunction

def add(x, y):
    return x + y

# Wrap the add function with ValidatedFunction
validated_add = ValidatedFunction(add)

# Call the wrapped function
result = validated_add(2, 3)
print(f"Result: {result}")

# Try another call
result = validated_add(10, 20)
print(f"Result: {result}")
```

이 코드에서는 먼저 `validate.py` 파일에서 `ValidatedFunction` 클래스를 가져옵니다. 그런 다음 두 개의 숫자를 받아 합계를 반환하는 `add`라는 간단한 함수를 정의합니다.

`add` 함수를 전달하여 `ValidatedFunction` 클래스의 인스턴스를 생성합니다. 이렇게 하면 `add` 함수가 `ValidatedFunction` 인스턴스 내부에 "래핑"됩니다.

그런 다음 래핑된 함수를 두 번 호출합니다. 한 번은 인수 `2`와 `3`으로, 다른 한 번은 `10`과 `20`으로 호출합니다. 래핑된 함수를 호출할 때마다 `ValidatedFunction` 클래스의 `__call__` 메서드가 호출되고, 이 메서드는 다시 원래의 `add` 함수를 호출합니다.

테스트 코드를 실행하려면 터미널에서 다음 명령을 실행하십시오.

```bash
python3 /home/labex/project/test_callable.py
```

다음과 유사한 출력을 볼 수 있습니다.

```
Calling <function add at 0x7f2d1c3a9940>
Result: 5
Calling <function add at 0x7f2d1c3a9940>
Result: 30
```

이 출력은 우리의 호출 가능 객체가 예상대로 작동하고 있음을 보여줍니다. `validated_add(2, 3)`을 호출하면 실제로 `ValidatedFunction` 클래스의 `__call__` 메서드를 호출하고, 이 메서드는 원래의 `add` 함수를 호출합니다.

현재 `ValidatedFunction` 클래스는 메시지를 출력하고 호출을 원래 함수로 전달하기만 합니다. 다음 단계에서는 함수의 주석 (annotations) 을 기반으로 타입 유효성 검사를 수행하도록 이 클래스를 개선할 것입니다.
