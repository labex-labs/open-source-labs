# Construindo um Servidor de Rede com Geradores

Nesta seção, vamos pegar o conceito de um agendador de tarefas que aprendemos e expandi-lo para criar algo mais prático: um servidor de rede simples. Este servidor pode lidar com múltiplas conexões de clientes ao mesmo tempo usando geradores. Geradores são um recurso poderoso do Python que permite que funções pausem e retomem sua execução, o que é muito útil para lidar com múltiplas tarefas sem bloquear.

Primeiro, você precisa criar um novo arquivo chamado `server.py` no diretório `/home/labex/project`. Este arquivo conterá o código para nosso servidor de rede.

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

Este agendador aprimorado é um pouco mais complicado do que o anterior, mas segue as mesmas ideias fundamentais. Vamos detalhar as principais diferenças:

1. As tarefas podem produzir (yield) uma razão ('recv' ou 'send') e um recurso (um socket). Isso significa que uma tarefa pode dizer ao agendador que está esperando para receber ou enviar dados em um socket específico.
2. Dependendo da razão do yield, a tarefa é movida para uma área de espera diferente. Se uma tarefa estiver esperando para receber dados, ela vai para o dicionário `recv_wait`. Se estiver esperando para enviar dados, ela vai para o dicionário `send_wait`.
3. A função `select()` é usada para descobrir quais sockets estão prontos para operações de I/O. Esta função verifica os sockets nos dicionários `recv_wait` e `send_wait` e retorna aqueles que estão prontos para receber ou enviar dados.
4. Quando um socket está pronto, a tarefa associada é movida de volta para a fila ativa. Isso permite que a tarefa continue sua execução e execute a operação de I/O pela qual estava esperando.

Ao usar essas técnicas, nossas tarefas podem esperar eficientemente por I/O de rede sem bloquear a execução de outras tarefas. Isso torna nosso servidor de rede mais responsivo e capaz de lidar com múltiplas conexões de clientes simultaneamente.
