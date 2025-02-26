# Beispiel: Ein Verlauf aufzeichnen

Problem: Wir möchten einen Verlauf der letzten N Dinge haben. Lösung: Verwenden Sie eine `deque`.

```python
from collections import deque

history = deque(maxlen=N)
with open(filename) as f:
    for line in f:
        history.append(line)
     ...
```

Das Modul `collections` ist möglicherweise eines der nützlichsten Bibliotheksmodule für die Behandlung spezieller Arten von Datenverarbeitungsaufgaben wie der Tabellierung und Indizierung.

In dieser Übung betrachten wir einige einfache Beispiele. Beginnen Sie, indem Sie Ihr Programm `report.py` ausführen, so dass Sie das Aktienportfolio im interaktiven Modus geladen haben.

```bash
$ python3 -i report.py
```
