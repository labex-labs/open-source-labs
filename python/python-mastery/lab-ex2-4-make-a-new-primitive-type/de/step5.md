# Hinzufügen von Typkonvertierungen

Unsere `MutInt`-Klasse unterstützt derzeit Additions- und Vergleichsoperationen. Sie funktioniert jedoch nicht mit den in Python integrierten Konvertierungsfunktionen wie `int()` und `float()`. Diese Konvertierungsfunktionen sind in Python sehr nützlich. Wenn Sie beispielsweise einen Wert in eine Ganzzahl (Integer) oder eine Gleitkommazahl (Floating-Point Number) für verschiedene Berechnungen oder Operationen konvertieren möchten, verlassen Sie sich auf diese Funktionen. Fügen wir also unserer `MutInt`-Klasse die Fähigkeit hinzu, mit ihnen zu arbeiten.

1. Öffnen Sie `mutint.py` in der WebIDE und aktualisieren Sie es mit dem folgenden Code:

```python
# mutint.py

from functools import total_ordering

@total_ordering
class MutInt:
    """
    Eine veränderliche (mutable) Integer-Klasse, die es ermöglicht, ihren Wert nach der Erstellung zu ändern.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialisierung mit einem Integer-Wert."""
        self.value = value

    def __str__(self):
        """Gibt eine String-Repräsentation für die Ausgabe zurück."""
        return str(self.value)

    def __repr__(self):
        """Gibt eine entwicklerfreundliche String-Repräsentation zurück."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Unterstützt String-Formatierung mit Format-Spezifikationen."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Behandelt Addition: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Behandelt umgekehrte Addition: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Behandelt In-Place-Addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Behandelt Gleichheitsvergleich: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Behandelt Kleiner-als-Vergleich: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Konvertiert zu int (Ganzzahl)."""
        return self.value

    def __float__(self):
        """Konvertiert zu float (Gleitkommazahl)."""
        return float(self.value)

    __index__ = __int__  # Unterstützt Array-Indizierung und andere Operationen, die einen Index erfordern

    def __lshift__(self, other):
        """Behandelt Linksschieben: self << other."""
        if isinstance(other, MutInt):
            return MutInt(self.value << other.value)
        elif isinstance(other, int):
            return MutInt(self.value << other)
        else:
            return NotImplemented

    def __rlshift__(self, other):
        """Behandelt umgekehrtes Linksschieben: other << self."""
        if isinstance(other, int):
            return MutInt(other << self.value)
        else:
            return NotImplemented
```

Wir haben der `MutInt`-Klasse drei neue Methoden hinzugefügt:

1. `__int__()`: Diese Methode wird aufgerufen, wenn Sie die Funktion `int()` auf ein Objekt unserer `MutInt`-Klasse anwenden. Wenn Sie beispielsweise ein `MutInt`-Objekt `a` haben und `int(a)` schreiben, ruft Python die Methode `__int__()` des Objekts `a` auf.
2. `__float__()`: Ebenso wird diese Methode aufgerufen, wenn Sie die Funktion `float()` auf unser `MutInt`-Objekt anwenden.
3. `__index__()`: Diese Methode wird für Operationen verwendet, die speziell einen Integer-Index (Ganzzahlindex) erfordern. Wenn Sie beispielsweise auf ein Element in einer Liste über einen Index zugreifen oder Bitlängenoperationen durchführen möchten, benötigt Python einen Integer-Index.
4. `__lshift__()`: Diese Methode behandelt Linksschiebeoperationen, wenn sich das `MutInt`-Objekt auf der linken Seite des Operators `<<` befindet.
5. `__rlshift__()`: Diese Methode behandelt Linksschiebeoperationen, wenn sich das `MutInt`-Objekt auf der rechten Seite des Operators `<<` befindet.

Die Methode `__index__` ist entscheidend für Operationen, die einen Integer-Index erfordern, wie z. B. Listenindizierung, Slicing und Bitlängenoperationen. In unserer einfachen Implementierung setzen wir sie auf dasselbe wie `__int__`, da der Wert unseres `MutInt`-Objekts direkt als Integer-Index verwendet werden kann.

Die Methoden `__lshift__` und `__rlshift__` sind unerlässlich, um bitweise Linksschiebeoperationen zu unterstützen. Sie ermöglichen es unseren `MutInt`-Objekten, an bitweisen Operationen teilzunehmen, was eine häufige Anforderung für integerähnliche Typen ist.

