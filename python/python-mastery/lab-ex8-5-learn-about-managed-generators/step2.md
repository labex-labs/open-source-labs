# Generators as Tasks Serving Network Connections

In the file `server.py` and put the following code into it:

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
            if reason == 'recv':
                recv_wait[resource] = task
            elif reason == 'send':
                send_wait[resource] = task
            else:
                raise RuntimeError('Unknown reason %r' % reason)
        except StopIteration:
            print('Task done')
```

This code is a slightly more complicated version of the task scheduler in
part (a). It will require a bit of study, but the idea is that not only
will each task yield, it will indicate a reason for doing so (receiving or
sending). Depending on the reason, the task will move over to a waiting
area. The scheduler then runs any available tasks or waits for I/O
events to occur when nothing is left to do.

It's all a bit tricky perhaps, but add the following code which implements
a simple echo server:

```python
# server.py
...

def tcp_server(address, handler):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        yield 'recv', sock
        client, addr = sock.accept()
        tasks.append(handler(client, addr))

def echo_handler(client, address):
    print('Connection from', address)
    while True:
        yield 'recv', client
        data = client.recv(1000)
        if not data:
            break
        yield 'send', client
        client.send(b'GOT:' + data)
    print('Connection closed')

if __name__ == '__main__':
    tasks.append(tcp_server(('',25000), echo_handler))
    run()
```

Run this server in its own terminal window. In another terminal, connect to it using a command such as `telnet` or `nc`. For example:

```bash
nc localhost 25000
Hello
Got: Hello
World
Got: World
```

If you don't have access to `nc` or `telnet` you can also use Python itself:

```bash
python3 -m telnetlib localhost 25000
Hello
Got: Hello
World
Got: World
```

If it's working, you should see output being echoed back to you. Not only that,
if you connect multiple clients, they'll all operate concurrently.

This tricky use of generators is not something that you would
likely have to code directly. However, they are used in certain advanced
packages such as `asyncio` that was added to the standard
library in Python 3.4.
