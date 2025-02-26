# Generadores como Tareas que Atienden Conexiones de Red

En el archivo `server.py` y ponga el siguiente código en él:

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
                raise RuntimeError('Razón desconocida %r' % reason)
        except StopIteration:
            print('Tarea terminada')
```

Este código es una versión ligeramente más complicada del planificador de tareas de la parte (a). Requiere un poco de estudio, pero la idea es que no solo cada tarea generará, sino que indicará una razón para hacerlo (recibir o enviar). Dependiendo de la razón, la tarea pasará a un área de espera. Luego, el planificador ejecuta cualquier tarea disponible o espera a que ocurran eventos de E/S cuando no queda nada que hacer.

Quizás todo sea un poco complicado, pero agregue el siguiente código que implementa un servidor de eco simple:

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
    print('Conexión desde', address)
    while True:
        yield 'recv', client
        data = client.recv(1000)
        if not data:
            break
        yield 'send', client
        client.send(b'GOT:' + data)
    print('Conexión cerrada')

if __name__ == '__main__':
    tasks.append(tcp_server(('',25000), echo_handler))
    run()
```

Ejecute este servidor en su propia ventana de terminal. En otra terminal, conéctese a él usando un comando como `telnet` o `nc`. Por ejemplo:

```bash
nc localhost 25000
Hello
Got: Hello
World
Got: World
```

Si no tiene acceso a `nc` o `telnet`, también puede usar Python mismo:

```bash
python3 -m telnetlib localhost 25000
Hello
Got: Hello
World
Got: World
```

Si está funcionando, debería ver la salida ecoada hacia usted. No solo eso, si conecta múltiples clientes, todos operarán concurrentemente.

Este uso complicado de generadores no es algo que probablemente tenga que codificar directamente. Sin embargo, se usan en ciertos paquetes avanzados como `asyncio` que se agregó a la biblioteca estándar en Python 3.4.
