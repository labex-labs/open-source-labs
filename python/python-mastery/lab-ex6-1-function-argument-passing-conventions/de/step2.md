# Erstellen einer Basisklasse für Strukturen

Nachdem wir nun ein gutes Verständnis der Übergabe von Funktionsargumenten haben, werden wir eine wiederverwendbare Basisklasse für Datenstrukturen erstellen. Dieser Schritt ist von entscheidender Bedeutung, da er uns hilft, den gleichen Code nicht immer wieder zu schreiben, wenn wir einfache Klassen erstellen, die Daten speichern. Durch die Verwendung einer Basisklasse können wir unseren Code vereinfachen und effizienter gestalten.

## Das Problem mit wiederholendem Code

In den früheren Übungen haben Sie eine `Stock`-Klasse wie folgt definiert:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Schauen Sie sich die `__init__`-Methode genau an. Sie werden feststellen, dass sie ziemlich wiederholend ist. Sie müssen jedes Attribut manuell einzeln zuweisen. Dies kann sehr mühsam und zeitaufwendig werden, insbesondere wenn Sie viele Klassen mit einer großen Anzahl von Attributen haben.

## Erstellen einer flexiblen Basisklasse

Lassen Sie uns eine `Structure`-Basisklasse erstellen, die die Attributzuweisung automatisch handhaben kann. Zunächst öffnen Sie die WebIDE und erstellen Sie eine neue Datei mit dem Namen `structure.py`. Fügen Sie dann den folgenden Code in diese Datei ein:

```python
# structure.py

class Structure:
    """
    A base class for creating simple data structures.
    Automatically populates object attributes from _fields and constructor arguments.
    """
    _fields = ()

    def __init__(self, *args):
        # Check that the number of arguments matches the number of fields
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")

        # Set the attributes
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
```

Diese Basisklasse hat mehrere wichtige Merkmale:

1. Sie definiert eine Klassenvariable `_fields`. Standardmäßig ist diese Variable leer. Diese Variable wird die Namen der Attribute enthalten, die die Klasse haben wird.
2. Sie prüft, ob die Anzahl der an den Konstruktor übergebenen Argumente mit der Anzahl der in `_fields` definierten Felder übereinstimmt. Wenn sie nicht übereinstimmen, wird ein `TypeError` ausgelöst. Dies hilft uns, Fehler frühzeitig zu erkennen.
3. Sie setzt die Attribute des Objekts mithilfe der Feldnamen und der als Argumente bereitgestellten Werte. Die `setattr`-Funktion wird verwendet, um die Attribute dynamisch zu setzen.

## Testen unserer Structure-Basisklasse

Jetzt erstellen wir einige Beispielklassen, die von der `Structure`-Basisklasse erben. Fügen Sie den folgenden Code in Ihre `structure.py`-Datei ein:

```python
# Example classes using Structure
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

class Point(Structure):
    _fields = ('x', 'y')

class Date(Structure):
    _fields = ('year', 'month', 'day')
```

Um zu testen, ob unsere Implementierung korrekt funktioniert, erstellen wir eine Testdatei mit dem Namen `test_structure.py`. Fügen Sie den folgenden Code in diese Datei ein:

```python
# test_structure.py
from structure import Stock, Point, Date

# Test Stock class
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}, shares: {s.shares}, price: {s.price}")

# Test Point class
p = Point(3, 4)
print(f"Point coordinates: ({p.x}, {p.y})")

# Test Date class
d = Date(2023, 11, 9)
print(f"Date: {d.year}-{d.month}-{d.day}")

# Test error handling
try:
    s2 = Stock('AAPL', 50)  # Missing price argument
    print("This should not print")
except TypeError as e:
    print(f"Error correctly caught: {e}")
```

Um den Test auszuführen, öffnen Sie Ihr Terminal und führen Sie den folgenden Befehl aus:

```bash
python3 test_structure.py
```

Sie sollten die folgende Ausgabe sehen:

```
Stock name: GOOG, shares: 100, price: 490.1
Point coordinates: (3, 4)
Date: 2023-11-9
Error correctly caught: Expected 3 arguments
```

Wie Sie sehen können, funktioniert unsere Basisklasse wie erwartet. Sie hat es viel einfacher gemacht, neue Datenstrukturen zu definieren, ohne den gleichen Boilerplate-Code wiederholt schreiben zu müssen.
