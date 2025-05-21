# 동시 프로그래밍을 위한 Future 사용하기

Python 에서 함수를 동시에, 즉 동시적으로 실행해야 할 필요가 있을 때, 스레드 (thread) 및 프로세스 (process) 와 같은 유용한 도구를 제공합니다. 하지만 여기서 흔히 직면하는 문제가 있습니다: 다른 스레드에서 실행 중인 함수가 반환하는 값을 어떻게 얻을 수 있을까요? 이 때 `Future`의 개념이 매우 중요해집니다.

`Future`는 나중에 사용할 수 있는 결과에 대한 자리 표시자와 같습니다. 함수가 실행을 완료하기 전에도 함수가 미래에 생성할 값을 나타내는 방법입니다. 간단한 예제를 통해 이 개념을 더 잘 이해해 보겠습니다.

### 1 단계: 새 파일 생성

먼저, 새 Python 파일을 생성해야 합니다. 이 파일의 이름을 `futures_demo.py`라고 하겠습니다. 터미널에서 다음 명령을 사용하여 이 파일을 생성할 수 있습니다.

```
touch ~/project/futures_demo.py
```

### 2 단계: 기본 함수 코드 추가

이제 `futures_demo.py` 파일을 열고 다음 Python 코드를 추가합니다. 이 코드는 간단한 함수를 정의하고 일반적인 함수 호출이 어떻게 작동하는지 보여줍니다.

```python
import time
import threading
from concurrent.futures import Future, ThreadPoolExecutor

def worker(x, y):
    """A function that takes time to complete"""
    print('Starting work...')
    time.sleep(5)  # Simulate a time-consuming task
    print('Work completed')
    return x + y

# Part 1: Normal function call
print("--- Part 1: Normal function call ---")
result = worker(2, 3)
print(f"Result: {result}")
```

이 코드에서 `worker` 함수는 두 개의 숫자를 받아 더하지만, 먼저 5 초 동안 일시 중지하여 시간이 많이 걸리는 작업을 시뮬레이션합니다. 이 함수를 일반적인 방식으로 호출하면 프로그램은 함수가 완료될 때까지 기다린 다음 반환 값을 가져옵니다.

### 3 단계: 기본 코드 실행

파일을 저장하고 터미널에서 다음 명령을 사용하여 실행합니다.

```
python ~/project/futures_demo.py
```

다음과 같은 출력을 볼 수 있습니다.

```
--- Part 1: Normal function call ---
Starting work...
Work completed
Result: 5
```

이것은 일반적인 함수 호출이 함수가 완료될 때까지 기다린 다음 결과를 반환함을 보여줍니다.

### 4 단계: 별도의 스레드에서 함수 실행

다음으로, `worker` 함수를 별도의 스레드에서 실행할 때 어떤 일이 발생하는지 살펴보겠습니다. 다음 코드를 `futures_demo.py` 파일에 추가합니다.

```python
# Part 2: Running in a separate thread (problem: no way to get result)
print("\n--- Part 2: Running in a separate thread ---")
t = threading.Thread(target=worker, args=(2, 3))
t.start()
print("Main thread continues while worker runs...")
t.join()  # Wait for the thread to complete
print("Worker thread finished, but we don't have its return value!")
```

여기서는 `threading.Thread` 클래스를 사용하여 `worker` 함수를 새 스레드에서 시작합니다. 메인 스레드는 `worker` 함수가 완료될 때까지 기다리지 않고 실행을 계속합니다. 그러나 `worker` 스레드가 완료되면 반환 값을 얻을 쉬운 방법이 없습니다.

### 5 단계: 스레드 코드 실행

파일을 다시 저장하고 동일한 명령을 사용하여 실행합니다.

```
python ~/project/futures_demo.py
```

메인 스레드가 계속 실행되고, worker 스레드가 실행되지만, `worker` 함수의 반환 값에 액세스할 수 없음을 알 수 있습니다.

### 6 단계: `Future` 수동 사용

