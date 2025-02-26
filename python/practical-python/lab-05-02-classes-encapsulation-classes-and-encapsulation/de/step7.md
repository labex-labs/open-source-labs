# Eigenschaften

Es gibt einen alternativen Ansatz zum vorherigen Muster.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Erwartet int')
        self._shares = value
```

Der normale Attribut-Zugriff löst jetzt die Getter- und Setter-Methoden unter `@property` und `@shares.setter` aus.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares         # Triggers @property
50
>>> s.shares = 75    # Triggers @shares.setter
>>>
```

Mit diesem Muster sind _keine Änderungen_ am Quellcode erforderlich. Der neue _Setter_ wird auch aufgerufen, wenn innerhalb der Klasse eine Zuweisung erfolgt, einschließlich innerhalb der `__init__()`-Methode.

```python
class Stock:
    def __init__(self, name, shares, price):
       ...
        # Diese Zuweisung ruft den unten stehenden Setter auf
        self.shares = shares
       ...

  ...
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Erwartet int')
        self._shares = value
```

Es besteht oft Verwirrung zwischen einer Eigenschaft und der Verwendung privater Namen. Obwohl eine Eigenschaft intern einen privaten Namen wie `_shares` verwendet, kann der Rest der Klasse (nicht die Eigenschaft) weiterhin einen Namen wie `shares` verwenden.

Eigenschaften sind auch nützlich für berechnete Datenattribute.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
  ...
```

Dies ermöglicht es Ihnen, die zusätzlichen Klammern zu weglassen und die Tatsache zu verbergen, dass es tatsächlich eine Methode ist:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares # Instanzvariable
100
>>> s.cost   # Berechneter Wert
49010.0
>>>
```
