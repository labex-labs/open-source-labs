# 제너레이터를 사용한 작업 스케줄러 생성

프로그래밍에서 작업 스케줄러는 여러 작업을 효율적으로 관리하고 실행하는 데 도움이 되는 중요한 도구입니다. 이 섹션에서는 제너레이터를 사용하여 여러 제너레이터 함수를 동시에 실행할 수 있는 간단한 작업 스케줄러를 구축합니다. 이를 통해 제너레이터가 협력적 멀티태스킹 (cooperative multitasking) 을 수행하도록 관리하는 방법을 보여줍니다. 즉, 작업이 번갈아 가며 실행되고 실행 시간을 공유합니다.

먼저 새 파일을 만들어야 합니다. `/home/labex/project` 디렉토리로 이동하여 `multitask.py`라는 파일을 만듭니다. 이 파일에는 작업 스케줄러에 대한 코드가 포함됩니다.

```python
# multitask.py

from collections import deque

# Task queue
tasks = deque()

# Simple task scheduler
def run():
    while tasks:
        task = tasks.popleft()  # Get the next task
        try:
            task.send(None)     # Resume the task
            tasks.append(task)  # Put it back in the queue
        except StopIteration:
            print('Task done')  # Task is complete

# Example task 1: Countdown
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield              # Pause execution
        n -= 1

# Example task 2: Count up
def countup(n):
    x = 0
    while x < n:
        print('Up we go', x)
        yield              # Pause execution
        x += 1
```

이제 이 작업 스케줄러가 어떻게 작동하는지 자세히 살펴보겠습니다.

1. `deque` (double-ended queue, 양방향 큐) 를 사용하여 제너레이터 작업을 저장합니다. `deque`는 양쪽 끝에서 요소를 효율적으로 추가하고 제거할 수 있는 데이터 구조입니다. 작업 큐에 적합한 선택입니다. 왜냐하면 작업을 끝에 추가하고 앞에서 제거해야 하기 때문입니다.
2. `run()` 함수는 작업 스케줄러의 핵심입니다. 큐에서 작업을 하나씩 가져옵니다.
   - `send(None)`을 사용하여 각 작업을 재개합니다. 이는 제너레이터에서 `next()`를 사용하는 것과 유사합니다. 제너레이터에게 중단된 지점부터 실행을 계속하도록 지시합니다.
   - 작업이 yield 된 후에는 큐의 끝에 다시 추가됩니다. 이렇게 하면 작업이 나중에 다시 실행될 기회를 얻게 됩니다.
   - 작업이 완료되면 (`StopIteration`을 발생시키면) 큐에서 제거됩니다. 이는 작업이 실행을 완료했음을 나타냅니다.
3. 제너레이터 작업의 각 `yield` 문은 일시 중지 지점 역할을 합니다. 제너레이터가 `yield` 문에 도달하면 실행을 일시 중지하고 제어 권한을 스케줄러에 다시 반환합니다. 이를 통해 다른 작업을 실행할 수 있습니다.

이 접근 방식은 협력적 멀티태스킹을 구현합니다. 각 작업은 자발적으로 제어 권한을 스케줄러에 다시 반환하여 다른 작업을 실행할 수 있도록 합니다. 이러한 방식으로 여러 작업이 실행 시간을 공유하고 동시에 실행될 수 있습니다.
