# Verständnis des Descriptor-Protokolls

In diesem Schritt werden wir lernen, wie Descriptor in Python funktionieren, indem wir eine einfache `Stock`-Klasse erstellen. Descriptor in Python sind ein leistungsstarkes Feature, das es Ihnen ermöglicht, anzupassen, wie Attribute zugegriffen, festgelegt und gelöscht werden. Das Descriptor-Protokoll besteht aus drei speziellen Methoden: `__get__()`, `__set__()` und `__delete__()`. Diese Methoden definieren, wie sich der Descriptor verhält, wenn auf ein Attribut zugegriffen wird, ihm ein Wert zugewiesen wird oder es gelöscht wird.

Zunächst müssen wir im Projektverzeichnis eine neue Datei namens `stock.py` erstellen. Diese Datei wird unsere `Stock`-Klasse enthalten. Hier ist der Code, den Sie in die `stock.py`-Datei einfügen sollten:

```python
# stock.py

class Stock:
    __slots__ = ['_name', '_shares', '_price']

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._price = value

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

In dieser `Stock`-Klasse verwenden wir den `property`-Decorator, um Getter- und Setter-Methoden für die Attribute `name`, `shares` und `price` zu definieren. Diese Getter- und Setter-Methoden fungieren als Descriptor, was bedeutet, dass sie steuern, wie auf diese Attribute zugegriffen und sie festgelegt werden. Beispielsweise validieren die Setter-Methoden die Eingabewerte, um sicherzustellen, dass sie vom richtigen Typ sind und innerhalb eines akzeptablen Bereichs liegen.

Jetzt, da unsere `stock.py`-Datei fertig ist, öffnen wir eine Python-Shell, um mit der `Stock`-Klasse zu experimentieren und zu sehen, wie Descriptor in der Praxis funktionieren. Dazu öffnen Sie Ihr Terminal und führen Sie die folgenden Befehle aus:

```bash
cd ~/project
python3 -i stock.py
```

Die `-i`-Option im `python3`-Befehl teilt Python mit, eine interaktive Shell zu starten, nachdem die `stock.py`-Datei ausgeführt wurde. Auf diese Weise können wir direkt mit der `Stock`-Klasse interagieren, die wir gerade definiert haben.

In der Python-Shell erstellen wir ein Aktienobjekt und versuchen, auf seine Attribute zuzugreifen. So können Sie es tun:

```python
s = Stock('GOOG', 100, 490.10)
s.name      # Should return 'GOOG'
s.shares    # Should return 100
```

Wenn Sie auf die Attribute `name` und `shares` des Objekts `s` zugreifen, verwendet Python tatsächlich die `__get__`-Methode des Descriptors im Hintergrund. Die `property`-Decoratoren in unserer Klasse werden mit Descriptor implementiert, was bedeutet, dass sie den Zugriff auf und die Zuweisung von Attributen auf kontrollierte Weise handhaben.

Schauen wir uns genauer das Klassenwörterbuch an, um die Descriptor-Objekte zu sehen. Das Klassenwörterbuch enthält alle Attribute und Methoden, die in der Klasse definiert sind. Sie können die Schlüssel des Klassenwörterbuchs mit dem folgenden Code anzeigen:

```python
Stock.__dict__.keys()
```

Sie sollten eine Ausgabe ähnlich dieser sehen:

```
dict_keys(['__module__', '__slots__', '__init__', 'name', '_name', 'shares', '_shares', 'price', '_price', 'cost', 'sell', '__repr__', '__doc__'])
```

Die Schlüssel `name`, `shares` und `price` repräsentieren die Descriptor-Objekte, die von den `property`-Decoratoren erstellt wurden.

Jetzt untersuchen wir, wie Descriptor funktionieren, indem wir ihre Methoden manuell aufrufen. Wir verwenden den `shares`-Descriptor als Beispiel. So können Sie es tun:

```python
# Get the descriptor object for 'shares'
q = Stock.__dict__['shares']

# Use the __get__ method to retrieve the value
q.__get__(s, Stock)  # Should return 100

# Use the __set__ method to set a new value
q.__set__(s, 75)
s.shares  # Should now be 75

# Try to set an invalid value
try:
    q.__set__(s, '75')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

Wenn Sie auf ein Attribut wie `s.shares` zugreifen, ruft Python die `__get__`-Methode des Descriptors auf, um den Wert abzurufen. Wenn Sie einen Wert wie `s.shares = 75` zuweisen, ruft Python die `__set__`-Methode des Descriptors auf. Der Descriptor kann dann die Daten validieren und Fehler auslösen, wenn der Eingabewert ungültig ist.

Sobald Sie mit der `Stock`-Klasse und den Descriptorn experimentiert haben, können Sie die Python-Shell beenden, indem Sie den folgenden Befehl ausführen:

```python
exit()
```
