# Übung 4.2: Hinzufügen einiger Methoden

Mit Klassen können Sie Funktionen an Ihre Objekte anfügen. Diese werden als Methoden bezeichnet und sind Funktionen, die auf den im Inneren eines Objekts gespeicherten Daten operieren. Fügen Sie eine `cost()`- und eine `sell()`-Methode zu Ihrem `Stock`-Objekt hinzu. Sie sollten so funktionieren:

```python
>>> import stock
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> s.cost()
49010.0
>>> s.shares
100
>>> s.sell(25)
>>> s.shares
75
>>> s.cost()
36757.5
>>>
```
