# `yield from` 문 이해하기

이 단계에서는 Python 의 `yield from` 문을 살펴보겠습니다. 이 문은 제너레이터 작업 시 강력한 도구이며, 다른 제너레이터로 작업을 위임하는 프로세스를 단순화합니다. 이 단계를 마치면 `yield from`이 무엇인지, 어떻게 작동하는지, 그리고 서로 다른 제너레이터 간의 값 전달을 어떻게 처리하는지 이해하게 될 것입니다.

## `yield from`이란 무엇인가?

`yield from` 문은 Python 3.3 에 도입되었습니다. 주요 목적은 하위 제너레이터로의 작업 위임을 단순화하는 것입니다. 하위 제너레이터는 메인 제너레이터가 작업을 위임할 수 있는 또 다른 제너레이터입니다.

일반적으로 제너레이터가 다른 제너레이터에서 값을 yield 하도록 하려면 루프를 사용해야 합니다. 예를 들어, `yield from`이 없으면 다음과 같은 코드를 작성합니다.

```python
def delegating_generator():
    for value in subgenerator():
        yield value
```

이 코드에서 `delegating_generator`는 `for` 루프를 사용하여 `subgenerator`가 생성한 값을 반복하고 각 값을 하나씩 yield 합니다.

그러나 `yield from` 문을 사용하면 코드가 훨씬 간단해집니다.

```python
def delegating_generator():
    yield from subgenerator()
```

이 한 줄의 코드는 이전 예제의 루프와 동일한 결과를 얻습니다. 하지만 `yield from`은 단순한 단축키가 아닙니다. 또한 호출자와 하위 제너레이터 간의 양방향 통신을 관리합니다. 즉, 위임 제너레이터로 전송된 모든 값은 하위 제너레이터로 직접 전달됩니다.

## 기본 예제

`yield from`이 실제로 어떻게 작동하는지 확인하기 위해 간단한 예제를 만들어 보겠습니다.

1. 먼저, 편집기에서 `cofollow.py` 파일을 열어야 합니다. 이렇게 하려면 `cd` 명령을 사용하여 올바른 디렉토리로 이동합니다. 터미널에서 다음 명령을 실행합니다.

```bash
cd /home/labex/project
```

2. 다음으로, `cofollow.py` 파일에 두 개의 함수를 추가합니다. `subgen` 함수는 0 부터 4 까지의 숫자를 yield 하는 간단한 제너레이터입니다. `main_gen` 함수는 `yield from`을 사용하여 이러한 숫자의 생성을 `subgen`에 위임한 다음 문자열 `'Done'`을 yield 합니다. 다음 코드를 `cofollow.py` 파일의 끝에 추가합니다.

```python
def subgen():
    for i in range(5):
        yield i

def main_gen():
    yield from subgen()
    yield 'Done'
```

3. 이제 이러한 함수를 테스트해 보겠습니다. Python 셸을 열고 다음 코드를 실행합니다.

```python
from cofollow import subgen, main_gen

# Test subgen directly
for x in subgen():
    print(x)

# Test main_gen that delegates to subgen
for x in main_gen():
    print(x)
```

이 코드를 실행하면 다음과 같은 출력이 표시됩니다.

```
0
1
2
3
4

0
1
2
3
4
Done
```

이 출력은 `yield from`을 통해 `main_gen`이 `subgen`에서 생성된 모든 값을 호출자에게 직접 전달할 수 있음을 보여줍니다.

## `yield from`을 사용한 값 전달

`yield from`의 가장 강력한 기능 중 하나는 양방향으로 값 전달을 처리하는 능력입니다. 이를 보여주기 위해 더 복잡한 예제를 만들어 보겠습니다.

1. 다음 함수를 `cofollow.py` 파일에 추가합니다.

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

def caller():
    acc = accumulator()
    yield from acc
    yield 'Total accumulated'
```

`accumulator` 함수는 실행 중인 합계를 추적하는 코루틴입니다. 현재 합계를 yield 한 다음 새 값을 받을 때까지 기다립니다. `None`을 받으면 루프를 중지합니다. `caller` 함수는 `accumulator`의 인스턴스를 생성하고 `yield from`을 사용하여 모든 send 및 receive 작업을 위임합니다.

2. Python 셸에서 이러한 함수를 테스트합니다.

```python
from cofollow import caller

c = caller()
print(next(c))  # Start the coroutine
print(c.send(1))  # Send value 1, get accumulated value
print(c.send(2))  # Send value 2, get accumulated value
print(c.send(3))  # Send value 3, get accumulated value
print(c.send(None))  # Send None to exit the accumulator
```

이 코드를 실행하면 다음과 같은 출력이 표시됩니다.

```
0
1
3
6
'Total accumulated'
```

이 출력은 `yield from`이 소진될 때까지 모든 send 및 receive 작업을 하위 제너레이터에 완전히 위임함을 보여줍니다.

이제 `yield from`의 기본 사항을 이해했으므로 다음 단계에서 더 실용적인 응용 프로그램으로 이동하겠습니다.
