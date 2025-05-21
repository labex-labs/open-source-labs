# 코루틴에서 `yield from` 사용하기

이 단계에서는 더 실용적인 응용 프로그램을 위해 `yield from` 문을 코루틴과 함께 사용하는 방법을 살펴보겠습니다. 코루틴은 Python 에서 강력한 개념이며, 코루틴과 함께 `yield from`을 사용하는 방법을 이해하면 코드를 크게 단순화할 수 있습니다.

## 코루틴과 메시지 전달

코루틴은 `yield` 문을 통해 값을 받을 수 있는 특수한 함수입니다. 데이터 처리 및 이벤트 처리와 같은 작업에 매우 유용합니다. `cofollow.py` 파일에는 `consumer` 데코레이터가 있습니다. 이 데코레이터는 코루틴을 자동으로 첫 번째 `yield` 지점까지 진행시켜 코루틴을 설정하는 데 도움이 됩니다. 즉, 코루틴을 수동으로 시작할 필요가 없으며 데코레이터가 이를 처리합니다.

값을 받고 해당 유형을 검증하는 코루틴을 만들어 보겠습니다. 방법은 다음과 같습니다.

1. 먼저, 편집기에서 `cofollow.py` 파일을 엽니다. 터미널에서 다음 명령을 사용하여 올바른 디렉토리로 이동할 수 있습니다.

```bash
cd /home/labex/project
```

2. 다음으로, `cofollow.py` 파일의 끝에 다음 `receive` 함수를 추가합니다. 이 함수는 메시지를 받고 해당 유형을 검증하는 코루틴입니다.

```python
def receive(expected_type):
    """
    A coroutine that receives a message and validates its type.
    Returns the received message if it matches the expected type.
    """
    msg = yield
    assert isinstance(msg, expected_type), f'Expected type {expected_type}'
    return msg
```

이 함수는 다음을 수행합니다.

- 표현식 없이 `yield`를 사용하여 값을 받습니다. 코루틴에 값이 전송되면 이 `yield` 문이 해당 값을 캡처합니다.
- `isinstance` 함수를 사용하여 수신된 값이 예상 유형인지 확인합니다. 유형이 일치하지 않으면 `AssertionError`를 발생시킵니다.
- 유형 검사가 통과하면 값을 반환합니다.

3. 이제 `receive` 함수와 함께 `yield from`을 사용하는 코루틴을 만들어 보겠습니다. 이 새로운 코루틴은 정수만 받고 출력합니다.

```python
@consumer
def print_ints():
    """
    A coroutine that receives and prints integers only.
    Uses yield from to delegate to the receive coroutine.
    """
    while True:
        val = yield from receive(int)
        print('Got:', val)
```

4. 이 코루틴을 테스트하려면 Python 셸을 열고 다음 코드를 실행합니다.

```python
from cofollow import print_ints

p = print_ints()
p.send(42)
p.send(13)
try:
    p.send('13')  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

다음과 같은 출력이 표시됩니다.

```
Got: 42
Got: 13
Error: Expected type <class 'int'>
```

## 코루틴에서 `yield from`이 작동하는 방식 이해하기

`print_ints` 코루틴에서 `yield from receive(int)`를 사용하면 다음 단계가 발생합니다.

1. 제어가 `receive` 코루틴으로 위임됩니다. 즉, `print_ints` 코루틴이 일시 중지되고 `receive` 코루틴이 실행을 시작합니다.
2. `receive` 코루틴은 `yield`를 사용하여 값을 받습니다. 값의 전송을 기다립니다.
3. `print_ints`로 값이 전송되면 실제로 `receive`에서 받습니다. `yield from` 문은 `print_ints`에서 `receive`로 값을 전달하는 역할을 합니다.
4. `receive` 코루틴은 수신된 값의 유형을 검증합니다. 유형이 올바르면 값을 반환합니다.
5. 반환된 값은 `print_ints` 코루틴의 `yield from` 표현식의 결과가 됩니다. 즉, `print_ints`의 `val` 변수에는 `receive`에서 반환된 값이 할당됩니다.

`yield from`을 사용하면 yielding 및 receiving 을 직접 처리해야 하는 경우보다 코드를 더 읽기 쉽게 만들 수 있습니다. 코루틴 간의 값 전달의 복잡성을 추상화합니다.

## 더 발전된 유형 검사 코루틴 만들기

더 복잡한 유형 검증을 처리하도록 유틸리티 함수를 확장해 보겠습니다. 방법은 다음과 같습니다.

1. 다음 함수를 `cofollow.py` 파일에 추가합니다.

```python
def receive_dict():
    """Receive and validate a dictionary"""
    result = yield from receive(dict)
    return result

def receive_str():
    """Receive and validate a string"""
    result = yield from receive(str)
    return result

@consumer
def process_data():
    """Process different types of data using the receive utilities"""
    while True:
        print("Waiting for a string...")
        name = yield from receive_str()
        print(f"Got string: {name}")

        print("Waiting for a dictionary...")
        data = yield from receive_dict()
        print(f"Got dictionary with {len(data)} items: {data}")

        print("Processing complete for this round.")
```

2. 새 코루틴을 테스트하려면 Python 셸을 열고 다음 코드를 실행합니다.

```python
from cofollow import process_data

proc = process_data()
proc.send("John Doe")
proc.send({"age": 30, "city": "New York"})
proc.send("Jane Smith")
try:
    proc.send(123)  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

다음과 같은 출력이 표시됩니다.

```
Waiting for a string...
Got string: John Doe
Waiting for a dictionary...
Got dictionary with 2 items: {'age': 30, 'city': 'New York'}
Processing complete for this round.
Waiting for a string...
Got string: Jane Smith
Waiting for a dictionary...
Error: Expected type <class 'dict'>
```

`yield from` 문은 코드를 더 깔끔하고 읽기 쉽게 만듭니다. 코루틴 간의 메시지 전달 세부 사항에 얽매이지 않고 프로그램의 상위 수준 논리에 집중할 수 있습니다.
