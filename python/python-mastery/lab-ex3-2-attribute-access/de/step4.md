# Gebundene Methoden

Es mag überraschend sein, aber Methodenaufrufe werden auf die Maschinerie für einfache Attribute aufgetragen. Im Wesentlichen ist eine Methode ein Attribut, das ausgeführt wird, wenn Sie die erforderlichen Klammern () hinzufügen, um es wie eine Funktion aufzurufen. Beispielsweise:

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.cost           # Sucht die Methode auf
<bound method Stock.cost of <__main__.Stock object at 0x409530>>
>>> s.cost()         # Sucht die Methode auf und ruft sie auf
49010.0

>>> # Die gleichen Operationen mit getattr()
>>> getattr(s, 'cost')
<bound method Stock.cost of <__main__.Stock object at 0x409530>>
>>> getattr(s, 'cost')()
49010.0
>>>
```

Eine gebundene Methode ist an das Objekt angehängt, aus dem sie stammt. Wenn das Objekt geändert wird, wird die Methode die Änderungen sehen. Sie können das ursprüngliche Objekt anzeigen, indem Sie das Attribut `__self__` der Methode überprüfen.

```python
>>> c = s.cost
>>> c()
49010.0
>>> s.shares = 75
>>> c()
36757.5
>>> c.__self__
<__main__.Stock object at 0x409530>
>>> c.__func__
<function cost at 0x37cc30>
>>> c.__func__(c.__self__)      # Dies passiert hinter den Kulissen beim Aufruf von c()
36757.5
>>>
```

Versuchen Sie es mit der `sell()`-Methode, um sicherzustellen, dass Sie die Mechanik verstehen:

```python
>>> f = s.sell
>>> f.__func__(f.__self__, 25)     # Identisch mit s.sell(25)
>>> s.shares
50
>>>
```
