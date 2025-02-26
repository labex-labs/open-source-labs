# Alles ist ein Objekt

Zahlen, Zeichenketten, Listen, Funktionen, Ausnahmen, Klassen, Instanzen usw. sind alle Objekte. Das bedeutet, dass alle benannten Objekte als Daten weitergegeben, in Containern platziert usw. werden können, ohne Einschränkungen. Es gibt keine _besondere_ Arten von Objekten. Manchmal wird gesagt, dass alle Objekte "erstklassig" sind.

Ein einfaches Beispiel:

```python
>>> import math
>>> items = [abs, math, ValueError ]
>>> items
[<built-in function abs>,
  <module'math' (builtin)>,
  <type 'exceptions.ValueError'>]
>>> items[0](-45)
45
>>> items[1].sqrt(2)
1.4142135623730951
>>> try:
        x = int('not a number')
    except items[2]:
        print('Fehlgeschlagen!')
Fehlgeschlagen!
>>>
```

Hier ist `items` eine Liste, die eine Funktion, ein Modul und eine Ausnahme enthält. Man kann die Elemente in der Liste direkt anstelle der ursprünglichen Namen verwenden:

```python
items[0](-45)       # abs
items[1].sqrt(2)    # math
except items[2]:    # ValueError
```

Mit großer Macht kommt große Verantwortung. Nur weil man das kann, heißt nicht, dass man es sollte.

In dieser Übungsgruppe betrachten wir einige der Möglichkeiten, die aus erstklassigen Objekten resultieren.
