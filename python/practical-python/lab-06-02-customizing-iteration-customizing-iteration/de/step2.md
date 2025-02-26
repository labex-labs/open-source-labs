# Generatoren

Ein Generator ist eine Funktion, die die Iteration definiert.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

Beispiel:

```python
>>> for x in countdown(10):
...   print(x, end=' ')
...
10 9 8 7 6 5 4 3 2 1
>>>
```

Ein Generator ist jede Funktion, die den `yield`-Befehl verwendet.

Das Verhalten von Generatoren unterscheidet sich von dem einer normalen Funktion. Wenn man eine Generatorfunktion aufruft, wird ein Generator-Objekt erstellt. Die Funktion wird nicht sofort ausgeführt.

```python
def countdown(n):
    # Ein Print-Befehl hinzugefügt
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1
```

```python
>>> x = countdown(10)
# ES GIBT KEINEN PRINT-BEFEHL
>>> x
# x ist ein Generator-Objekt
<generator object at 0x58490>
>>>
```

Die Funktion wird nur bei einem Aufruf von `__next__()` ausgeführt.

```python
>>> x = countdown(10)
>>> x
<generator object at 0x58490>
>>> x.__next__()
Counting down from 10
10
>>>
```

`yield` liefert einen Wert, aber suspendiert die Ausführung der Funktion. Die Funktion setzt bei dem nächsten Aufruf von `__next__()` fort.

```python
>>> x.__next__()
9
>>> x.__next__()
8
```

Wenn der Generator schließlich zurückkehrt, löst die Iteration einen Fehler aus.

```python
>>> x.__next__()
1
>>> x.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in? StopIteration
>>>
```

_Bemerkung: Eine Generatorfunktion implementiert das gleiche niedrigere Protokoll, das die for-Schleife bei Listen, Tupeln, Dictionaries, Dateien usw. verwendet._
