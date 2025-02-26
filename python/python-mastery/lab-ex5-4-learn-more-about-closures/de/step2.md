# Closures als Codegenerator

In Übung 4.3 haben Sie eine Sammlung von Deskriptorklassen entwickelt, die die Typüberprüfung von Objektattributen ermöglichten. Beispielsweise:

```python

class Stock:
    name = String()
    shares = Integer()
    price = Float()
```

Etwas ähnliches lässt sich auch mit Closures implementieren. Definieren Sie eine Datei `typedproperty.py` und legen Sie den folgenden Code darin ab:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value
```

Dies sieht ziemlich wild aus, aber die Funktion erstellt effektiv Code. Sie würden es in einer Klassendefinition wie folgt verwenden:

```python
from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Verifizieren Sie, dass diese Klasse die Typüberprüfung auf die gleiche Weise wie der Deskriptorcode durchführt.

Fügen Sie die Funktionen `String()`, `Integer()` und `Float()` zur `typedproperty.py`-Datei hinzu, sodass Sie folgenden Code schreiben können:

```python
from typedproperty import String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```
