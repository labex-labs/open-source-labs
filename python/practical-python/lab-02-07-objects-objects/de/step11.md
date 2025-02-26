# Übung 2.24: Erstklassige Daten

In der Datei `portfolio.csv` lesen wir Daten, die in Spalten organisiert sind und so aussehen:

```csv
name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
```

In früherem Code haben wir das `csv`-Modul verwendet, um die Datei zu lesen, mussten aber immer noch manuelle Typumwandlungen vornehmen. Beispielsweise:

```python
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

Diese Art der Umwandlung kann auch auf eine cleverere Weise mit einigen Listenbasisoperationen durchgeführt werden.

Erstellen Sie eine Python-Liste, die die Namen der Umwandlungsfunktionen enthält, die Sie verwenden würden, um jede Spalte in den entsprechenden Typ umzuwandeln:

```python
>>> types = [str, int, float]
>>>
```

Der Grund, warum Sie diese Liste sogar erstellen können, ist, dass alles in Python _erstklassig_ ist. Also, wenn Sie eine Liste von Funktionen haben möchten, ist das kein Problem. Die Elemente in der von Ihnen erstellten Liste sind Funktionen zum Konvertieren eines Werts `x` in einen bestimmten Typ (z.B. `str(x)`, `int(x)`, `float(x)`).

Lesen Sie jetzt eine Zeile von Daten aus der obigen Datei:

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

Wie erwähnt, reicht diese Zeile nicht aus, um Berechnungen durchzuführen, weil die Typen falsch sind. Beispielsweise:

```python
>>> row[1] * row[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type'str'
>>>
```

Allerdings kann die Daten vielleicht mit den Typen, die Sie in `types` angegeben haben, zusammengeführt werden. Beispielsweise:

```python
>>> types[1]
<type 'int'>
>>> row[1]
'100'
>>>
```

Versuchen Sie, einen der Werte zu konvertieren:

```python
>>> types[1](row[1])     # Gleiches wie int(row[1])
100
>>>
```

Versuchen Sie, einen anderen Wert zu konvertieren:

```python
>>> types[2](row[2])     # Gleiches wie float(row[2])
32.2
>>>
```

Versuchen Sie die Berechnung mit den konvertierten Werten:

```python
>>> types[1](row[1])*types[2](row[2])
3220.0000000000005
>>>
```

Zip die Spaltentypen mit den Feldern und betrachten Sie das Ergebnis:

```python
>>> r = list(zip(types, row))
>>> r
[(<type'str'>, 'AA'), (<type 'int'>, '100'), (<type 'float'>,'32.20')]
>>>
```

Sie werden feststellen, dass dies einen Typumwandlung mit einem Wert zusammengeführt hat. Beispielsweise ist `int` mit dem Wert `'100'` zusammengeführt.

Die zusammengefügte Liste ist nützlich, wenn Sie alle Werte nacheinander umwandeln möchten. Versuchen Sie das:

```python
>>> converted = []
>>> for func, val in zip(types, row):
          converted.append(func(val))
...
>>> converted
['AA', 100, 32.2]
>>> converted[1] * converted[2]
3220.0000000000005
>>>
```

Stellen Sie sicher, dass Sie verstehen, was im obigen Code passiert. In der Schleife ist die Variable `func` eine der Typumwandlungsfunktionen (z.B. `str`, `int` usw.) und die Variable `val` ist einer der Werte wie `'AA'`, `'100'`. Der Ausdruck `func(val)` konvertiert einen Wert (ähnlich wie eine Typumwandlung).

Den obigen Code kann in eine einzelne Listenkomprehension komprimiert werden.

```python
>>> converted = [func(val) for func, val in zip(types, row)]
>>> converted
['AA', 100, 32.2]
>>>
```
