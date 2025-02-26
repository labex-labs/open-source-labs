# Alles zusammenbringen

In Übung 6.1 haben Sie eine Klasse `Structure` erstellt, die eine verallgemeinerte `__init__()`, `__setattr__()` und `__repr__()`-Methode definiert. Diese Klasse erforderte es den Benutzer, eine `_fields`-Klassenvariable wie folgt zu definieren:

```python
class Stock(Structure):
    _fields = ('name','shares','price')
```

Das Problem mit dieser Klasse ist, dass die `__init__()`-Funktion für die Zwecke von Hilfe und Übergabe von Schlüsselwortargumenten keine nützliche Argumentsignatur hatte. In Übung 6.2 haben Sie einen raffinierten Trick angewandt, der eine spezielle `self._init()`-Funktion beinhaltete. Beispielsweise:

```python
class Stock(Structure):
    _fields = ('name','shares', 'price')
    def __init__(self, name, shares, price):
        self._init()
  ...
```

Dies gab eine nützliche Signatur, aber jetzt ist die Klasse etwas merkwürdig, weil der Benutzer sowohl die `_fields`-Variable als auch die `__init__()`-Methode angeben muss.

Ihre Aufgabe ist es, die `_fields`-Variable mit Hilfe einiger Funktionsprüftechniken zu eliminieren. Zunächst stellen Sie fest, dass Sie die Argumentsignatur von `Stock` wie folgt erhalten können:

```python
>>> import inspect
>>> sig = inspect.signature(Stock)
>>> tuple(sig.parameters)
('name','shares', 'price')
>>>
```

Vielleicht können Sie die `_fields`-Variable aus der Argumentsignatur von `__init__()` setzen. Fügen Sie eine Klassenmethode `set_fields(cls)` zu `Structure` hinzu, die die `__init__()`-Funktion prüft und die `_fields`-Variable entsprechend setzt. Sie sollten Ihre neue Funktion wie folgt verwenden:

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

  ...

Stock.set_fields()
```

Die resultierende Klasse sollte auf die gleiche Weise wie zuvor funktionieren:

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

Verifizieren Sie die leicht modifizierte `Stock`-Klasse erneut mit Ihren Unit-Tests. Es werden immer noch Fehler auftreten, aber nichts sollte sich gegenüber der vorherigen Übung ändern.

Zu diesem Zeitpunkt ist alles immer noch etwas "hacky", aber Sie machen Fortschritte. Sie haben eine `Stock`-Strukturklasse mit einer nützlichen `__init__()`-Funktion, eine nützliche Darstellungzeichenfolge und die `__setattr__()`-Methode beschränkt die Menge der Attributnamen. Der zusätzliche Schritt, `set_fields()` aufzurufen, ist etwas ungewöhnlich, aber wir werden später noch darauf zurückkommen.
