# Les générateurs en tant que tâches servant des connexions réseau

Dans le fichier `server.py` et mettez le code suivant dedans :

```python
# server.py

from socket import *
from select import select
from collections import deque

tasks = deque()
recv_wait = {}   #  sock -> tâche
send_wait = {}   #  sock -> tâche

def run():
    while any([tasks, recv_wait, send_wait]):
        while not tasks:
            can_recv, can_send, _ = select(recv_wait, send_wait, [])
            for s in can_recv:
                tasks.append(recv_wait.pop(s))
            for s in can_send:
                tasks.append(send_wait.pop(s))
        tâche = tasks.popleft()
        try:
            raison, ressource = tâche.send(None)
            if raison =='recv':
                recv_wait[ressource] = tâche
            elif raison =='send':
                send_wait[ressource] = tâche
            else:
                raise RuntimeError('Raison inconnue %r' % raison)
        except StopIteration:
            print('Tâche terminée')
```

Ce code est une version un peu plus compliquée du planificateur de tâches de la partie (a). Cela nécessitera un peu d'étude, mais l'idée est que non seulement chaque tâche va générer, elle indiquera également une raison pour le faire (recevoir ou envoyer). En fonction de la raison, la tâche passera dans une zone d'attente. Le planificateur exécutera ensuite toutes les tâches disponibles ou attendra que des événements d'entrée/sortie se produisent lorsqu'il n'y a plus rien à faire.

Cela peut sembler un peu compliqué, mais ajoutez le code suivant qui implémente un serveur d'écho simple :

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
    print('Connexion de', address)
    while True:
        yield'recv', client
        data = client.recv(1000)
        if not data:
            break
        yield'send', client
        client.send(b'GOT:' + data)
    print('Connexion fermée')

if __name__ == '__main__':
    tasks.append(tcp_server(('',25000), echo_handler))
    run()
```

Exécutez ce serveur dans une fenêtre de terminal à part. Dans un autre terminal, connectez-vous à lui en utilisant une commande telle que `telnet` ou `nc`. Par exemple :

```bash
nc localhost 25000
Hello
Got: Hello
World
Got: World
```

Si vous n'avez pas accès à `nc` ou `telnet`, vous pouvez également utiliser Python lui-même :

```bash
python3 -m telnetlib localhost 25000
Hello
Got: Hello
World
Got: World
```

Si cela fonctionne, vous devriez voir la sortie vous être renvoyée. Pas seulement ça, si vous connectez plusieurs clients, ils fonctionneront tous en parallèle.

Cet usage astucieux des générateurs n'est probablement pas quelque chose que vous devriez avoir à coder directement. Cependant, ils sont utilisés dans certains packages avancés tels que `asyncio` qui a été ajouté à la bibliothèque standard en Python 3.4.
