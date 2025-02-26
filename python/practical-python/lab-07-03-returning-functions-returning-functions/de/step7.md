# Übung 7.7: Verwendung von Closures zur Vermeidung von Wiederholungen

Eine der leistungsfähigsten Eigenschaften von Closures ist ihre Verwendung bei der Erzeugung von wiederholendem Code. Wenn Sie sich an Übung 5.7 erinnern, denken Sie an den Code zur Definition einer Eigenschaft mit Typüberprüfung.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
  ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
  ...
```

Anstatt diesen Code immer wieder zu tippen, können Sie ihn mithilfe eines Closures automatisch erstellen.

Erstellen Sie eine Datei `typedproperty.py` und legen Sie den folgenden Code darin ab:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name
    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop
```

Versuchen Sie es nun, indem Sie eine Klasse wie diese definieren:

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

Versuchen Sie, eine Instanz zu erstellen und zu überprüfen, ob die Typüberprüfung funktioniert.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.name
'IBM'
>>> s.shares = '100'
... sollte einen TypeError erzeugen...
>>>
```
