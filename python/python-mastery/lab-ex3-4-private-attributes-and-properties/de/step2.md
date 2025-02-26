# Eigenschaften für berechnete Attribute

Früher haben Sie eine Klasse `Stock` definiert. Beispielsweise:

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>>
```

Verwenden Sie eine Eigenschaft, um `cost()` in ein Attribut umzuwandeln, das keine Klammern mehr erfordert. Beispielsweise:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.cost               # Eigenschaft. Berechnet die Kosten
49010.0
>>>
```
