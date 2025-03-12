# Construyendo un servidor de red con generadores

En esta sección, tomaremos el concepto de un programador de tareas (task scheduler) que hemos aprendido y lo expandiremos para crear algo más práctico: un sencillo servidor de red. Este servidor puede manejar múltiples conexiones de clientes al mismo tiempo utilizando generadores. Los generadores son una poderosa característica de Python que permite a las funciones pausar y reanudar su ejecución, lo cual es muy útil para manejar múltiples tareas sin bloquear.

Primero, debes crear un nuevo archivo llamado `server.py` en el directorio `/home/labex/project`. Este archivo contendrá el código de nuestro servidor de red.

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

Este programador de tareas mejorado es un poco más complicado que el anterior, pero sigue las mismas ideas fundamentales. Analicemos las principales diferencias:

1. Las tareas pueden devolver una razón ('recv' o 'send') y un recurso (un socket). Esto significa que una tarea puede decirle al programador de tareas que está esperando recibir o enviar datos en un socket específico.
2. Dependiendo de la razón devuelta, la tarea se mueve a una zona de espera diferente. Si una tarea está esperando recibir datos, se va al diccionario `recv_wait`. Si está esperando enviar datos, se va al diccionario `send_wait`.
3. La función `select()` se utiliza para determinar qué sockets están listos para operaciones de E/S (I/O). Esta función verifica los sockets en los diccionarios `recv_wait` y `send_wait` y devuelve aquellos que están listos para recibir o enviar datos.
4. Cuando un socket está listo, la tarea asociada se mueve de nuevo a la cola activa. Esto permite que la tarea continúe su ejecución y realice la operación de E/S por la que estaba esperando.

Al utilizar estas técnicas, nuestras tareas pueden esperar de manera eficiente a la E/S de red sin bloquear la ejecución de otras tareas. Esto hace que nuestro servidor de red sea más receptivo y capaz de manejar múltiples conexiones de clientes de forma concurrente.
