# Ein Coroutine-Beispiel

Das Erlernen von Coroutinen kann ein bisschen tricky sein. Hier ist ein Beispielprogramm, das die gleiche Aufgabe wie das Übungsblatt 8.2 durchführt, aber mit Coroutinen. Nehmen Sie dieses Programm und kopieren Sie es in eine Datei namens `cofollow.py`.

```python
# cofollow.py
import os
import time

# Datenquelle
def follow(filename,target):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line!= '':
                target.send(line)
            else:
                time.sleep(0.1)

# Dekorator für Coroutine-Funktionen
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args,**kwargs):
        f = func(*args,**kwargs)
        f.send(None)
        return f
    return start

# Beispiel-Coroutine
@consumer
def printer():
    while True:
        item = yield     # Empfange ein mir gesendetes Element
        print(item)

# Beispielgebrauch
if __name__ == '__main__':
    follow('stocklog.csv',printer())
```

Führen Sie dieses Programm aus und stellen Sie sicher, dass es Ausgabe erzeugt. Stellen Sie sicher, dass Sie verstehen, wie die verschiedenen Teile zusammenhängen.
