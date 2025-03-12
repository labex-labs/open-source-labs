# Construire un serveur réseau avec des générateurs

Dans cette section, nous allons prendre le concept de planificateur de tâches que nous avons appris et l'étendre pour créer quelque chose de plus pratique : un simple serveur réseau. Ce serveur peut gérer plusieurs connexions clientes en même temps en utilisant des générateurs. Les générateurs sont une fonctionnalité puissante de Python qui permet aux fonctions de mettre en pause et de reprendre leur exécution, ce qui est très utile pour gérer plusieurs tâches sans bloquer.

Tout d'abord, vous devez créer un nouveau fichier nommé `server.py` dans le répertoire `/home/labex/project`. Ce fichier contiendra le code de notre serveur réseau.

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

Ce planificateur amélioré est un peu plus compliqué que le précédent, mais il suit les mêmes idées fondamentales. Analysons les principales différences :

1. Les tâches peuvent céder (yield) une raison ('recv' ou 'send') et une ressource (un socket). Cela signifie qu'une tâche peut indiquer au planificateur qu'elle attend soit de recevoir, soit d'envoyer des données sur un socket spécifique.
2. Selon la raison du cession (yield), la tâche est déplacée dans une zone d'attente différente. Si une tâche attend de recevoir des données, elle est placée dans le dictionnaire `recv_wait`. Si elle attend d'envoyer des données, elle est placée dans le dictionnaire `send_wait`.
3. La fonction `select()` est utilisée pour déterminer quels sockets sont prêts pour des opérations d'E/S. Cette fonction vérifie les sockets dans les dictionnaires `recv_wait` et `send_wait` et renvoie ceux qui sont prêts à recevoir ou à envoyer des données.
4. Lorsqu'un socket est prêt, la tâche associée est déplacée de nouveau dans la file d'attente active. Cela permet à la tâche de reprendre son exécution et d'effectuer l'opération d'E/S pour laquelle elle attendait.

En utilisant ces techniques, nos tâches peuvent attendre efficacement les opérations d'E/S réseau sans bloquer l'exécution des autres tâches. Cela rend notre serveur réseau plus réactif et capable de gérer plusieurs connexions clientes de manière concurrente.
