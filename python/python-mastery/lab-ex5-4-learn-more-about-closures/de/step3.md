# Elimination von Eigenschaftsnamen mit Descriptoren

Im vorherigen Schritt mussten wir bei der Erstellung von typisierten Eigenschaften die Eigenschaftsnamen explizit angeben. Dies ist redundant, da die Eigenschaftsnamen bereits in der Klassendefinition festgelegt sind. In diesem Schritt werden wir Descriptor (Beschreiber) verwenden, um diese Redundanz zu beseitigen.

Ein Descriptor in Python ist ein spezielles Objekt, das steuert, wie der Zugriff auf Attribute funktioniert. Wenn Sie die `__set_name__`-Methode in einem Descriptor implementieren, kann dieser automatisch den Attributnamen aus der Klassendefinition abrufen.

Beginnen wir damit, eine neue Datei zu erstellen.

1. Erstellen Sie eine neue Datei namens `improved_typedproperty.py` mit folgendem Code:

```python
# improved_typedproperty.py

class TypedProperty:
    """
    A descriptor that performs type checking.

    This descriptor automatically captures the attribute name from the class definition.
    """
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        # This method is called when the descriptor is assigned to a class attribute
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {self.expected_type}')
        instance.__dict__[self.name] = value

# Convenience functions
def String():
    """Create a string property with type checking."""
    return TypedProperty(str)

def Integer():
    """Create an integer property with type checking."""
    return TypedProperty(int)

def Float():
    """Create a float property with type checking."""
    return TypedProperty(float)
```

Dieser Code definiert eine Descriptor-Klasse namens `TypedProperty`, die den Typ von Werten überprüft, die an Attribute zugewiesen werden. Die `__set_name__`-Methode wird automatisch aufgerufen, wenn der Descriptor einem Klassenattribut zugewiesen wird. Dadurch kann der Descriptor den Attributnamen erfassen, ohne dass wir ihn manuell angeben müssen.

Als Nächstes erstellen wir eine Klasse, die diese verbesserten typisierten Eigenschaften verwendet.

2. Erstellen Sie eine neue Datei namens `stock_improved.py`, die die verbesserten typisierten Eigenschaften verwendet:

```python
from improved_typedproperty import String, Integer, Float

class Stock:
    """A class representing a stock with type-checked attributes."""

    # No need to specify property names anymore
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Beachten Sie, dass wir die Eigenschaftsnamen nicht mehr angeben müssen, wenn wir die typisierten Eigenschaften erstellen. Der Descriptor wird automatisch den Attributnamen aus der Klassendefinition abrufen.

Jetzt testen wir unsere verbesserte Klasse.

3. Erstellen Sie eine Testdatei `test_stock_improved.py`, um die verbesserte Version zu testen:

```python
from stock_improved import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try setting attributes with wrong types
try:
    s.name = 123  # Should raise TypeError
    print("Name type check failed")
except TypeError as e:
    print(f"Name type check succeeded: {e}")

try:
    s.shares = "hundred"  # Should raise TypeError
    print("Shares type check failed")
except TypeError as e:
    print(f"Shares type check succeeded: {e}")

try:
    s.price = "490.1"  # Should raise TypeError
    print("Price type check failed")
except TypeError as e:
    print(f"Price type check succeeded: {e}")
```

Schließlich führen wir den Test aus, um zu sehen, ob alles wie erwartet funktioniert.

4. Führen Sie den Test aus:

```bash
python3 test_stock_improved.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Name type check succeeded: Expected <class 'str'>
Shares type check succeeded: Expected <class 'int'>
Price type check succeeded: Expected <class 'float'>
```

In diesem Schritt haben wir unser Typüberprüfungssystem verbessert, indem wir Descriptor und die `__set_name__`-Methode verwendet haben. Dies beseitigt die redundante Angabe der Eigenschaftsnamen, macht den Code kürzer und verringert die Wahrscheinlichkeit von Fehlern.

Die `__set_name__`-Methode ist ein sehr nützliches Merkmal von Descriptor. Sie ermöglicht es ihnen, automatisch Informationen darüber zu sammeln, wie sie in einer Klassendefinition verwendet werden. Dies kann genutzt werden, um APIs zu erstellen, die einfacher zu verstehen und zu verwenden sind.
