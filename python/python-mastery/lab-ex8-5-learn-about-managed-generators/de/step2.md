# Erstellen eines Task-Schedulers mit Generatoren

In der Programmierung ist ein Task-Scheduler (Aufgabenplaner) ein wichtiges Werkzeug, das hilft, mehrere Aufgaben effizient zu verwalten und auszuführen. In diesem Abschnitt verwenden wir Generatoren, um einen einfachen Task-Scheduler zu erstellen, der mehrere Generatorfunktionen gleichzeitig ausführen kann. Dies zeigt Ihnen, wie Generatoren verwaltet werden können, um kooperatives Multitasking (gemeinsames Mehrfachverarbeitung) durchzuführen, was bedeutet, dass Aufgaben abwechselnd ausgeführt werden und die Ausführungszeit teilen.

Zunächst müssen Sie eine neue Datei erstellen. Navigieren Sie zum Verzeichnis `/home/labex/project` und erstellen Sie eine Datei namens `multitask.py`. Diese Datei wird den Code für unseren Task-Scheduler enthalten.

```python
# multitask.py

from collections import deque

# Task queue
tasks = deque()

# Simple task scheduler
def run():
    while tasks:
        task = tasks.popleft()  # Get the next task
        try:
            task.send(None)     # Resume the task
            tasks.append(task)  # Put it back in the queue
        except StopIteration:
            print('Task done')  # Task is complete

# Example task 1: Countdown
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield              # Pause execution
        n -= 1

# Example task 2: Count up
def countup(n):
    x = 0
    while x < n:
        print('Up we go', x)
        yield              # Pause execution
        x += 1
```

Jetzt zerlegen wir, wie dieser Task-Scheduler funktioniert:

1. Wir verwenden eine `deque` (Doppel-Ende-Warteschlange), um unsere Generator-Aufgaben zu speichern. Eine `deque` ist eine Datenstruktur, die es Ihnen ermöglicht, Elemente effizient von beiden Enden hinzuzufügen und zu entfernen. Sie ist eine gute Wahl für unsere Aufgabenwarteschlange, da wir Aufgaben am Ende hinzufügen und am Anfang entfernen müssen.
2. Die `run()`-Funktion ist das Herzstück unseres Task-Schedulers. Sie nimmt die Aufgaben nacheinander aus der Warteschlange:
   - Sie setzt jede Aufgabe mit `send(None)` fort. Dies ist ähnlich wie das Verwenden von `next()` auf einem Generator. Es sagt dem Generator, die Ausführung dort fortzusetzen, wo sie aufgehört hat.
   - Nachdem die Aufgabe einen Wert zurückgegeben hat, wird sie wieder an das Ende der Warteschlange hinzugefügt. Auf diese Weise hat die Aufgabe später wieder die Möglichkeit, ausgeführt zu werden.
   - Wenn eine Aufgabe abgeschlossen ist (wenn `StopIteration` ausgelöst wird), wird sie aus der Warteschlange entfernt. Dies zeigt an, dass die Aufgabe ihre Ausführung beendet hat.
3. Jede `yield`-Anweisung in unseren Generator-Aufgaben fungiert als Pausepunkt. Wenn ein Generator eine `yield`-Anweisung erreicht, wird seine Ausführung angehalten und die Kontrolle an den Scheduler zurückgegeben. Dies ermöglicht es anderen Aufgaben, ausgeführt zu werden.

Dieser Ansatz implementiert kooperatives Multitasking. Jede Aufgabe gibt die Kontrolle freiwillig an den Scheduler zurück, wodurch andere Aufgaben ausgeführt werden können. Auf diese Weise können mehrere Aufgaben die Ausführungszeit teilen und gleichzeitig ausgeführt werden.
