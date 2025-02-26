# Gebundene Methoden

Eine Methode, die noch nicht vom Funktionsaufrufoperator `()` aufgerufen wurde, wird als _gebundene Methode_ bezeichnet. Sie operiert auf der Instanz, aus der sie stammt.

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> s
<Stock object at 0x590d0>
>>> c = s.cost
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()
49010.0
>>>
```

Gebundene Methoden sind oft die Quelle von sorglosen, nicht offensichtlichen Fehlern. Beispielsweise:

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> print('Cost : %0.2f' % s.cost)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float argument required
>>>
```

Oder von absichtsvollen Verhaltensweisen, die schwer zu debuggen sind.

```python
f = open(filename, 'w')
...
f.close     # Ups, hat überhaupt nichts getan. `f` ist immer noch geöffnet.
```

In beiden Fällen ist der Fehler darauf zurückzuführen, dass man die abschließenden Klammern vergessen hat. Beispielsweise `s.cost()` oder `f.close()`.