2. Erstellen Sie eine neue Testdatei namens `test_conversions.py`, um diese neuen Methoden zu testen:

```python
# test_conversions.py

from mutint import MutInt

# Erstellt ein MutInt-Objekt
a = MutInt(3)

# Testet Konvertierungen
print(f"int(a): {int(a)}")
print(f"float(a): {float(a)}")

# Testet die Verwendung als Index
names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
print(f"names[a]: {names[a]}")

# Testet die Verwendung in Bitoperationen (erfordert __index__)
print(f"1 << a: {1 << a}")  # Verschiebt um 3 Stellen nach links

# Testet hex/oct/bin-Funktionen (erfordert __index__)
print(f"hex(a): {hex(a)}")
print(f"oct(a): {oct(a)}")
print(f"bin(a): {bin(a)}")

# Modifiziert und testet erneut
a.value = 4
print(f"\nNachdem der Wert auf 4 geändert wurde:")
print(f"int(a): {int(a)}")
print(f"names[a]: {names[a]}")
```

3. Führen Sie das Testskript aus:

```bash
python3 /home/labex/project/test_conversions.py
```

Sie sollten eine ähnliche Ausgabe wie diese sehen:

```
int(a): 3
float(a): 3.0
names[a]: Thomas
1 << a: 8
hex(a): 0x3
oct(a): 0o3
bin(a): 0b11

Nachdem der Wert auf 4 geändert wurde:
int(a): 4
names[a]: Lewis
```

Jetzt kann unsere `MutInt`-Klasse in Standard-Python-Typen konvertiert und in Operationen verwendet werden, die einen Integer-Index erfordern.

Die Methode `__index__` ist besonders wichtig. Sie wurde in Python eingeführt, um die Verwendung von Objekten in Situationen zu ermöglichen, in denen ein Integer-Index erforderlich ist, wie z. B. Listenindizierung, bitweise Operationen und verschiedene Funktionen wie `hex()`, `oct()` und `bin()`.

Mit diesen Ergänzungen ist unsere `MutInt`-Klasse nun ein recht vollständiger primitiver Typ. Sie kann in den meisten Kontexten verwendet werden, in denen eine reguläre Ganzzahl (Integer) verwendet würde, mit dem zusätzlichen Vorteil, dass sie veränderlich (mutable) ist.

## Vollständige MutInt-Implementierung

Hier ist unsere vollständige `MutInt`-Implementierung mit allen Funktionen, die wir hinzugefügt haben:

```python
# mutint.py

from functools import total_ordering

@total_ordering
class MutInt:
    """
    Eine veränderliche (mutable) Integer-Klasse, die es ermöglicht, ihren Wert nach der Erstellung zu ändern.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialisierung mit einem Integer-Wert."""
        self.value = value

    def __str__(self):
        """Gibt eine String-Repräsentation für die Ausgabe zurück."""
        return str(self.value)

    def __repr__(self):
        """Gibt eine entwicklerfreundliche String-Repräsentation zurück."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Unterstützt String-Formatierung mit Format-Spezifikationen."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Behandelt Addition: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Behandelt umgekehrte Addition: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Behandelt In-Place-Addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Behandelt Gleichheitsvergleich: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Behandelt Kleiner-als-Vergleich: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Konvertiert zu int (Ganzzahl)."""
        return self.value

    def __float__(self):
        """Konvertiert zu float (Gleitkommazahl)."""
        return float(self.value)

    __index__ = __int__  # Unterstützt Array-Indizierung und andere Operationen, die einen Index erfordern

    def __lshift__(self, other):
        """Behandelt Linksschieben: self << other."""
        if isinstance(other, MutInt):
            return MutInt(self.value << other.value)
        elif isinstance(other, int):
            return MutInt(self.value << other)
        else:
            return NotImplemented

    def __rlshift__(self, other):
        """Behandelt umgekehrtes Linksschieben: other << self."""
        if isinstance(other, int):
            return MutInt(other << self.value)
        else:
            return NotImplemented
```

Diese Implementierung deckt die wichtigsten Aspekte der Erstellung eines neuen primitiven Typs in Python ab. Um sie noch vollständiger zu machen, könnten Sie zusätzliche Methoden für andere Operationen wie Subtraktion, Multiplikation, Division usw. implementieren.
