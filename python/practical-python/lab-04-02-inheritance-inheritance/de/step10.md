# Basisklasse `object`

Wenn eine Klasse keine Elternklasse hat, sieht man manchmal `object` als Basis verwendet.

```python
class Shape(object):
...
```

`object` ist die Elternklasse aller Objekte in Python.

\*Hinweis: Technisch gesehen ist dies nicht erforderlich, aber man sieht es oft als Überbleibsel aus der erforderlichen Verwendung in Python 2 angegeben. Wenn es weggelassen wird, erbt die Klasse immer noch implizit von `object`.
