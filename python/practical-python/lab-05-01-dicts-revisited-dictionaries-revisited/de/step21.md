# Übung 5.4: Gebundene Methoden

Ein subtiler Aspekt von Python ist, dass das Aufrufen einer Methode tatsächlich zwei Schritte umfasst und etwas, das als gebundene Methode bekannt ist. Beispielsweise:

```python
>>> s = goog.sell
>>> s
<bound method Stock.sell of Stock('GOOG', 100, 490.1)>
>>> s(25)
>>> goog.shares
75
>>>
```

Gebundene Methoden enthalten tatsächlich alle Bestandteile, die für das Aufrufen einer Methode erforderlich sind. Beispielsweise behalten sie einen Verweis auf die Funktion, die die Methode implementiert:

```python
>>> s.__func__
<function sell at 0x10049af50>
>>>
```

Dies ist der gleiche Wert wie der, der im `Stock`-Wörterbuch gefunden wird.

```python
>>> Stock.__dict__['sell']
<function sell at 0x10049af50>
>>>
```

Gebundene Methoden verzeichnen auch die Instanz, die das `self`-Argument ist.

```python
>>> s.__self__
Stock('GOOG',75,490.1)
>>>
```

Wenn Sie die Funktion mit `()` aufrufen, kommen alle Bestandteile zusammen. Beispielsweise führt das Aufrufen von `s(25)` tatsächlich folgendes aus:

```python
>>> s.__func__(s.__self__, 25)    # Identisch mit s(25)
>>> goog.shares
50
>>>
```
