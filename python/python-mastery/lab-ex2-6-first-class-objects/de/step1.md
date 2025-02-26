# Erstklassige Daten

In der Datei `portfolio.csv` haben Sie Daten gelesen, die in Spalten organisiert sind und so aussehen:

```python
"AA",100,32.20
"IBM",50,91.10
...
```

In früherem Code wurde diese Datenverarbeitung durch das harte Codieren aller Typumwandlungen durchgeführt. Beispielsweise:

```python
rows = csv.reader(f)
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

Diese Art der Umwandlung kann auch auf eine klügere Weise mit einigen Listenoperationen durchgeführt werden. Erstellen Sie eine Python-Liste, die die Umwandlungen enthält, die Sie auf jeder Spalte ausführen möchten:

```python
>>> coltypes = [str, int, float]
>>>
```

Der Grund, warum Sie diese Liste überhaupt erstellen können, ist, dass alles in Python "erstklassig" ist. Also, wenn Sie eine Liste von Funktionen haben möchten, ist das kein Problem.

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

Zip die Spaltentypen mit der Zeile und betrachten Sie das Ergebnis:

```python
>>> r = list(zip(coltypes, row))
>>> r
[(<class'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>,'32.20')]
>>>
```

Sie werden feststellen, dass dies eine Typumwandlung mit einem Wert zugeordnet hat. Beispielsweise ist `int` mit dem Wert `'100'` zugeordnet. Probieren Sie jetzt Folgendes aus:

```python
>>> record = [func(val) for func, val in zip(coltypes, row)]
>>> record
['AA', 100, 32.2]
>>>
```

Stellen Sie sicher, dass Sie verstehen, was im obigen Code passiert. In der Schleife ist die Variable `func` eine der Typumwandlungsfunktionen (z.B. `str`, `int` usw.) und die Variable `val` ist ein Wert wie `'AA'`, `'100'`. Der Ausdruck `func(val)` wandelt einen Wert um (ähnlich wie eine Typumwandlung).

Sie können es einen Schritt weiter gehen und mit Hilfe der Spaltenüberschriften Dictionaries erstellen. Beispielsweise:

```python
>>> dict(zip(headers, record))
{'name': 'AA','shares': 100, 'price': 32.2}
>>>
```

Wenn Sie möchten, können Sie alle diese Schritte auf einmal mit einem Dictionary Comprehension ausführen:

```python
>>> { name:func(val) for name, func, val in zip(headers, coltypes, row) }
{'name': 'AA','shares': 100, 'price': 32.2}
>>>
```
