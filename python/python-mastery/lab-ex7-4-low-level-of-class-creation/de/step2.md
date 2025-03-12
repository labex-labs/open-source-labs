# Erstellen eines Hilfsprogramms für typisierte Strukturen

In diesem Schritt werden wir ein praktischeres Beispiel erstellen. Wir implementieren eine Funktion, die Klassen mit Typüberprüfung (type validation) erstellt. Typüberprüfung ist von entscheidender Bedeutung, da sie sicherstellt, dass die den Klassenattributen zugewiesenen Daten bestimmten Kriterien entsprechen, wie z. B. einem bestimmten Datentyp oder einem bestimmten Wertebereich. Dies hilft, Fehler frühzeitig zu erkennen und macht unseren Code robuster.

## Verständnis der `Structure`-Klasse

Zunächst müssen wir die Datei `structure.py` im WebIDE-Editor öffnen. Diese Datei enthält eine grundlegende `Structure`-Klasse. Diese Klasse bietet die grundlegende Funktionalität zur Initialisierung und Darstellung von strukturierten Objekten. Initialisierung bedeutet, dass das Objekt mit den bereitgestellten Daten eingerichtet wird, und Darstellung bezieht sich darauf, wie das Objekt angezeigt wird, wenn wir es ausgeben.

Um die Datei zu öffnen, verwenden wir den folgenden Befehl im Terminal:

```bash
cd ~/project
```

Nachdem Sie diesen Befehl ausgeführt haben, befinden Sie sich im richtigen Verzeichnis, in dem sich die Datei `structure.py` befindet. Wenn Sie die Datei öffnen, werden Sie die grundlegende `Structure`-Klasse bemerken. Unser Ziel ist es, diese Klasse zu erweitern, um Typüberprüfung zu unterstützen.

## Implementieren der `typed_structure`-Funktion

Jetzt fügen wir die `typed_structure`-Funktion zur Datei `structure.py` hinzu. Diese Funktion wird eine neue Klasse erstellen, die von der `Structure`-Klasse erbt und die angegebenen Validatoren enthält. Vererbung bedeutet, dass die neue Klasse alle Funktionen der `Structure`-Klasse hat und auch ihre eigenen Features hinzufügen kann. Validatoren werden verwendet, um zu überprüfen, ob die den Klassenattributen zugewiesenen Werte gültig sind.

Hier ist der Code für die `typed_structure`-Funktion:

```python
def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

Der Parameter `clsname` ist der Name, den wir der neuen Klasse geben möchten. Der Parameter `validators` ist ein Dictionary, in dem die Schlüssel die Attributnamen und die Werte die Validator-Objekte sind. Die `type()`-Funktion wird verwendet, um eine neue Klasse dynamisch zu erstellen. Sie nimmt drei Argumente: den Klassennamen, ein Tupel von Basisklassen (in diesem Fall nur die `Structure`-Klasse) und ein Dictionary von Klassenattributen (die Validatoren).

Nachdem Sie diese Funktion hinzugefügt haben, sollte Ihre `structure.py`-Datei wie folgt aussehen:

```python
# Structure class definition

class Structure:
    _fields = ()

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        attrs = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({attrs})'

def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

## Testen der `typed_structure`-Funktion

Lassen Sie uns unsere `typed_structure`-Funktion mit den Validatoren aus der Datei `validate.py` testen. Diese Validatoren werden verwendet, um zu überprüfen, ob die den Klassenattributen zugewiesenen Werte den richtigen Typ haben und anderen Kriterien entsprechen.

Zunächst öffnen wir eine interaktive Python-Shell. Wir verwenden die folgenden Befehle im Terminal:

```bash
cd ~/project
python3
```

Der erste Befehl bringt uns in das richtige Verzeichnis, und der zweite Befehl startet die interaktive Python-Shell.

Jetzt importieren wir die erforderlichen Komponenten und erstellen eine typisierte Struktur:

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import typed_structure

# Create a Stock class with type validation
Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())

# Create a stock instance
s = Stock('GOOG', 100, 490.1)

# Test the instance
print(s.name)
print(s)

# Test validation
try:
    invalid_stock = Stock('AAPL', -10, 150.25)  # Should raise an error
except ValueError as e:
    print(f"Validation error: {e}")
```

Wir importieren die Validatoren `String`, `PositiveInteger` und `PositiveFloat` aus der Datei `validate.py`. Dann verwenden wir die `typed_structure`-Funktion, um eine `Stock`-Klasse mit Typüberprüfung zu erstellen. Wir erstellen eine Instanz der `Stock`-Klasse und testen sie, indem wir ihre Attribute ausgeben. Schließlich versuchen wir, eine ungültige Aktieninstanz zu erstellen, um die Überprüfung zu testen.

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
GOOG
Stock('GOOG', 100, 490.1)
Validation error: Expected a positive value
```

Wenn Sie mit dem Testen fertig sind, beenden Sie die Python-Shell:

```python
exit()
```

Dieses Beispiel zeigt, wie wir die `type()`-Funktion verwenden können, um benutzerdefinierte Klassen mit bestimmten Überprüfungsregeln zu erstellen. Dieser Ansatz ist sehr leistungsstark, da er es uns ermöglicht, Klassen programmgesteuert zu generieren, was viel Zeit sparen und unseren Code flexibler machen kann.
