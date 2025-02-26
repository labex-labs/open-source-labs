# Uniform access

Das letzte Beispiel zeigt, wie man eine einheitlichere Schnittstelle für ein Objekt erstellt. Wenn man das nicht tut, kann das Verwenden eines Objekts verwirrend sein:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> a = s.cost() # Methode
49010.0
>>> b = s.shares # Datenattribut
100
>>>
```

Warum ist die `()` für den Wert von `cost` erforderlich, aber nicht für `shares`? Eine Eigenschaft kann das beheben.
