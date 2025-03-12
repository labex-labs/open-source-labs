# Hinzufügen von mathematischen Operationen

Derzeit unterstützt unsere `MutInt` - Klasse keine mathematischen Operationen wie Addition. In Python müssen wir für eine benutzerdefinierte Klasse spezielle Methoden implementieren, um solche Operationen zu ermöglichen. Diese speziellen Methoden werden auch als "Magie - Methoden" oder "Dunder - Methoden" bezeichnet, da sie von doppelten Unterstrichen umgeben sind. Fügen wir die Funktionalität für die Addition hinzu, indem wir die relevanten speziellen Methoden für arithmetische Operationen implementieren.

1. Öffnen Sie `mutint.py` in der WebIDE und aktualisieren Sie es mit dem folgenden Code:

```python
# mutint.py

class MutInt:
    """
    A mutable integer class that allows its value to be modified after creation.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialize with an integer value."""
        self.value = value

    def __str__(self):
        """Return a string representation for printing."""
        return str(self.value)

    def __repr__(self):
        """Return a developer-friendly string representation."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Support string formatting with format specifications."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Handle addition: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Handle reversed addition: other + self."""
        # For commutative operations like +, we can reuse __add__
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in-place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
```

Wir haben drei neue Methoden zur `MutInt` - Klasse hinzugefügt:

- `__add__()`: Diese Methode wird aufgerufen, wenn der `+` - Operator mit unserem `MutInt` - Objekt auf der linken Seite verwendet wird. Innerhalb dieser Methode überprüfen wir zunächst, ob der `other` - Operand eine Instanz von `MutInt` oder ein `int` ist. Wenn dies der Fall ist, führen wir die Addition aus und geben ein neues `MutInt` - Objekt mit dem Ergebnis zurück. Wenn der `other` - Operand etwas anderes ist, geben wir `NotImplemented` zurück. Dies sagt Python, andere Methoden zu versuchen oder einen `TypeError` auszulösen.
- `__radd__()`: Diese Methode wird aufgerufen, wenn der `+` - Operator mit unserem `MutInt` - Objekt auf der rechten Seite verwendet wird. Da die Addition eine kommutative Operation ist (d. h., `a + b` ist dasselbe wie `b + a`), können wir einfach die `__add__` - Methode wiederverwenden.
- `__iadd__()`: Diese Methode wird aufgerufen, wenn der `+=` - Operator auf unserem `MutInt` - Objekt verwendet wird. Anstatt ein neues Objekt zu erstellen, modifiziert sie das vorhandene `MutInt` - Objekt und gibt es zurück.

2. Erstellen Sie eine neue Testdatei namens `test_math_ops.py`, um diese neuen Methoden zu testen:

```python
# test_math_ops.py

from mutint import MutInt

# Create MutInt objects
a = MutInt(3)
b = MutInt(5)

# Test regular addition
c = a + b
print(f"a + b = {c}")

# Test addition with int
d = a + 10
print(f"a + 10 = {d}")

# Test reversed addition
e = 7 + a
print(f"7 + a = {e}")

# Test in-place addition
print(f"Before a += 5: a = {a}")
a += 5
print(f"After a += 5: a = {a}")

# Test in-place addition with reference sharing
f = a  # f and a point to the same object
print(f"Before a += 10: a = {a}, f = {f}")
a += 10
print(f"After a += 10: a = {a}, f = {f}")

# Test unsupported operation
try:
    result = a + 3.5  # Adding a float is not supported
    print(f"a + 3.5 = {result}")
except TypeError as e:
    print(f"Error when adding float: {e}")
```

In dieser Testdatei importieren wir zunächst die `MutInt` - Klasse. Dann erstellen wir einige `MutInt` - Objekte und führen verschiedene Arten von Additionsoperationen aus. Wir testen auch die in - place - Addition und den Fall, in dem eine nicht unterstützte Operation (Addition einer Fließkommazahl) versucht wird.

3. Führen Sie das Testskript aus:

```bash
python3 /home/labex/project/test_math_ops.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
a + b = MutInt(8)
a + 10 = MutInt(13)
7 + a = MutInt(10)
Before a += 5: a = MutInt(3)
After a += 5: a = MutInt(8)
Before a += 10: a = MutInt(8), f = MutInt(8)
After a += 10: a = MutInt(18), f = MutInt(18)
Error when adding float: unsupported operand type(s) for +: 'MutInt' and 'float'
```

Jetzt unterstützt unsere `MutInt` - Klasse grundlegende Additionsoperationen. Beachten Sie, dass sowohl `a` als auch `f` aktualisiert wurden, als wir `+=` verwendeten. Dies zeigt, dass `a += 10` das vorhandene Objekt modifiziert hat, anstatt ein neues zu erstellen.

Dieses Verhalten bei veränderlichen Objekten ähnelt Python's eingebauten veränderlichen Typen wie Listen. Beispielsweise:

```python
a = [1, 2, 3]
b = a
a += [4, 5]  # Both a and b are updated
```

Im Gegensatz dazu erstellt `+=` für unveränderliche Typen wie Tupel ein neues Objekt:

```python
c = (1, 2, 3)
d = c
c += (4, 5)  # c is a new object, d still points to the old one
```
