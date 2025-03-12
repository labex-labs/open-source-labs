# Aufbau eines Netzwerkservers mit Generatoren

In diesem Abschnitt nehmen wir das Konzept eines Task-Schedulers, das wir gelernt haben, und erweitern es, um etwas Praktikableres zu erstellen: einen einfachen Netzwerkserver. Dieser Server kann mithilfe von Generatoren mehrere Client-Verbindungen gleichzeitig verwalten. Generatoren sind eine leistungsstarke Python-Funktion, die es Funktionen ermöglicht, ihre Ausführung anzuhalten und fortzusetzen, was sehr nützlich ist, um mehrere Aufgaben ohne Blockierung zu verwalten.

Zunächst müssen Sie eine neue Datei namens `server.py` im Verzeichnis `/home/labex/project` erstellen. Diese Datei wird den Code für unseren Netzwerkserver enthalten.

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

Dieser verbesserte Scheduler ist etwas komplizierter als der vorherige, aber er folgt denselben grundlegenden Ideen. Lassen Sie uns die Hauptunterschiede aufschlüsseln:

1. Aufgaben können einen Grund ('recv' oder 'send') und eine Ressource (einen Socket) zurückgeben. Dies bedeutet, dass eine Aufgabe dem Scheduler mitteilen kann, dass sie entweder auf das Empfangen oder Senden von Daten über einen bestimmten Socket wartet.
2. Je nach Grund wird die Aufgabe in einen anderen Wartebereich verschoben. Wenn eine Aufgabe auf das Empfangen von Daten wartet, geht sie in das `recv_wait`-Wörterbuch. Wenn sie auf das Senden von Daten wartet, geht sie in das `send_wait`-Wörterbuch.
3. Die `select()`-Funktion wird verwendet, um herauszufinden, welche Sockets für E/A-Operationen bereit sind. Diese Funktion überprüft die Sockets in den `recv_wait`- und `send_wait`-Wörterbüchern und gibt diejenigen zurück, die entweder auf das Empfangen oder Senden von Daten bereit sind.
4. Wenn ein Socket bereit ist, wird die zugehörige Aufgabe zurück in die aktive Warteschlange verschoben. Dies ermöglicht es der Aufgabe, ihre Ausführung fortzusetzen und die E/A-Operation auszuführen, auf die sie gewartet hat.

Durch die Verwendung dieser Techniken können unsere Aufgaben effizient auf Netzwerk-E/A warten, ohne die Ausführung anderer Aufgaben zu blockieren. Dies macht unseren Netzwerkserver reaktionsfähiger und in der Lage, mehrere Client-Verbindungen gleichzeitig zu verwalten.
