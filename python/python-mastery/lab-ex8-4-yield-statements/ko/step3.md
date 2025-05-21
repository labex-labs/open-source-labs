# 제너레이터 관리에 대한 실용적인 응용

이 단계에서는 제너레이터 관리 및 제너레이터에서 예외를 처리하는 방법에 대해 배운 개념을 실제 시나리오에 적용하는 방법을 살펴보겠습니다. 이러한 실용적인 응용을 이해하면 더 강력하고 효율적인 Python 코드를 작성하는 데 도움이 됩니다.

## 강력한 파일 모니터링 시스템 구축

파일 모니터링 시스템의 더 안정적인 버전을 구축해 보겠습니다. 이 시스템은 시간 초과 및 중지 요청과 같은 다양한 상황을 처리할 수 있습니다.

먼저 WebIDE 편집기를 열고 `robust_follow.py`라는 새 파일을 만듭니다. 이 파일에 작성해야 하는 코드는 다음과 같습니다.

```python
import os
import time
import signal

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

def follow(filename, timeout=None):
    """
    A generator that yields new lines in a file.
    With timeout handling and proper cleanup.
    """
    try:
        # Set up timeout if specified
        if timeout:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout)

        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    # No new data, wait briefly
                    time.sleep(0.1)
                    continue
                yield line
    except TimeoutError:
        print(f"Following timed out after {timeout} seconds")
    except GeneratorExit:
        print("Following stopped by request")
    finally:
        # Clean up timeout alarm if it was set
        if timeout:
            signal.alarm(0)
        print("Follow generator cleanup complete")
```

이 코드에서는 먼저 사용자 지정 `TimeoutError` 클래스를 정의합니다. `timeout_handler` 함수는 시간 초과가 발생할 때 이 오류를 발생시키는 데 사용됩니다. `follow` 함수는 파일을 읽고 새 줄을 yield 하는 제너레이터입니다. 시간 초과가 지정되면 `signal` 모듈을 사용하여 알람을 설정합니다. 파일에 새 데이터가 없으면 잠시 기다린 후 다시 시도합니다. `try - except - finally` 블록은 다양한 예외를 처리하고 적절한 정리를 보장하는 데 사용됩니다.

코드를 작성한 후 파일을 저장합니다.

## 강력한 파일 모니터링 시스템 실험

이제 개선된 파일 모니터링 시스템을 테스트해 보겠습니다. 터미널을 열고 다음 명령으로 Python 인터프리터를 실행합니다.

```bash
cd ~/project
python3
```

### 실험 1: 기본 사용

Python 인터프리터에서 `follow` 제너레이터의 기본 기능을 테스트합니다. 실행할 코드는 다음과 같습니다.

```python
>>> from robust_follow import follow
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 2:  # Just read a few lines for the example
...         break
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Line 3: "HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
```

여기서는 `robust_follow.py` 파일에서 `follow` 함수를 가져옵니다. 그런 다음 `stocklog.csv` 파일을 따르는 제너레이터 객체 `f`를 생성합니다. `for` 루프를 사용하여 제너레이터가 yield 하는 줄을 반복하고 처음 세 줄을 출력합니다.

### 실험 2: 시간 초과 사용

시간 초과 기능이 어떻게 작동하는지 살펴보겠습니다. Python 인터프리터에서 다음 코드를 실행합니다.

```python
>>> # Create a generator that will time out after 3 seconds
>>> f = follow('stocklog.csv', timeout=3)
>>> for line in f:
...     print(line.strip())
...     time.sleep(1)  # Process each line slowly
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
Following timed out after 3 seconds
Follow generator cleanup complete
```

이 실험에서는 3 초 시간 초과가 있는 제너레이터를 생성합니다. 각 줄 사이에 1 초 동안 대기하여 각 줄을 천천히 처리합니다. 약 3 초 후에 제너레이터는 시간 초과 예외를 발생시키고 `finally` 블록의 정리 코드가 실행됩니다.

### 실험 3: 명시적 클로저

제너레이터가 명시적 클로저를 어떻게 처리하는지 테스트해 보겠습니다. 다음 코드를 실행합니다.

