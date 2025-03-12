# Hinzufügen von Typkonvertierungen

Unsere `MutInt` - Klasse unterstützt derzeit Addition und Vergleichsoperationen. Allerdings funktioniert sie nicht mit Python's eingebauten Konvertierungsfunktionen wie `int()` und `float()`. Diese Konvertierungsfunktionen sind in Python sehr nützlich. Beispielsweise wenn Sie einen Wert in eine Ganzzahl oder eine Fließkommazahl umwandeln möchten, um verschiedene Berechnungen oder Operationen durchzuführen, verlassen Sie sich auf diese Funktionen. Fügen wir daher unserer `MutInt` - Klasse die Fähigkeit hinzu, mit ihnen zu arbeiten.

1. Öffnen Sie `mutint.py` in der WebIDE und aktualisieren Sie es mit dem folgenden Code:

```python
# mutint.py

from functools import total_ordering

@total_ordering
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
        """Return a developer - friendly string representation."""
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
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in - place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less - than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Convert to int."""
        return self.value

    def __float__(self):
        """Convert to float."""
        return float(self.value)

    __index__ = __int__  # Support array indexing and other operations requiring an index
```

Wir haben drei neue Methoden zur `MutInt` - Klasse hinzugefügt:

1. `__int__()`: Diese Methode wird aufgerufen, wenn Sie die `int()` - Funktion auf ein Objekt unserer `MutInt` - Klasse anwenden. Beispielsweise, wenn Sie ein `MutInt` - Objekt `a` haben und Sie `int(a)` schreiben, wird Python die `__int__()` - Methode des `a` - Objekts aufrufen.
2. `__float__()`: Ebenso wird diese Methode aufgerufen, wenn Sie die `float()` - Funktion auf unser `MutInt` - Objekt anwenden.
3. `__index__()`: Diese Methode wird für Operationen verwendet, die speziell einen Ganzzahlindex erfordern. Beispielsweise, wenn Sie ein Element in einer Liste über einen Index zugreifen möchten oder Bitlängenoperationen durchführen, benötigt Python einen Ganzzahlindex.

Die `__index__` - Methode ist für Operationen, die einen Ganzzahlindex erfordern, wie Listenindizierung, Slicing und Bitlängenoperationen, von entscheidender Bedeutung. In unserer einfachen Implementierung setzen wir sie gleich `__int__`, da der Wert unseres `MutInt` - Objekts direkt als Ganzzahlindex verwendet werden kann.

2. Erstellen Sie eine neue Testdatei namens `test_conversions.py`, um diese neuen Methoden zu testen:

```python
# test_conversions.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test conversions
print(f"int(a): {int(a)}")
print(f"float(a): {float(a)}")

# Test using as an index
names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
print(f"names[a]: {names[a]}")

# Test using in bit operations (requires __index__)
print(f"1 << a: {1 << a}")  # Shift left by 3

# Test hex/oct/bin functions (requires __index__)
print(f"hex(a): {hex(a)}")
print(f"oct(a): {oct(a)}")
print(f"bin(a): {bin(a)}")

# Modify and test again
a.value = 5
print(f"\nAfter changing value to 5:")
print(f"int(a): {int(a)}")
print(f"names[a]: {names[a]}")
```

3. Führen Sie das Testskript aus:

```bash
python3 /home/labex/project/test_conversions.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
int(a): 3
float(a): 3.0
names[a]: Paula
1 << a: 8
hex(a): 0x3
oct(a): 0o3
bin(a): 0b11

After changing value to 5:
int(a): 5
names[a]: Lewis
```

Jetzt kann unsere `MutInt` - Klasse in Standard - Python - Typen umgewandelt werden und in Operationen verwendet werden, die einen Ganzzahlindex erfordern.

Die `__index__` - Methode ist besonders wichtig. Sie wurde in Python eingeführt, um es Objekten zu ermöglichen, in Situationen verwendet zu werden, in denen ein Ganzzahlindex erforderlich ist, wie z. B. bei der Listenindizierung, bitweisen Operationen und verschiedenen Funktionen wie `hex()`, `oct()` und `bin()`.

Mit diesen Ergänzungen ist unsere `MutInt` - Klasse jetzt eine ziemlich vollständige primitive Typklasse. Sie kann in den meisten Kontexten verwendet werden, in denen eine normale Ganzzahl verwendet würde, mit dem zusätzlichen Vorteil, dass sie veränderlich ist.

## Vollständige MutInt - Implementierung

Hier ist unsere vollständige `MutInt` - Implementierung mit allen Funktionen, die wir hinzugefügt haben:

```python
# mutint.py

from functools import total_ordering

@total_ordering
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
        """Return a developer - friendly string representation."""
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
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in - place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less - than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Convert to int."""
        return self.value

    def __float__(self):
        """Convert to float."""
        return float(self.value)

    __index__ = __int__  # Support array indexing and other operations requiring an index
```

Diese Implementierung deckt die wichtigsten Aspekte der Erstellung eines neuen primitiven Typs in Python ab. Um sie noch vollständiger zu machen, könnten Sie zusätzliche Methoden für andere Operationen wie Subtraktion, Multiplikation, Division usw. implementieren.
