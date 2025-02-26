# Deskriptoren im Einsatz

Früher haben Sie eine Klasse `Stock` erstellt, die Slots, Eigenschaften und andere Funktionen nutzt. Alle diese Funktionen werden mithilfe des Deskriptor-Protokolls implementiert. Sehen Sie sich dies am Beispiel eines einfachen Experiments an.

Erstellen Sie zunächst ein `Stock`-Objekt und versuchen Sie, einige Attribute aufzurufen:

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>>
```

Beachten Sie nun, dass diese Attribute im Klassenwörterbuch sind.

```python
>>> Stock.__dict__.keys()
['sell', '__module__', '__weakref__', 'price', '_price','shares', '_shares',
'__slots__', 'cost', '__repr__', '__doc__', '__init__']
>>>
```

Versuchen Sie die folgenden Schritte, die veranschaulichen, wie Deskriptoren Werte an einer Instanz abrufen und setzen:

```python
>>> q = Stock.__dict__['shares']
>>> q.__get__(s)
100
>>> q.__set__(s,75)
>>> s.shares
75
>>> q.__set__(s, '75')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "stock.py", line 23, in shares
    raise TypeError('Expected an integer')
TypeError: Expected an integer
>>>
```

Das Ausführen von `__get__()` und `__set__()` erfolgt automatisch, wenn Sie Instanzen zugreifen.
