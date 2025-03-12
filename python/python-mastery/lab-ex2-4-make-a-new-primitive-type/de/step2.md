# Verbesserung der String - Darstellung

Wenn Sie in Python ein `MutInt` - Objekt ausgeben, sehen Sie eine Ausgabe wie `<__main__.MutInt object at 0x...>`. Diese Ausgabe ist nicht sehr hilfreich, da sie Ihnen den tatsächlichen Wert des `MutInt` - Objekts nicht mitteilt. Um es einfacher zu machen, zu verstehen, was das Objekt repräsentiert, werden wir spezielle Methoden für die String - Darstellung implementieren.

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
```

Wir haben drei wichtige Methoden zur `MutInt` - Klasse hinzugefügt:

- `__str__()`: Diese Methode wird aufgerufen, wenn Sie die `str()` - Funktion auf das Objekt anwenden oder das Objekt direkt ausgeben. Sie sollte eine menschenlesbare Zeichenkette zurückgeben.
- `__repr__()`: Diese Methode liefert die "offizielle" String - Darstellung des Objekts. Sie wird hauptsächlich zum Debugging verwendet und sollte idealerweise eine Zeichenkette zurückgeben, die, wenn sie an die `eval()` - Funktion übergeben wird, das Objekt neu erstellen würde.
- `__format__()`: Diese Methode ermöglicht es Ihnen, Python's Zeichenkettenformatierungssystem mit Ihren `MutInt` - Objekten zu verwenden. Sie können Formatangaben wie Auffüllung und Zahlenformatierung nutzen.

2. Erstellen Sie eine neue Testdatei namens `test_string_repr.py`, um diese neuen Methoden zu testen:

```python
# test_string_repr.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test string representation
print(f"str(a): {str(a)}")
print(f"repr(a): {repr(a)}")

# Test direct printing
print(f"Print a: {a}")

# Test string formatting
print(f"Formatted with padding: '{a:*^10}'")
print(f"Formatted as decimal: '{a:d}'")

# Test mutability
a.value = 42
print(f"After changing value, repr(a): {repr(a)}")
```

In dieser Testdatei importieren wir zunächst die `MutInt` - Klasse. Dann erstellen wir ein `MutInt` - Objekt mit dem Wert `3`. Wir testen die `__str__()` - und `__repr__()` - Methoden, indem wir die `str()` - und `repr()` - Funktionen verwenden. Wir testen auch die direkte Ausgabe, die Zeichenkettenformatierung und die Veränderlichkeit des `MutInt` - Objekts.

3. Führen Sie das Testskript aus:

```bash
python3 /home/labex/project/test_string_repr.py
```

Wenn Sie diesen Befehl ausführen, wird Python das `test_string_repr.py` - Skript ausführen. Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
str(a): 3
repr(a): MutInt(3)
Print a: 3
Formatted with padding: '****3*****'
Formatted as decimal: '3'
After changing value, repr(a): MutInt(42)
```

Jetzt werden unsere `MutInt` - Objekte schön angezeigt. Die String - Darstellung zeigt den zugrunde liegenden Wert, und wir können die Zeichenkettenformatierung genauso wie bei normalen Ganzzahlen verwenden.

Der Unterschied zwischen `__str__()` und `__repr__()` besteht darin, dass `__str__()` dazu dient, eine menschenfreundliche Ausgabe zu erzeugen, während `__repr__()` idealerweise eine Zeichenkette erzeugen sollte, die, wenn sie an `eval()` übergeben wird, das Objekt neu erstellen würde. Deshalb haben wir den Klassennamen in der `__repr__()` - Methode enthalten.

Die `__format__()` - Methode ermöglicht es unserem Objekt, mit Python's Formatierungssystem zu arbeiten, sodass wir Formatangaben wie Auffüllung und Zahlenformatierung verwenden können.
