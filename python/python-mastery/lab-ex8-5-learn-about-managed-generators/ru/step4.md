# Создание сетевого сервера с использованием генераторов

В этом разделе мы возьмем концепцию планировщика задач, которую мы изучили, и расширим ее, чтобы создать что-то более практичное: простой сетевой сервер. Этот сервер может обрабатывать несколько клиентских подключений одновременно с использованием генераторов. Генераторы - это мощная особенность Python, которая позволяет функциям приостанавливать и возобновлять свое выполнение, что очень полезно для обработки нескольких задач без блокировки.

Сначала вам нужно создать новый файл с именем `server.py` в директории `/home/labex/project`. Этот файл будет содержать код нашего сетевого сервера.

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

Этот улучшенный планировщик немного сложнее, чем предыдущий, но он следует тем же основным идеям. Разберем основные различия:

1. Задачи могут возвращать причину (`'recv'` или `'send'`) и ресурс (сокет). Это означает, что задача может сообщить планировщику, что она ждет либо получения, либо отправки данных на определенном сокете.
2. В зависимости от причины возврата задача перемещается в другую область ожидания. Если задача ждет получения данных, она попадает в словарь `recv_wait`. Если она ждет отправки данных, она попадает в словарь `send_wait`.
3. Функция `select()` используется для определения, какие сокеты готовы к операциям ввода-вывода. Эта функция проверяет сокеты в словарях `recv_wait` и `send_wait` и возвращает те, которые готовы либо к получению, либо к отправке данных.
4. Когда сокет готов, связанная с ним задача возвращается в активную очередь. Это позволяет задаче продолжить свое выполнение и выполнить операцию ввода-вывода, на которую она ждала.

Используя эти методы, наши задачи могут эффективно ждать сетевого ввода-вывода без блокировки выполнения других задач. Это делает наш сетевой сервер более отзывчивым и способным обрабатывать несколько клиентских подключений одновременно.
