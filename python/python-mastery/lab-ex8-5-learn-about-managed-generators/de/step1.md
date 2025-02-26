# Generatoren als Aufgaben

Wenn Sie die Datei `multitask.py` definieren, fügen Sie folgenden Code hinzu:

```python
# multitask.py

from collections import deque

tasks = deque()
def run():
    while tasks:
        task = tasks.popleft()
        try:
            task.send(None)
            tasks.append(task)
        except StopIteration:
            print('Task abgeschlossen')
```

Dieser Code implementiert einen kleinen Task-Scheduler, der Generator-Funktionen ausführt. Testen Sie es, indem Sie es mit folgenden Funktionen ausführen.

```python
# multitask.py
...

def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield
        n -= 1

def countup(n):
    x = 0
    while x < n:
        print('Los geht es', x)
        yield
        x += 1

if __name__ == '__main__':
    tasks.append(countdown(10))
    tasks.append(countdown(5))
    tasks.append(countup(20))
    run()
```

Wenn Sie das ausführen, sollten Sie die Ausgabe aller Generatoren miteinander durchgemischt sehen. Beispielsweise:

```python
T-minus 10
T-minus 5
Los geht es 0
T-minus 9
T-minus 4
Los geht es 1
T-minus 8
T-minus 3
Los geht es 2
T-minus 7
T-minus 2
Los geht es 3
T-minus 6
T-minus 1
Los geht es 4
T-minus 5
Task abgeschlossen
Los geht es 5
T-minus 4
Los geht es 6
T-minus 3
Los geht es 7
T-minus 2
Los geht es 8
T-minus 1
Los geht es 9
Task abgeschlossen
Los geht es 10
Los geht es 11
Los geht es 12
Los geht es 13
Los geht es 14
Los geht es 15
Los geht es 16
Los geht es 17
Los geht es 18
Los geht es 19
Task abgeschlossen
```

Das ist interessant, aber nicht besonders überzeugend. Gehen Sie zum nächsten Beispiel über.
