# Erstellen einer `__init__()`-Funktion

In Übung 6.3 haben Sie Code geschrieben, der die Signatur der `__init__()`-Methode überprüft, um die Attributnamen in einer `_fields`-Klassenvariable festzulegen. Beispielsweise:

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

Stock.set_fields()
```

Anstatt die `__init__()`-Methode zu überprüfen, schreiben Sie eine Klassenmethode `create_init(cls)`, die eine `__init__()`-Methode aus dem Wert von `_fields` erstellt. Verwenden Sie die `exec()`-Funktion, um dies wie oben gezeigt zu tun. So wird ein Benutzer sie verwenden:

```python
class Stock(Structure):
    _fields = ('name','shares', 'price')

Stock.create_init()
```

Die resultierende Klasse sollte genauso wie zuvor funktionieren:

```python
>>> s = Stock(name='GOOG', shares=100, price=490.1)
>>> s
Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 12, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>>
```

Ändern Sie die `Stock`-Klasse im Gange, um die `create_init()`-Funktion wie gezeigt zu verwenden. Überprüfen Sie dies wie zuvor mit Ihren Unit-Tests.

Während Sie dabei sind, entfernen Sie die `_init()`- und `set_fields()`-Methoden von der `Structure`-Klasse - dieser Ansatz war etwas seltsam.
