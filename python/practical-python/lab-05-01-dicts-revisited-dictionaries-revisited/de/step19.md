# Übung 5.2: Änderung von Instanzdaten

Versuchen Sie, einem der obigen Instanzen ein neues Attribut zuzuweisen:

```python
>>> goog.date = '6/11/2007'
>>> goog.__dict__
... schauen Sie sich das Ergebnis an...
>>> ibm.__dict__
... schauen Sie sich das Ergebnis an...
>>>
```

In der obigen Ausgabe werden Sie feststellen, dass die `goog`-Instanz ein Attribut `date` hat, während die `ibm`-Instanz es nicht hat. Es ist wichtig zu beachten, dass Python eigentlich keine Beschränkungen für Attribute stellt. Beispielsweise sind die Attribute einer Instanz nicht auf die in der `__init__()`-Methode eingerichteten beschränkt.

Anstatt ein Attribut zuzuweisen, versuchen Sie, einen neuen Wert direkt in das `__dict__`-Objekt zu platzieren:

```python
>>> goog.__dict__['time'] = '9:45am'
>>> goog.time
'9:45am'
>>>
```

Hier erkennen Sie wirklich die Tatsache, dass eine Instanz einfach eine Schicht über einem Wörterbuch ist. Hinweis: Es sollte betont werden, dass das direkte Manipulieren des Wörterbuchs ungewöhnlich ist - Sie sollten immer Ihren Code so schreiben, dass Sie die (.)-Syntax verwenden.