```python
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 1:
...         print("Explicitly closing the generator...")
...         f.close()
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Explicitly closing the generator...
Following stopped by request
Follow generator cleanup complete
```

여기서는 제너레이터를 생성하고 해당 줄을 반복하기 시작합니다. 두 줄을 처리한 후 `close` 메서드를 사용하여 제너레이터를 명시적으로 닫습니다. 그러면 제너레이터는 `GeneratorExit` 예외를 처리하고 필요한 정리를 수행합니다.

## 오류 처리를 통한 데이터 처리 파이프라인 구축

다음으로 코루틴을 사용하여 간단한 데이터 처리 파이프라인을 만들겠습니다. 이 파이프라인은 다양한 단계에서 오류를 처리할 수 있습니다.

WebIDE 편집기를 열고 `pipeline.py`라는 새 파일을 만듭니다. 이 파일에 작성할 코드는 다음과 같습니다.

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def grep(pattern, target):
    """Filter lines containing pattern and send to target"""
    try:
        while True:
            line = yield
            if pattern in line:
                target.send(line)
    except Exception as e:
        target.throw(e)

@consumer
def printer():
    """Print received items"""
    try:
        while True:
            item = yield
            print(f"PRINTER: {item}")
    except Exception as e:
        print(f"PRINTER ERROR: {repr(e)}")

def follow_and_process(filename, pattern):
    """Follow a file and process its contents"""
    import time
    import os

    output = printer()
    filter_pipe = grep(pattern, output)

    try:
        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                filter_pipe.send(line)
    except KeyboardInterrupt:
        print("Processing stopped by user")
    finally:
        filter_pipe.close()
        output.close()
```

이 코드에서 `consumer` 데코레이터는 코루틴을 초기화하는 데 사용됩니다. `grep` 코루틴은 특정 패턴을 포함하는 줄을 필터링하여 다른 코루틴으로 보냅니다. `printer` 코루틴은 수신된 항목을 출력합니다. `follow_and_process` 함수는 파일을 읽고, `grep` 코루틴을 사용하여 해당 줄을 필터링하고, `printer` 코루틴을 사용하여 일치하는 줄을 출력합니다. 또한 `KeyboardInterrupt` 예외를 처리하고 적절한 정리를 보장합니다.

코드를 작성한 후 파일을 저장합니다.

## 데이터 처리 파이프라인 테스트

데이터 처리 파이프라인을 테스트해 보겠습니다. 터미널에서 다음 명령을 실행합니다.

```bash
cd ~/project
python3 -c "from pipeline import follow_and_process; follow_and_process('stocklog.csv', 'IBM')"
```

다음과 유사한 출력이 표시됩니다.

```
PRINTER: "IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550

PRINTER: "IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859

PRINTER: "IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
```

이 출력은 파이프라인이 올바르게 작동하여 "IBM" 패턴을 포함하는 줄을 필터링하고 출력함을 보여줍니다.

프로세스를 중지하려면 `Ctrl+C`를 누릅니다. 다음 메시지가 표시됩니다.

```
Processing stopped by user
```

## 주요 내용

1. 제너레이터에서 적절한 예외 처리를 통해 오류를 적절하게 처리할 수 있는 강력한 시스템을 만들 수 있습니다. 즉, 프로그램에서 문제가 발생하더라도 예기치 않게 충돌하지 않습니다.
2. 시간 초과와 같은 기술을 사용하여 제너레이터가 무기한 실행되는 것을 방지할 수 있습니다. 이는 시스템 리소스를 관리하고 프로그램이 무한 루프에 갇히지 않도록 하는 데 도움이 됩니다.
3. 제너레이터와 코루틴은 오류를 전파하고 적절한 수준에서 처리할 수 있는 강력한 데이터 처리 파이프라인을 형성할 수 있습니다. 이렇게 하면 복잡한 데이터 처리 시스템을 더 쉽게 구축할 수 있습니다.
4. 제너레이터의 `finally` 블록은 제너레이터가 종료되는 방식에 관계없이 정리 작업이 수행되도록 합니다. 이는 프로그램의 무결성을 유지하고 리소스 누수를 방지하는 데 도움이 됩니다.
