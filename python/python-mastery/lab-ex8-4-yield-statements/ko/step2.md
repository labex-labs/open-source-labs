# 제너레이터에서 예외 처리

이 단계에서는 제너레이터와 코루틴에서 예외를 처리하는 방법을 배우겠습니다. 하지만 먼저 예외가 무엇인지 이해해 보겠습니다. 예외는 프로그램 실행 중에 발생하여 프로그램의 정상적인 흐름을 방해하는 이벤트입니다. Python 에서는 `throw()` 메서드를 사용하여 제너레이터와 코루틴에서 예외를 처리할 수 있습니다.

## 코루틴 이해

코루틴은 특수한 유형의 제너레이터입니다. 주로 값을 yield 하는 일반 제너레이터와 달리, 코루틴은 값을 소비 ( `send()` 메서드 사용) 하고 값을 yield 할 수 있습니다. `cofollow.py` 파일에는 코루틴의 간단한 구현이 있습니다.

WebIDE 편집기에서 `cofollow.py` 파일을 열어보겠습니다. 다음은 내부 코드입니다.

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def printer():
    while True:
        item = yield
        print(item)
```

이제 이 코드를 분석해 보겠습니다. `consumer`는 데코레이터입니다. 데코레이터는 다른 함수를 인수로 받아 해당 함수에 일부 기능을 추가한 다음 수정된 함수를 반환하는 함수입니다. 이 경우 `consumer` 데코레이터는 자동으로 제너레이터를 첫 번째 `yield` 문으로 이동시킵니다. 이는 제너레이터가 값을 받을 준비가 되도록 하므로 중요합니다.

`printer()` 코루틴은 `@consumer` 데코레이터로 정의됩니다. `printer()` 함수 내부에는 무한 `while` 루프가 있습니다. `item = yield` 문은 마법이 일어나는 곳입니다. 코루틴의 실행을 일시 중지하고 값을 받을 때까지 기다립니다. 코루틴으로 값이 전송되면 실행을 재개하고 수신된 값을 출력합니다.

## 코루틴에 예외 처리 추가

이제 `printer()` 코루틴을 수정하여 예외를 처리하겠습니다. `cofollow.py`의 `printer()` 함수를 다음과 같이 업데이트합니다.

```python
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)
```

`try` 블록에는 예외를 발생시킬 수 있는 코드가 포함되어 있습니다. 이 경우 값을 받고 출력하는 코드입니다. `try` 블록에서 예외가 발생하면 실행이 `except` 블록으로 이동합니다. `except` 블록은 예외를 catch 하고 오류 메시지를 출력합니다. 이러한 변경을 수행한 후 파일을 저장합니다.

## 코루틴에서 예외 처리 실험

코루틴에 예외를 throw 하는 실험을 시작해 보겠습니다. 터미널을 열고 다음 명령을 사용하여 Python 인터프리터를 실행합니다.

```bash
cd ~/project
python3
```

### 실험 1: 기본 코루틴 사용

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')  # Send a value to the coroutine
hello
>>> p.send(42)  # Send another value
42
```

여기서는 먼저 `cofollow` 모듈에서 `printer` 코루틴을 가져옵니다. 그런 다음 `p`라는 `printer` 코루틴의 인스턴스를 생성합니다. `send()` 메서드를 사용하여 코루틴에 값을 보냅니다. 보시다시피 코루틴은 문제 없이 전송한 값을 처리합니다.

### 실험 2: 코루틴에 예외 throw

```python
>>> p.throw(ValueError('It failed'))  # Throw an exception into the coroutine
ERROR: ValueError('It failed')
```

이 실험에서는 `throw()` 메서드를 사용하여 `ValueError` 예외를 코루틴에 주입합니다. `printer()` 코루틴의 `try-except` 블록은 예외를 catch 하고 오류 메시지를 출력합니다. 이는 예외 처리가 예상대로 작동하고 있음을 보여줍니다.

### 실험 3: 코루틴에 실제 예외 throw

```python
>>> try:
...     int('n/a')  # This will raise a ValueError
... except ValueError as e:
...     p.throw(e)  # Throw the caught exception into the coroutine
...
ERROR: ValueError("invalid literal for int() with base 10: 'n/a'")
```

여기서는 먼저 문자열 `'n/a'`를 정수로 변환하려고 시도하는데, 이로 인해 `ValueError`가 발생합니다. 이 예외를 catch 한 다음 `throw()` 메서드를 사용하여 코루틴에 전달합니다. 코루틴은 예외를 catch 하고 오류 메시지를 출력합니다.

### 실험 4: 코루틴이 계속 실행되는지 확인

```python
>>> p.send('still working')  # The coroutine continues to run after handling exceptions
still working
```

예외를 처리한 후 `send()` 메서드를 사용하여 코루틴에 다른 값을 보냅니다. 코루틴은 여전히 활성 상태이며 새 값을 처리할 수 있습니다. 이는 오류가 발생한 후에도 코루틴이 계속 실행될 수 있음을 보여줍니다.

## 주요 내용

1. 제너레이터와 코루틴은 `yield` 문 지점에서 예외를 처리할 수 있습니다. 즉, 코루틴이 값을 기다리거나 처리할 때 발생하는 오류를 catch 하고 처리할 수 있습니다.
2. `throw()` 메서드를 사용하면 예외를 제너레이터 또는 코루틴에 주입할 수 있습니다. 이는 테스트 및 코루틴 외부에서 발생하는 오류를 처리하는 데 유용합니다.
3. 제너레이터에서 예외를 적절하게 처리하면 오류가 발생하더라도 계속 실행될 수 있는 강력하고 오류 허용적인 제너레이터를 만들 수 있습니다. 이렇게 하면 코드가 더 안정적이고 유지 관리하기 쉬워집니다.

Python 인터프리터를 종료하려면 `exit()`를 입력하거나 `Ctrl+D`를 누르면 됩니다.
