# Iteration: Protokoll

Betrachten Sie die `for`-Anweisung.

```python
for x in obj:
    # Anweisungen
```

Was geschieht hinter den Kulissen?

```python
_iter = obj.__iter__()        # Hole das Iterationsobjekt
while True:
    try:
        x = _iter.__next__()  # Hole das nächste Element
        # Anweisungen...
    except StopIteration:     # Es gibt keine weiteren Elemente
        break
```

Alle Objekte, die mit der `for-Schleife` zusammenarbeiten, implementieren dieses niedrigere Iterationsprotokoll.

Beispiel: Manuelle Iteration über eine Liste.

```python
>>> x = [1,2,3]
>>> it = x.__iter__()
>>> it
<listiterator object at 0x590b0>
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in? StopIteration
>>>
```
