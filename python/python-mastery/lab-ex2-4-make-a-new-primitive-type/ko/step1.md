# 기본 MutInt 클래스 생성

가변 정수형 (Mutable Integer type) 에 대한 기본 클래스를 생성하는 것으로 시작해 보겠습니다. 프로그래밍에서 클래스는 객체를 생성하기 위한 청사진과 같습니다. 이 단계에서는 새로운 기본형의 기초를 만들 것입니다. 기본형은 프로그래밍 언어에서 제공하는 기본적인 데이터 유형이며, 여기서는 사용자 정의 기본형을 직접 만들 것입니다.

1. WebIDE 를 열고 `/home/labex/project` 디렉토리로 이동합니다. WebIDE 는 코드를 작성, 편집 및 실행할 수 있는 통합 개발 환경입니다. 이 디렉토리로 이동하면 모든 파일이 한 곳에 정리되고 서로 제대로 상호 작용할 수 있습니다.

2. 설정 단계에서 생성된 `mutint.py` 파일을 엽니다. 이 파일은 `MutInt` 클래스 정의의 중심이 될 것입니다.

3. 기본 `MutInt` 클래스를 정의하기 위해 다음 코드를 추가합니다.

```python
# mutint.py

class MutInt:
    """
    생성 후 값을 수정할 수 있는 가변 정수 클래스입니다.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """정수 값으로 초기화합니다."""
        self.value = value
```

`__slots__` 속성은 이 클래스가 가질 수 있는 속성을 정의하는 데 사용됩니다. 속성은 클래스의 객체에 속하는 변수와 같습니다. `__slots__`를 사용하면 Python 에게 속성을 저장하는 데 더 메모리 효율적인 방법을 사용하도록 지시합니다. 이 경우, `MutInt` 클래스는 `value`라는 단일 속성만 갖게 됩니다. 즉, `MutInt` 클래스의 각 객체는 정수 값인 하나의 데이터 조각만 저장할 수 있습니다.

`__init__` 메서드는 클래스의 생성자입니다. 생성자는 클래스의 객체가 생성될 때 호출되는 특수한 메서드입니다. 값 매개변수를 받아 인스턴스의 `value` 속성에 저장합니다. 인스턴스는 클래스 청사진에서 생성된 개별 객체입니다.

클래스를 테스트하기 위해 Python 스크립트를 생성하여 사용해 보겠습니다.

4. 동일한 디렉토리에 `test_mutint.py`라는 새 파일을 생성합니다.

```python
# test_mutint.py

from mutint import MutInt

# MutInt 객체 생성
a = MutInt(3)
print(f"Created MutInt with value: {a.value}")

# 값 수정 (가변성 시연)
a.value = 42
print(f"Modified value to: {a.value}")

# 더하기 시도 (실패할 것입니다)
try:
    result = a + 10
    print(f"Result of a + 10: {result}")
except TypeError as e:
    print(f"Error when adding: {e}")
```

이 테스트 스크립트에서는 먼저 `mutint.py` 파일에서 `MutInt` 클래스를 가져옵니다. 그런 다음 초기 값이 3 인 `MutInt` 클래스의 객체를 생성합니다. 초기 값을 출력한 다음 42 로 수정하고 새 값을 출력합니다. 마지막으로, `MutInt` 객체에 10 을 더하려고 시도합니다. 이는 클래스가 아직 더하기 연산을 지원하지 않기 때문에 오류가 발생합니다.

5. 터미널에서 다음 명령을 실행하여 테스트 스크립트를 실행합니다.

```bash
python3 /home/labex/project/test_mutint.py
```

터미널은 시스템 및 코드와 상호 작용하기 위해 다양한 명령을 실행할 수 있는 명령줄 인터페이스입니다. 이 명령을 실행하면 `test_mutint.py` 스크립트가 실행됩니다.

다음과 유사한 출력을 볼 수 있습니다.

```
Created MutInt with value: 3
Modified value to: 42
Error when adding: unsupported operand type(s) for +: 'MutInt' and 'int'
```

`MutInt` 클래스는 값을 성공적으로 저장하고 업데이트합니다. 그러나 몇 가지 제한 사항이 있습니다.

- 인쇄 시 제대로 표시되지 않습니다.
- 덧셈과 같은 수학 연산을 지원하지 않습니다.
- 비교를 지원하지 않습니다.
- 타입 변환을 지원하지 않습니다.

다음 단계에서는 `MutInt` 클래스가 진정한 기본형처럼 동작하도록 이러한 제한 사항을 하나씩 해결할 것입니다.
