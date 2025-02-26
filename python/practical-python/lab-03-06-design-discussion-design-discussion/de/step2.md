# Tiefes Konzept: "Duck Typing"

[Duck Typing](https://en.wikipedia.org/wiki/Duck_typing) ist ein Begriff der Computerprogrammierung, um zu bestimmen, ob ein Objekt für einen bestimmten Zweck verwendet werden kann. Es ist eine Anwendung des [Entenprüfungsverfahrens](https://en.wikipedia.org/wiki/Duck_test).

> Wenn es wie eine Ente aussieht, schwimmt wie eine Ente und quakt wie eine Ente, dann ist es wahrscheinlich eine Ente.

In der zweiten Version von `read_data()` oben erwartet die Funktion jedes iterierbare Objekt. Nicht nur die Zeilen einer Datei.

```python
def read_data(lines):
    records = []
    for line in lines:
     ...
        records.append(r)
    return records
```

Das bedeutet, dass wir es mit anderen _Zeilen_ verwenden können.

```python
# Eine CSV-Datei
lines = open('data.csv')
data = read_data(lines)

# Eine komprimierte Datei
lines = gzip.open('data.csv.gz','rt')
data = read_data(lines)

# Die Standard-Eingabe
lines = sys.stdin
data = read_data(lines)

# Eine Liste von Zeichenketten
lines = ['ACME,50,91.1','IBM,75,123.45',...]
data = read_data(lines)
```

Diese Designentscheidung bietet beträchtliche Flexibilität.

_Frage: Sollten wir uns dieser Flexibilität annähern oder dagegen kämpfen?_
