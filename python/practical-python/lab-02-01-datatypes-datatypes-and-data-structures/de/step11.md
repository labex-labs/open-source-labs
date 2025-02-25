# Übung 2.1: Tupel

Am interaktiven Prompt erstellen Sie das folgende Tupel, das die obige Zeile repräsentiert, wobei die numerischen Spalten in richtige Zahlen umgewandelt sind:

```python
>>> t = (row[0], int(row[1]), float(row[2]))
>>> t
('AA', 100, 32.2)
>>>
```

Mit diesem können Sie jetzt die Gesamtkosten berechnen, indem Sie die Anzahl der Anteile und den Preis multiplizieren:

```python
>>> cost = t[1] * t[2]
>>> cost
3220.0000000000005
>>>
```

Ist die Mathematik in Python kaputt? Was ist mit der Antwort 3220.0000000000005 los?

Dies ist ein Artefakt der Gleitkomma-Hardware Ihres Computers, die nur in der Lage ist, Dezimalzahlen in Basis-2, nicht in Basis-10, genau darzustellen. Bei sogar einfachen Berechnungen mit Basis-10 Dezimalzahlen werden kleine Fehler eingeführt. Dies ist normal, obwohl es vielleicht etwas überraschend sein kann, wenn Sie es noch nie gesehen haben.

Dies passiert in allen Programmiersprachen, die Gleitkomma-Zahlen verwenden, wird aber oft bei der Ausgabe versteckt. Beispielsweise:

```python
>>> print(f'{cost:0.2f}')
3220.00
>>>
```

Tupel sind schreibgeschützt. Verifizieren Sie dies, indem Sie versuchen, die Anzahl der Anteile auf 75 zu ändern.

```python
>>> t[1] = 75
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```

Obwohl Sie die Tupel-Inhalte nicht ändern können, können Sie immer ein ganz neues Tupel erstellen, das das alte ersetzt.

```python
>>> t = (t[0], 75, t[2])
>>> t
('AA', 75, 32.2)
>>>
```

Wenn Sie eine vorhandene Variablennamen wie oben neu zuweisen, wird der alte Wert verworfen. Obwohl die obige Zuweisung so aussieht, als würden Sie das Tupel ändern, erstellen Sie tatsächlich ein neues Tupel und werfen das alte weg.

Tupel werden oft verwendet, um Werte in Variablen zu packen und wieder auszupacken. Versuchen Sie Folgendes:

```python
>>> name, shares, price = t
>>> name
'AA'
>>> shares
75
>>> price
32.2
>>>
```

Nehmen Sie die obigen Variablen und packen Sie sie wieder in ein Tupel

```python
>>> t = (name, 2*shares, price)
>>> t
('AA', 150, 32.2)
>>>
```
