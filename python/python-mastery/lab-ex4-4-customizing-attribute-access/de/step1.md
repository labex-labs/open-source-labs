# Slots vs. setattr

In früheren Übungen wurde `__slots__` verwendet, um die Instanzattribute einer Klasse aufzulisten. Der primäre Zweck von Slots ist die Optimierung der Arbeitsspeicher-Nutzung. Ein sekundärer Effekt ist, dass die erlaubten Attribute strikt auf die aufgelisteten begrenzt werden. Ein Nachteil von Slots ist, dass sie oft merkwürdig mit anderen Teilen von Python interagieren (z.B. können Klassen mit Slots nicht mit Mehrfachvererbung verwendet werden). Aus diesem Grund sollten Sie Slots eigentlich nur in speziellen Fällen verwenden.

Wenn Sie wirklich die Menge der erlaubten Attribute begrenzen möchten, wäre eine alternative Möglichkeit, eine `__setattr__()`-Methode zu definieren. Probieren Sie dieses Experiment aus:

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
        def __setattr__(self, name, value):
            if name not in { 'name','shares', 'price' }:
                raise AttributeError('No attribute %s' % name)
            super().__setattr__(name, value)

>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares = 75
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __setattr__
AttributeError: No attribute share
>>>
```

In diesem Beispiel gibt es keine Slots, aber die `__setattr__()`-Methode begrenzt immer noch die Attribute auf die in einem vorgegebenen Satz. Sie müssten wahrscheinlich darüber nachdenken, wie dieser Ansatz mit der Vererbung interagieren könnte (z.B. wenn Unterklassen neue Attribute hinzufügen möchten, müssten sie wahrscheinlich `__setattr__()` neu definieren, um es zu ermöglichen).
