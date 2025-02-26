# Übung 5.6: Einfache Eigenschaften

Eigenschaften sind eine nützliche Möglichkeit, "berechnete Attribute" einem Objekt hinzuzufügen. In `stock.py` haben Sie ein Objekt `Stock` erstellt. Beachten Sie, dass bei Ihrem Objekt eine leichte Inkonsistenz bei der Extraktion unterschiedlicher Arten von Daten besteht:

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>>
```

Insbesondere beobachten Sie, wie Sie die zusätzlichen Klammern `()` zu `cost` hinzufügen müssen, da es sich um eine Methode handelt.

Sie können die zusätzlichen Klammern `()` bei `cost()` entfernen, indem Sie es zu einer Eigenschaft machen. Nehmen Sie Ihre `Stock`-Klasse und ändern Sie sie so, dass die Kostenberechnung wie folgt funktioniert:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.cost
49010.0
>>>
```

Versuchen Sie, `s.cost()` als Funktion aufzurufen, und beobachten Sie, dass es jetzt nicht funktioniert, da `cost` als Eigenschaft definiert wurde.

```python
>>> s.cost()
... funktioniert nicht...
>>>
```

Dieser Änderung wird wahrscheinlich Ihr früheres `pcost.py`-Programm brechen. Sie müssen möglicherweise zurückgehen und die Klammern `()` bei der `cost()`-Methode entfernen.
