# Validator 클래스 이해하기

이 랩에서는 호출 가능 객체를 생성하기 위해 일련의 validator 클래스를 기반으로 구축할 것입니다. 구축을 시작하기 전에 `validate.py` 파일에 제공된 validator 클래스를 이해하는 것이 중요합니다. 이러한 클래스는 코드의 예상대로 작동하는지 확인하는 데 중요한 부분인 타입 검사 (type checking) 를 수행하는 데 도움이 됩니다.

WebIDE 에서 `validate.py` 파일을 열어 시작해 보겠습니다. 이 파일에는 우리가 사용할 validator 클래스에 대한 코드가 포함되어 있습니다. 파일을 열려면 터미널에서 다음 명령을 실행하십시오.

```bash
code /home/labex/project/validate.py
```

파일을 열면 여러 클래스가 포함되어 있는 것을 볼 수 있습니다. 각 클래스가 수행하는 작업에 대한 간략한 개요는 다음과 같습니다.

1. `Validator`: 이것은 기본 클래스입니다. `check` 메서드가 있지만, 현재 이 메서드는 아무 작업도 수행하지 않습니다. 다른 validator 클래스의 시작점으로 사용됩니다.
2. `Typed`: 이것은 `Validator`의 서브클래스입니다. 주요 역할은 값이 특정 유형인지 확인하는 것입니다.
3. `Integer`, `Float`, 및 `String`: 이들은 `Typed`에서 상속되는 특정 타입 validator 입니다. 각각 값이 정수, 부동 소수점 또는 문자열인지 확인하도록 설계되었습니다.

이제 이러한 validator 클래스가 실제로 어떻게 작동하는지 살펴보겠습니다. 이를 테스트하기 위해 `test.py`라는 새 파일을 만들 것입니다. 이 파일을 생성하고 열려면 다음 명령을 실행하십시오.

```bash
code /home/labex/project/test.py
```

`test.py` 파일이 열리면 다음 코드를 추가하십시오. 이 코드는 `Integer` 및 `String` validator 를 테스트합니다.

```python
from validate import Integer, String, Float

# Test Integer validator
print("Testing Integer validator:")
try:
    Integer.check(42)
    print("✓ Integer check passed for 42")
except TypeError as e:
    print(f"✗ Error: {e}")

try:
    Integer.check("Hello")
    print("✗ Integer check incorrectly passed for 'Hello'")
except TypeError as e:
    print(f"✓ Correctly raised error: {e}")

# Test String validator
print("\nTesting String validator:")
try:
    String.check("Hello")
    print("✓ String check passed for 'Hello'")
except TypeError as e:
    print(f"✗ Error: {e}")
```

이 코드에서는 먼저 `validate.py` 파일에서 `Integer`, `String`, 및 `Float` validator 를 가져옵니다. 그런 다음 정수 값 (`42`) 과 문자열 값 (`"Hello"`) 을 확인하여 `Integer` validator 를 테스트합니다. 정수에 대한 검사가 통과하면 성공 메시지를 출력합니다. 문자열에 대해 잘못 통과하면 오류 메시지를 출력합니다. 문자열에 대해 검사가 `TypeError`를 올바르게 발생시키면 성공 메시지를 출력합니다. `String` validator 에 대해서도 유사한 테스트를 수행합니다.

코드를 추가한 후 다음 명령을 사용하여 테스트 파일을 실행하십시오.

```bash
python3 /home/labex/project/test.py
```

다음과 유사한 출력을 볼 수 있습니다.

```
Testing Integer validator:
✓ Integer check passed for 42
✓ Correctly raised error: Expected <class 'int'>

Testing String validator:
✓ String check passed for 'Hello'
```

보시다시피, 이러한 validator 클래스를 사용하면 타입 검사를 쉽게 수행할 수 있습니다. 예를 들어, `Integer.check(x)`를 호출하면 `x`가 정수가 아닌 경우 `TypeError`가 발생합니다.

이제 실제 시나리오를 생각해 보겠습니다. 인수가 특정 유형이어야 하는 함수가 있다고 가정해 보겠습니다. 다음은 그러한 함수의 예입니다.

```python
def add(x, y):
    Integer.check(x)  # Make sure x is an integer
    Integer.check(y)  # Make sure y is an integer
    return x + y
```

이 함수는 작동하지만 문제가 있습니다. 타입 검사를 사용하고 싶을 때마다 수동으로 validator 검사를 추가해야 합니다. 특히 더 큰 함수나 프로젝트의 경우 시간이 많이 걸리고 오류가 발생하기 쉽습니다.

다음 단계에서는 호출 가능 객체를 생성하여 이 문제를 해결할 것입니다. 이 객체는 함수 주석 (function annotations) 을 기반으로 이러한 타입 검사를 자동으로 적용할 수 있습니다. 이렇게 하면 매번 검사를 수동으로 추가할 필요가 없습니다.
