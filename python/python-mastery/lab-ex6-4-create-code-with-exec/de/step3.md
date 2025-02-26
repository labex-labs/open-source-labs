# Benannte Tupel

In Übung 2.1 haben Sie mit `namedtuple`-Objekten im `collections`-Modul experimentiert. Um Ihre Erinnerung zu erneuern, hier ist, wie sie funktionierten:

```python
>>> from collections import namedtuple
>>> Stock = namedtuple('Stock', ['name','shares', 'price'])
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s[1]
100
>>>
```

Im Hintergrund erstellt die `namedtuple()`-Funktion Code als String und führt ihn mit `exec()` aus. Schauen Sie sich den Code an und staunen Sie:

```python
>>> import inspect
>>> print(inspect.getsource(namedtuple))
... schauen Sie sich die Ausgabe an...
>>>
```
