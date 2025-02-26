# Übung 7.8: Vereinfachung von Funktionsaufrufen

Im obigen Beispiel könnten Benutzer die Aufrufe wie `typedproperty('shares', int)` als etwas umständlich bei der Eingabe empfinden - insbesondere wenn sie oft wiederholt werden. Fügen Sie die folgenden Definitionen zur `typedproperty.py`-Datei hinzu:

```python
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
```

Nehmen Sie nun die `Stock`-Klasse auf und verwenden Sie stattdessen diese Funktionen:

```python
class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Ah, das ist etwas besser. Der wichtigste Punkt hier ist, dass Closures und `lambda` oft verwendet werden können, um Code zu vereinfachen und lästige Wiederholungen zu eliminieren. Dies ist oft vorteilhaft.
