# 제너레이터를 사용한 네트워크 서버 구축

이 섹션에서는 우리가 배운 작업 스케줄러의 개념을 확장하여 더 실용적인 것, 즉 간단한 네트워크 서버를 만들 것입니다. 이 서버는 제너레이터를 사용하여 여러 클라이언트 연결을 동시에 처리할 수 있습니다. 제너레이터는 함수가 실행을 일시 중지하고 재개할 수 있도록 하는 강력한 Python 기능으로, 블로킹 없이 여러 작업을 처리하는 데 매우 유용합니다.

먼저 `/home/labex/project` 디렉토리에 `server.py`라는 새 파일을 만들어야 합니다. 이 파일에는 네트워크 서버에 대한 코드가 포함됩니다.

```python
# server.py

from socket import *
from select import select
from collections import deque

# Task system
tasks = deque()
recv_wait = {}   # Map: socket -> task (for tasks waiting to receive)
send_wait = {}   # Map: socket -> task (for tasks waiting to send)

def run():
    while any([tasks, recv_wait, send_wait]):
        # If no active tasks, wait for I/O
        while not tasks:
            # Wait for any socket to become ready for I/O
            can_recv, can_send, _ = select(recv_wait, send_wait, [])

            # Add tasks waiting on readable sockets back to active queue
            for s in can_recv:
                tasks.append(recv_wait.pop(s))

            # Add tasks waiting on writable sockets back to active queue
            for s in can_send:
                tasks.append(send_wait.pop(s))

        # Get next task to run
        task = tasks.popleft()

        try:
            # Resume the task
            reason, resource = task.send(None)

            # Handle different yield reasons
            if reason == 'recv':
                # Task is waiting to receive data
                recv_wait[resource] = task
            elif reason == 'send':
                # Task is waiting to send data
                send_wait[resource] = task
            else:
                raise RuntimeError('Unknown yield reason %r' % reason)

        except StopIteration:
            print('Task done')
```

이 향상된 스케줄러는 이전 스케줄러보다 약간 더 복잡하지만 동일한 기본 아이디어를 따릅니다. 주요 차이점을 살펴보겠습니다.

1. 작업은 이유 ('recv' 또는 'send') 와 리소스 (소켓) 를 yield 할 수 있습니다. 즉, 작업은 특정 소켓에서 데이터를 수신하거나 전송하기 위해 대기 중임을 스케줄러에게 알릴 수 있습니다.
2. yield 이유에 따라 작업은 다른 대기 영역으로 이동합니다. 작업이 데이터를 수신하기 위해 대기 중인 경우 `recv_wait` 딕셔너리로 이동합니다. 데이터를 전송하기 위해 대기 중인 경우 `send_wait` 딕셔너리로 이동합니다.
3. `select()` 함수는 어떤 소켓이 I/O 작업을 위해 준비되었는지 파악하는 데 사용됩니다. 이 함수는 `recv_wait` 및 `send_wait` 딕셔너리의 소켓을 확인하고 데이터를 수신하거나 전송할 준비가 된 소켓을 반환합니다.
4. 소켓이 준비되면 관련 작업이 다시 활성 큐로 이동합니다. 이를 통해 작업은 실행을 계속하고 대기 중이던 I/O 작업을 수행할 수 있습니다.

이러한 기술을 사용하면 작업은 다른 작업의 실행을 차단하지 않고 네트워크 I/O 를 효율적으로 대기할 수 있습니다. 이렇게 하면 네트워크 서버가 더 빠르게 응답하고 여러 클라이언트 연결을 동시에 처리할 수 있습니다.