스레드에서 반환 값을 얻는 문제를 해결하기 위해 `Future` 객체를 사용할 수 있습니다. 다음 코드를 `futures_demo.py` 파일에 추가합니다.

```python
# Part 3: Using a Future to get the result
print("\n--- Part 3: Using a Future manually ---")

def do_work_with_future(x, y, future):
    """Wrapper that sets the result in the Future"""
    result = worker(x, y)
    future.set_result(result)

# Create a Future object
fut = Future()

# Start a thread that will set the result in the Future
t = threading.Thread(target=do_work_with_future, args=(2, 3, fut))
t.start()

print("Main thread continues...")
print("Waiting for the result...")
# Block until the result is available
result = fut.result()  # This will wait until set_result is called
print(f"Got the result: {result}")
```

이 코드에서는 `Future` 객체를 생성하고 새 함수 `do_work_with_future`에 전달합니다. 이 함수는 `worker` 함수를 호출한 다음 `Future` 객체에 결과를 설정합니다. 그런 다음 메인 스레드는 `Future` 객체의 `result()` 메서드를 사용하여 결과가 사용 가능할 때 결과를 얻을 수 있습니다.

### 7 단계: `Future`로 코드 실행

파일을 저장하고 다시 실행합니다.

```
python ~/project/futures_demo.py
```

이제 스레드에서 실행되는 함수에서 반환 값을 성공적으로 얻을 수 있음을 알 수 있습니다.

### 8 단계: `ThreadPoolExecutor` 사용

Python 의 `ThreadPoolExecutor` 클래스는 동시 작업을 훨씬 쉽게 처리할 수 있도록 해줍니다. 다음 코드를 `futures_demo.py` 파일에 추가합니다.

```python
# Part 4: Using ThreadPoolExecutor (easier way)
print("\n--- Part 4: Using ThreadPoolExecutor ---")
with ThreadPoolExecutor() as executor:
    # Submit the work to the executor
    future = executor.submit(worker, 2, 3)

    print("Main thread continues after submitting work...")
    print("Checking if the future is done:", future.done())

    # Get the result (will wait if not ready)
    result = future.result()
    print("Now the future is done:", future.done())
    print(f"Final result: {result}")
```

`ThreadPoolExecutor`는 `Future` 객체를 생성하고 관리하는 것을 처리합니다. 함수와 해당 인수를 제출하기만 하면 결과를 얻는 데 사용할 수 있는 `Future` 객체를 반환합니다.

### 9 단계: 전체 코드 실행

파일을 마지막으로 저장하고 실행합니다.

```
python ~/project/futures_demo.py
```

### 설명

1. **일반 함수 호출**: 일반적인 방식으로 함수를 호출하면 프로그램은 함수가 완료될 때까지 기다리고 직접 반환 값을 가져옵니다.
2. **스레드 문제**: 별도의 스레드에서 함수를 실행하는 데는 단점이 있습니다. 해당 스레드에서 실행되는 함수의 반환 값을 얻을 수 있는 내장된 방법이 없습니다.
3. **수동 Future**: `Future` 객체를 생성하여 스레드에 전달하면 `Future`에 결과를 설정한 다음 메인 스레드에서 결과를 얻을 수 있습니다.
4. **ThreadPoolExecutor**: 이 클래스는 동시 프로그래밍을 단순화합니다. `Future` 객체의 생성 및 관리를 처리하여 함수를 동시적으로 실행하고 반환 값을 얻는 것을 더 쉽게 만듭니다.

`Future` 객체에는 몇 가지 유용한 메서드가 있습니다.

- `result()`: 이 메서드는 함수의 결과를 얻는 데 사용됩니다. 결과가 아직 준비되지 않은 경우 준비될 때까지 기다립니다.
- `done()`: 이 메서드를 사용하여 함수의 계산이 완료되었는지 확인할 수 있습니다.
- `add_done_callback()`: 이 메서드를 사용하면 결과가 준비될 때 호출될 함수를 등록할 수 있습니다.

이 패턴은 동시 프로그래밍에서, 특히 병렬로 실행되는 함수에서 결과를 얻어야 할 때 매우 중요합니다.
