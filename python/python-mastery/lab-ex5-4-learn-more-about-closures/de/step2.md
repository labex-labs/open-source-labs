# Closures als Codegenerator

In diesem Schritt werden wir lernen, wie Closures verwendet werden können, um Code dynamisch zu generieren. Insbesondere werden wir ein Typüberprüfungssystem für Klassenattribute mit Hilfe von Closures erstellen.

Zunächst verstehen wir, was Closures sind. Ein Closure ist ein Funktionsobjekt, das Werte aus dem umgebenden Geltungsbereich (Scope) behält, auch wenn diese nicht mehr im Speicher vorhanden sind. In Python werden Closures erstellt, wenn eine verschachtelte Funktion auf einen Wert aus ihrer umgebenden Funktion verweist.

Jetzt beginnen wir mit der Implementierung unseres Typüberprüfungssystems.

1. Erstellen Sie eine neue Datei namens `typedproperty.py` im Verzeichnis `/home/labex/project` mit folgendem Code:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    """
    Create a property with type checking.

    Args:
        name: The name of the property
        expected_type: The expected type of the property value

    Returns:
        A property object that performs type checking
    """
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

In diesem Code ist die `typedproperty`-Funktion ein Closure. Sie nimmt zwei Argumente entgegen: `name` und `expected_type`. Der `@property`-Decorator wird verwendet, um eine Getter-Methode für das Attribut zu erstellen, die den Wert des privaten Attributs abruft. Der `@value.setter`-Decorator erstellt eine Setter-Methode, die überprüft, ob der zu setzende Wert vom erwarteten Typ ist. Wenn nicht, wird ein `TypeError` ausgelöst.

2. Jetzt erstellen wir eine Klasse, die diese typisierten Attribute verwendet. Erstellen Sie eine Datei namens `stock.py` mit folgendem Code:

```python
from typedproperty import typedproperty

class Stock:
    """A class representing a stock with type-checked attributes."""

    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

In der `Stock`-Klasse verwenden wir die `typedproperty`-Funktion, um typüberprüfte Attribute für `name`, `shares` und `price` zu erstellen. Wenn wir eine Instanz der `Stock`-Klasse erstellen, wird die Typüberprüfung automatisch angewendet.

3. Erstellen wir eine Testdatei, um dies in Aktion zu sehen. Erstellen Sie eine Datei namens `test_stock.py` mit folgendem Code:

```python
from stock import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try to set an attribute with the wrong type
try:
    s.shares = "hundred"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

In dieser Testdatei erstellen wir zunächst ein `Stock`-Objekt mit korrekten Typen. Dann versuchen wir, das `shares`-Attribut auf einen String zu setzen, was einen `TypeError` auslösen sollte, da der erwartete Typ eine Ganzzahl ist.

4. Führen Sie die Testdatei aus:

```bash
python3 test_stock.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'int'>
```

Diese Ausgabe zeigt, dass die Typüberprüfung korrekt funktioniert.

5. Jetzt erweitern wir die `typedproperty.py`-Datei, indem wir bequeme Funktionen für häufige Typen hinzufügen. Fügen Sie folgenden Code ans Ende der Datei hinzu:

```python
def String(name):
    """Create a string property with type checking."""
    return typedproperty(name, str)

def Integer(name):
    """Create an integer property with type checking."""
    return typedproperty(name, int)

def Float(name):
    """Create a float property with type checking."""
    return typedproperty(name, float)
```

Diese Funktionen sind einfach Wrapper um die `typedproperty`-Funktion, was es einfacher macht, Attribute für häufige Typen zu erstellen.

6. Erstellen Sie eine neue Datei namens `stock_enhanced.py`, die diese bequemen Funktionen verwendet:

```python
from typedproperty import String, Integer, Float

class Stock:
    """A class representing a stock with type-checked attributes."""

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Diese `Stock`-Klasse verwendet die bequemen Funktionen, um typüberprüfte Attribute zu erstellen, was den Code lesbarer macht.

7. Erstellen Sie eine Testdatei `test_stock_enhanced.py`, um die erweiterte Version zu testen:

```python
from stock_enhanced import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try to set an attribute with the wrong type
try:
    s.price = "490.1"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

Diese Testdatei ist ähnlich der vorherigen, aber sie testet die erweiterte `Stock`-Klasse.

8. Führen Sie den Test aus:

```bash
python3 test_stock_enhanced.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'float'>
```

In diesem Schritt haben wir gezeigt, wie Closures verwendet werden können, um Code zu generieren. Die `typedproperty`-Funktion erstellt Eigenschaftsobjekte, die Typüberprüfung durchführen, und die `String`, `Integer` und `Float`-Funktionen erstellen spezialisierte Eigenschaften für häufige Typen.
