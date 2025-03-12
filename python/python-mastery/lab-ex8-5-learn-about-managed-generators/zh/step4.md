# 使用生成器构建网络服务器

在本节中，我们将运用所学的任务调度器概念，并将其扩展以创建更实用的东西：一个简单的网络服务器。这个服务器可以使用生成器同时处理多个客户端连接。生成器是 Python 中一个强大的特性，它允许函数暂停和恢复执行，这对于在不阻塞的情况下处理多个任务非常有用。

首先，你需要在 `/home/labex/project` 目录下创建一个名为 `server.py` 的新文件。该文件将包含我们网络服务器的代码。

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

这个改进后的调度器比之前的稍微复杂一些，但它遵循相同的基本思路。让我们来分析一下主要的区别：

1. 任务可以产生一个原因（`'recv'` 或 `'send'`）和一个资源（一个套接字）。这意味着任务可以告诉调度器它正在等待在特定套接字上接收或发送数据。
2. 根据产生的原因，任务会被移动到不同的等待区域。如果任务正在等待接收数据，它会被放入 `recv_wait` 字典中。如果它正在等待发送数据，它会被放入 `send_wait` 字典中。
3. `select()` 函数用于确定哪些套接字已准备好进行 I/O 操作。该函数会检查 `recv_wait` 和 `send_wait` 字典中的套接字，并返回那些准备好接收或发送数据的套接字。
4. 当一个套接字准备好时，关联的任务会被移回到活动队列中。这使得任务可以继续执行，并执行它所等待的 I/O 操作。

通过使用这些技术，我们的任务可以高效地等待网络 I/O，而不会阻塞其他任务的执行。这使得我们的网络服务器更具响应性，并且能够并发处理多个客户端连接。
