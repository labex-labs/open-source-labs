# Генераторы в качестве задач для обслуживания сетевых подключений

В файл `server.py` вставьте следующий код:

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

Этот код представляет собой немного более сложную версию планировщика задач из части (a). Его нужно будет немного изучить, но идея заключается в том, что не только каждый таск будет генерировать, но и указывать причину этого (прием или отправка). В зависимости от причины таск перейдет в зону ожидания. Затем планировщик запускает любые доступные задачи или ждет событий ввода-вывода, когда нечего делать.

Вполне возможно, что это все выглядит сложновато, но добавьте следующий код, который реализует простой эхо-сервер:

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

Запустите этот сервер в отдельном окне терминала. В другом терминале подключитесь к нему с помощью команды, такой как `telnet` или `nc`. Например:

```bash
nc localhost 25000
Hello
Got: Hello
World
Got: World
```

Если у вас нет доступа к `nc` или `telnet`, вы также можете использовать сам Python:

```bash
python3 -m telnetlib localhost 25000
Hello
Got: Hello
World
Got: World
```

Если все работает, вы должны увидеть, что вывод возвращается обратно. Не только это, но и если подключить несколько клиентов, они будут работать одновременно.

Этот сложный способ использования генераторов - это не то, что вы, вероятно, будете писать напрямую. Однако они используются в некоторых более продвинутых пакетах, таких как `asyncio`, который был добавлен в стандартную библиотеку в Python 3.4.
