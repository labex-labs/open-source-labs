# Änderung von Instanzdaten

Versuchen Sie, einem der oben genannten Instanzen ein neues Attribut zuzuweisen:

```python
>>> goog.date = "6/11/2007"
>>> goog.__dict__
... schauen Sie sich das Ergebnis an...
>>> ibm.__dict__
... schauen Sie sich das Ergebnis an...
>>>
```

In der obigen Ausgabe werden Sie feststellen, dass die `goog`-Instanz ein Attribut `date` hat, während die `ibm`-Instanz es nicht hat. Es ist wichtig zu beachten, dass Python keine Einschränkungen für die Attribute setzt. Beispielsweise sind die Attribute einer Instanz nicht auf die in der `__init__()`-Methode festgelegten beschränkt.

Anstatt ein Attribut zu setzen, versuchen Sie, einen neuen Wert direkt in das `__dict__`-Objekt einzugeben:

```python
>>> goog.__dict__['time'] = '9:45am'
>>> goog.time
'9:45am'
>>>
```

Hier erkennen Sie wirklich, dass eine Instanz eine Schicht über einem Wörterbuch ist.
