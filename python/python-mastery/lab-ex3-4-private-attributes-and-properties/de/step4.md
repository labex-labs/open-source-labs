# Hinzufügen von `__slots__`

Modifizieren Sie Ihre neue `Stock`-Klasse, um `__slots__` zu verwenden. Sie werden feststellen, dass Sie einen anderen Satz von Attributnamen als zuvor verwenden müssen - insbesondere müssen Sie die privaten Attributnamen auflisten (z.B., wenn eine Eigenschaft einen Wert in einem Attribut `_shares` speichert, ist das der Name, den Sie in `__slots__` auflisten). Vergewissern Sie sich, dass die Klasse weiterhin funktioniert und dass Sie keine neuen Attribute mehr hinzufügen können.

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.spam = 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Stock' Objekt hat kein Attribut 'spam'
>>>
```
