# Verwendung von getattr()

Die Funktion `getattr()` ist extrem nützlich, um Code zu schreiben, der Objekte auf extrem generische Weise verarbeitet. Um dies zu veranschaulichen, betrachten Sie folgendes Beispiel, das eine Reihe von benutzerdefinierten Attributen ausgibt:

```python
>>> s= Stock('GOOG', 100, 490.1)
>>> fields = ['name','shares','price']
>>> for name in fields:
           print(name, getattr(s, name))

name GOOG
shares 100
price 490.1
>>>
```
