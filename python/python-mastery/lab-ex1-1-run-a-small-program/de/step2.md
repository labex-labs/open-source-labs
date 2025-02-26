# Einige generatives Kunstwerk

Erstellen Sie das folgende Programm und speichern Sie es in einer Datei namens `art.py`:

```python
# art.py

import sys
import random

chars = '\|/'

def draw(rows, columns):
    for r in range(rows):
        print(''.join(random.choice(chars) for _ in range(columns)))

if __name__ == '__main__':
    if len(sys.argv)!= 3:
        raise SystemExit("Usage: art.py rows columns")
    draw(int(sys.argv[1]), int(sys.argv[2]))
```

Stellen Sie sicher, dass Sie dieses Programm von der Befehlszeile oder einem Terminal aus ausführen können.

```bash
python3 art.py 10 20
```

Wenn Sie den obigen Befehl ausführen, erhalten Sie eine Fehlermeldung und einen Stacktrace. Beheben Sie das Problem und führen Sie das Programm erneut aus. Sie sollten folgende Ausgabe erhalten:

```bash
python3 art.py 10 20
||||/\||//\//\|||\|\
///||\/||\//|\\|\\/\
|\////|//|||\//|/\||
|//\||\/|\///|\|\|/|
|/|//|/|/|\\/\/\||//
|\/\|\//\\//\|\||\\/
|||\\\\/\\\|/||||\/|
\\||\\\|\||||////\\|
//\//|/|\\|\//\|||\/
\\\|/\\|/|\\\|/|/\/|
```

## Wichtige Bemerkung

Es ist von absoluter Wichtigkeit, dass Sie in diesem Kurs in der Lage sind, normale Python-Programme zu bearbeiten, auszuführen und zu debuggen. Die Wahl des Editors, der IDE oder des Betriebssystems spielt keine Rolle, solange Sie interaktiv experimentieren und normale Python-Quelldateien erstellen können, die von der Befehlszeile aus ausgeführt werden können.
