# 作为处理网络连接任务的生成器

在 `server.py` 文件中，输入以下代码：

```python
# server.py

from socket import *
from select import select
from collections import deque

tasks = deque()
recv_wait = {}   #  sock -> task
send_wait = {}   #  sock -> task

def run():
    while any([tasks, recv_wait, send_wait]):
        while not tasks:
            can_recv, can_send, _ = select(recv_wait, send_wait, [])
            for s in can_recv:
                tasks.append(recv_wait.pop(s))
            for s in can_send:
                tasks.append(send_wait.pop(s))
        task = tasks.popleft()
        try:
            reason, resource = task.send(None)
            if reason =='recv':
                recv_wait[resource] = task
            elif reason =='send':
                send_wait[resource] = task
            else:
                raise RuntimeError('Unknown reason %r' % reason)
        except StopIteration:
            print('Task done')
```

这段代码是（a）部分中任务调度器的一个稍微复杂的版本。它需要一些研究，但思路是每个任务不仅会产生（yield），还会指明这样做的原因（接收或发送）。根据原因，任务会转移到等待区域。然后调度器运行任何可用的任务，或者在无事可做时等待 I/O 事件发生。

这可能有点棘手，不过添加以下实现简单回声服务器的代码：

```python
# server.py
...

def tcp_server(address, handler):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        yield'recv', sock
        client, addr = sock.accept()
        tasks.append(handler(client, addr))

def echo_handler(client, address):
    print('Connection from', address)
    while True:
        yield'recv', client
        data = client.recv(1000)
        if not data:
            break
        yield'send', client
        client.send(b'GOT:' + data)
    print('Connection closed')

if __name__ == '__main__':
    tasks.append(tcp_server(('',25000), echo_handler))
    run()
```

在其自己的终端窗口中运行此服务器。在另一个终端中，使用诸如 `telnet` 或 `nc` 之类的命令连接到它。例如：

```bash
nc localhost 25000
Hello
Got: Hello
World
Got: World
```

如果你没有 `nc` 或 `telnet`，也可以使用 Python 本身：

```bash
python3 -m telnetlib localhost 25000
Hello
Got: Hello
World
Got: World
```

如果运行正常，你应该会看到输出被回显给你。不仅如此，如果你连接多个客户端，它们将全部并发运行。

这种对生成器的巧妙使用不太可能是你需要直接编写代码的情况。然而，它们在某些高级包中被使用，比如 Python 3.4 标准库中添加的 `asyncio`。
