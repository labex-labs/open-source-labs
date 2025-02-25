# Übung 2.14: Weitere Sequenzoperationen

Experimentieren Sie interaktiv mit einigen der Sequenzreduktionsoperationen.

```python
>>> data = [4, 9, 1, 25, 16, 100, 49]
>>> min(data)
1
>>> max(data)
100
>>> sum(data)
204
>>>
```

Versuchen Sie, über die Daten zu iterieren.

```python
>>> for x in data:
        print(x)

4
9
...
>>> for n, x in enumerate(data):
        print(n, x)

0 4
1 9
2 1
...
>>>
```

Manchmal wird die `for`-Anweisung, `len()` und `range()` von Neulingen in einem schrecklichen Codefragment verwendet, das so aussieht, als wäre es aus der Tiefe eines rostigen C-Programms gekommen.

```python
>>> for n in range(len(data)):
        print(data[n])

4
9
1
...
>>>
```

Machen Sie das nicht! Nicht nur macht es jedem die Augen weh, es ist auch ineffizient bei der Arbeitsspeicherverwaltung und läuft viel langsamer. Verwenden Sie einfach eine normale `for`-Schleife, wenn Sie über Daten iterieren möchten. Verwenden Sie `enumerate()`, wenn Sie aus irgendeinem Grund den Index benötigen.
