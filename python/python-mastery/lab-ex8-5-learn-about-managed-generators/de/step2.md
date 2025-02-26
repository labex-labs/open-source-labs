# Generatoren als Aufgaben für Netzwerkverbindungen

Öffnen Sie die Datei `server.py` und fügen Sie folgenden Code hinzu:

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
                raise RuntimeError('Unbekannter Grund %r' % reason)
        except StopIteration:
            print('Task abgeschlossen')
```

Dieser Code ist eine etwas komplexere Version des Task-Schedulers aus Teil (a). Er erfordert ein wenig Studium, aber die Idee ist, dass jede Aufgabe nicht nur pausiert, sondern auch einen Grund dafür angibt (Empfangen oder Senden). Je nachdem, um welchen Grund es sich handelt, wechselt die Aufgabe in einen Wartebereich. Der Scheduler führt dann alle verfügbaren Aufgaben aus oder wartet auf I/O-Ereignisse, wenn nichts mehr zu tun ist.

Es ist vielleicht alles ein bisschen kompliziert, aber fügen Sie folgenden Code hinzu, der einen einfachen Echo-Server implementiert:

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
    print('Verbindung von', address)
    while True:
        yield 'recv', client
        data = client.recv(1000)
        if not data:
            break
        yield 'send', client
        client.send(b'GOT:' + data)
    print('Verbindung geschlossen')

if __name__ == '__main__':
    tasks.append(tcp_server(('',25000), echo_handler))
    run()
```

Führen Sie diesen Server in einem eigenen Terminalfenster aus. In einem anderen Terminal können Sie sich mit einem Befehl wie `telnet` oder `nc` verbinden. Beispielsweise:

```bash
nc localhost 25000
Hello
Got: Hello
World
Got: World
```

Wenn Sie keinen Zugang zu `nc` oder `telnet` haben, können Sie auch Python selbst verwenden:

```bash
python3 -m telnetlib localhost 25000
Hello
Got: Hello
World
Got: World
```

Wenn es funktioniert, sollten Sie sehen, dass die Ausgabe zurück an Sie echoed wird. Nicht nur das, wenn Sie mehrere Clients verbinden, werden sie alle gleichzeitig arbeiten.

Diese raffinierte Verwendung von Generatoren ist etwas, das Sie wahrscheinlich nicht direkt in Ihrem Code implementieren müssen. Allerdings werden sie in bestimmten fortgeschrittenen Paketen wie `asyncio` verwendet, das in Python 3.4 der Standardbibliothek hinzugefügt wurde.
