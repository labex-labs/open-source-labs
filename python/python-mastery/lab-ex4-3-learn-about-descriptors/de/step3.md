# Implementierung von Validatoren mit Descriptor

In diesem Schritt werden wir ein Validierungssystem mit Descriptor erstellen. Zunächst verstehen wir, was Descriptor sind und warum wir sie verwenden. Descriptor sind Python-Objekte, die das Descriptor-Protokoll implementieren, das die Methoden `__get__`, `__set__` oder `__delete__` umfasst. Sie ermöglichen es Ihnen, anzupassen, wie auf ein Attribut eines Objekts zugegriffen, es festgelegt oder gelöscht wird. In unserem Fall verwenden wir Descriptor, um ein Validierungssystem zu erstellen, das die Datenintegrität gewährleistet. Das bedeutet, dass die in unseren Objekten gespeicherten Daten immer bestimmten Kriterien entsprechen, wie z. B. einem bestimmten Datentyp oder einem positiven Wert.

Jetzt beginnen wir mit der Erstellung unseres Validierungssystems. Wir erstellen im Projektverzeichnis eine neue Datei namens `validate.py`. Diese Datei wird die Klassen enthalten, die unsere Validatoren implementieren.

```python
# validate.py

class Validator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class String(Validator):
    expected_type = str

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return value


class PositiveInteger(Validator):
    expected_type = int

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        if value < 0:
            raise ValueError('Expected a positive value')
        return value


class PositiveFloat(Validator):
    expected_type = float

    @classmethod
    def check(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        return float(value)
```

In der `validate.py`-Datei definieren wir zunächst eine Basisklasse namens `Validator`. Diese Klasse hat eine `__init__`-Methode, die einen `name`-Parameter akzeptiert, der verwendet wird, um das zu validierende Attribut zu identifizieren. Die `check`-Methode ist eine Klassenmethode, die einfach den ihr übergebenen Wert zurückgibt. Die `__set__`-Methode ist eine Descriptor-Methode, die aufgerufen wird, wenn ein Attribut an einem Objekt festgelegt wird. Sie ruft die `check`-Methode auf, um den Wert zu validieren, und speichert dann den validierten Wert im Wörterbuch des Objekts.

Anschließend definieren wir drei Unterklassen von `Validator`: `String`, `PositiveInteger` und `PositiveFloat`. Jede dieser Unterklassen überschreibt die `check`-Methode, um spezifische Validierungsüberprüfungen durchzuführen. Die `String`-Klasse überprüft, ob der Wert eine Zeichenkette ist, die `PositiveInteger`-Klasse überprüft, ob der Wert eine positive Ganzzahl ist, und die `PositiveFloat`-Klasse überprüft, ob der Wert eine positive Zahl (entweder eine Ganzzahl oder eine Fließkommazahl) ist.

Jetzt, da wir unsere Validatoren definiert haben, ändern wir unsere `Stock`-Klasse, um diese Validatoren zu verwenden. Wir erstellen eine neue Datei namens `stock_with_validators.py` und importieren die Validatoren aus der `validate.py`-Datei.

```python
# stock_with_validators.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String('name')
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

In der `stock_with_validators.py`-Datei definieren wir die `Stock`-Klasse und verwenden die Validatoren als Klassenattribute. Das bedeutet, dass jedes Mal, wenn ein Attribut an einem `Stock`-Objekt festgelegt wird, die `__set__`-Methode des entsprechenden Validators aufgerufen wird, um den Wert zu validieren. Die `__init__`-Methode initialisiert die Attribute des `Stock`-Objekts, und die `cost`, `sell` und `__repr__`-Methoden bieten zusätzliche Funktionalität.

Jetzt testen wir unsere auf Validatoren basierende `Stock`-Klasse. Wir öffnen ein Terminal, navigieren zum Projektverzeichnis und führen die `stock_with_validators.py`-Datei im interaktiven Modus aus.

```bash
cd ~/project
python3 -i stock_with_validators.py
```

Sobald der Python-Interpreter läuft, können wir einige Befehle ausprobieren, um das Validierungssystem zu testen.

```python
# Create a stock with valid values
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing to valid values
s.shares = 75
print(s.shares)  # Should return 75

# Try setting invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error setting shares to string: {e}")

try:
    s.shares = -50  # Should raise ValueError
except ValueError as e:
    print(f"Error setting negative shares: {e}")

exit()
```

Im Testcode erstellen wir zunächst ein `Stock`-Objekt mit gültigen Werten und geben seine Attribute aus, um zu überprüfen, ob sie korrekt festgelegt wurden. Dann versuchen wir, das `shares`-Attribut auf einen gültigen Wert zu ändern und geben es erneut aus, um die Änderung zu bestätigen. Schließlich versuchen wir, das `shares`-Attribut auf einen ungültigen Wert (eine Zeichenkette und eine negative Zahl) zu setzen und fangen die von den Validatoren ausgelösten Ausnahmen ab.

Beachten Sie, wie unser Code jetzt viel sauberer ist. Die `Stock`-Klasse muss nicht mehr alle diese Eigenschaftsmethoden implementieren - die Validatoren übernehmen alle Typüberprüfungen und Einschränkungen.

Descriptor haben es uns ermöglicht, ein wiederverwendbares Validierungssystem zu erstellen, das auf jedes Klassenattribut angewendet werden kann. Dies ist ein leistungsstarkes Muster für die Aufrechterhaltung der Datenintegrität in Ihrer Anwendung.
