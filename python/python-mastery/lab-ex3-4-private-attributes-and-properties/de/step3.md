# Durchsetzung von Validierungsregeln

Verwenden Sie Eigenschaften und private Attribute, um das `shares`-Attribut der `Stock`-Klasse so zu modifizieren, dass nur ein nicht-negativer ganzzahliger Wert zugewiesen werden kann. Darüber hinaus modifizieren Sie das `price`-Attribut, sodass nur ein nicht-negativer Gleitkomma-Wert zugewiesen werden kann.

Das neue Objekt sollte fast genauso wie das alte funktionieren, außer dass zusätzliche Typ- und Wertprüfungen durchgeführt werden.

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.shares = 50          # OK
>>> s.shares = '50'
Traceback (most recent call last):
...
TypeError: Erwartet ganze Zahl
>>> s.shares = -10
Traceback (most recent call last):
...
ValueError: Anteile müssen >= 0 sein

>>> s.price = 123.45       # OK
>>> s.price = '123.45'
Traceback (most recent call last):
...
TypeError: Erwartet Gleitkomma
>>> s.price = -10.0
Traceback (most recent call last):
...
ValueError: Preis muss >= 0 sein
>>>
```
