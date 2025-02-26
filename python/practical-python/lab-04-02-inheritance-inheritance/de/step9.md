# "ist ein" - Beziehung

Die Vererbung etabliert eine Typbeziehung.

```python
class Shape:
...

class Circle(Shape):
...
```

Prüfe auf Objektinstanz.

```python
>>> c = Circle(4.0)
>>> isinstance(c, Shape)
True
>>>
```

_Wichtig: Idealerweise sollte jeder Code, der mit Instanzen der Elternklasse funktioniert, auch mit Instanzen der Kindklasse funktionieren._
