# Übung 1.13: Extrahieren einzelner Zeichen und Teilzeichenketten

Zeichenketten sind Arrays von Zeichen. Versuchen Sie, ein paar Zeichen zu extrahieren:

```python
>>> symbols[0]
?
>>> symbols[1]
?
>>> symbols[2]
?
>>> symbols[-1]        # Letztes Zeichen
?
>>> symbols[-2]        # Negative Indizes beginnen am Ende der Zeichenkette
?
>>>
```

In Python sind Zeichenketten schreibgeschützt.

Verifizieren Sie dies, indem Sie versuchen, das erste Zeichen von `symbols` in einen Kleinbuchstaben 'a' umzuwandeln.

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```
