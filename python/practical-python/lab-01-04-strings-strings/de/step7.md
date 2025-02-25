# String-Immutabilität

Strings sind "immutable" oder schreibgeschützt. Einmal erstellt, kann der Wert nicht geändert werden.

```python
>>> s = 'Hello World'
>>> s[1] = 'a'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError:'str' object does not support item assignment
>>>
```

**Alle Operationen und Methoden, die String-Daten manipulieren, erzeugen immer neue Strings.**
