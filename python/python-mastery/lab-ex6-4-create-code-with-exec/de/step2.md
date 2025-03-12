# Dynamisches Erstellen einer `__init__()`-Methode

Jetzt werden wir das, was wir über die `exec()`-Funktion gelernt haben, auf ein reales Programmier-Szenario anwenden. In Python ermöglicht die `exec()`-Funktion die Ausführung von Python-Code, der in einer Zeichenkette gespeichert ist. In diesem Schritt werden wir die `Structure`-Klasse modifizieren, um eine `__init__()`-Methode dynamisch zu erstellen. Die `__init__()`-Methode ist eine spezielle Methode in Python-Klassen, die aufgerufen wird, wenn ein Objekt der Klasse instanziiert wird. Die Erstellung dieser Methode basiert auf der Klassenvariablen `_fields`, die eine Liste von Feldnamen für die Klasse enthält.

Zunächst werfen wir einen Blick auf die vorhandene Datei `structure.py`. Diese Datei enthält die aktuelle Implementierung der `Structure`-Klasse und eine `Stock`-Klasse, die von ihr erbt. Um den Inhalt der Datei anzuzeigen, öffnen Sie sie im WebIDE mit dem folgenden Befehl:

```bash
cat /home/labex/project/structure.py
```

In der Ausgabe sehen Sie, dass die aktuelle Implementierung einen manuellen Ansatz zur Initialisierung von Objekten verwendet. Dies bedeutet, dass der Code zur Initialisierung der Objektattribute explizit geschrieben wird, anstatt dynamisch generiert zu werden.

Jetzt werden wir die `Structure`-Klasse modifizieren. Wir werden eine Klassenmethode `create_init()` hinzufügen, die die `__init__()`-Methode dynamisch generiert. Um diese Änderungen vorzunehmen, öffnen Sie die Datei `structure.py` im WebIDE-Editor und befolgen Sie diese Schritte:

1. Entfernen Sie die vorhandenen Methoden `_init()` und `set_fields()` aus der `Structure`-Klasse. Diese Methoden gehören zum manuellen Initialisierungsansatz, und wir brauchen sie nicht mehr, da wir einen dynamischen Ansatz verwenden werden.

2. Fügen Sie die Klassenmethode `create_init()` zur `Structure`-Klasse hinzu. Hier ist der Code für die Methode:

```python
@classmethod
def create_init(cls):
    """Dynamically create an __init__ method based on _fields."""
    # Create argument string from field names
    argstr = ','.join(cls._fields)

    # Create the function code as a string
    code = f'def __init__(self, {argstr}):\n'
    for name in cls._fields:
        code += f'    self.{name} = {name}\n'

    # Execute the code and get the generated function
    locs = {}
    exec(code, locs)

    # Set the function as the __init__ method of the class
    setattr(cls, '__init__', locs['__init__'])
```

In dieser Methode erstellen wir zunächst eine Zeichenkette `argstr`, die alle Feldnamen durch Kommas getrennt enthält. Diese Zeichenkette wird als Argumentliste für die `__init__()`-Methode verwendet. Dann erstellen wir den Code für die `__init__()`-Methode als Zeichenkette. Wir gehen durch die Feldnamen in einer Schleife und fügen Zeilen zum Code hinzu, die jedem Argument das entsprechende Objektattribut zuweisen. Danach verwenden wir die `exec()`-Funktion, um den Code auszuführen und die generierte Funktion im `locs`-Dictionary zu speichern. Schließlich verwenden wir die `setattr()`-Funktion, um die generierte Funktion als `__init__()`-Methode der Klasse festzulegen.

3. Modifizieren Sie die `Stock`-Klasse, um diesen neuen Ansatz zu verwenden:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

Hier definieren wir die `_fields` für die `Stock`-Klasse und rufen dann die Methode `create_init()` auf, um die `__init__()`-Methode für die `Stock`-Klasse zu generieren.

Ihre vollständige `structure.py`-Datei sollte jetzt in etwa so aussehen:

```python
class Structure:
    # Restrict attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")

    # String representation for debugging
    def __repr__(self):
        args = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f"{type(self).__name__}({args})"

    @classmethod
    def create_init(cls):
        """Dynamically create an __init__ method based on _fields."""
        # Create argument string from field names
        argstr = ','.join(cls._fields)

        # Create the function code as a string
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'

        # Execute the code and get the generated function
        locs = {}
        exec(code, locs)

        # Set the function as the __init__ method of the class
        setattr(cls, '__init__', locs['__init__'])

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

Jetzt testen wir unsere Implementierung, um sicherzustellen, dass sie korrekt funktioniert. Wir werden die Unittests ausführen, um zu überprüfen, ob alle Tests erfolgreich sind. Verwenden Sie die folgenden Befehle:

```bash
cd /home/labex/project
python3 -m unittest test_structure.py
```

Wenn Ihre Implementierung korrekt ist, sollten Sie sehen, dass alle Tests erfolgreich sind. Dies bedeutet, dass die dynamisch generierte `__init__()`-Methode wie erwartet funktioniert.

Sie können die Klasse auch manuell in der Python-Shell testen. So können Sie es tun:

```python
>>> from structure import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s
Stock('GOOG', 100, 490.1)
>>> s.shares = 50
>>> s.share = 50  # This should raise an AttributeError
Traceback (most recent call last):
  ...
AttributeError: No attribute share
```

In der Python-Shell importieren wir zunächst die `Stock`-Klasse aus der Datei `structure.py`. Dann erstellen wir eine Instanz der `Stock`-Klasse und geben sie aus. Wir können auch das Attribut `shares` des Objekts ändern. Wenn wir jedoch versuchen, ein Attribut festzulegen, das nicht in der `_fields`-Liste vorhanden ist, sollten wir einen `AttributeError` erhalten.

Herzlichen Glückwunsch! Sie haben erfolgreich die `exec()`-Funktion verwendet, um eine `__init__()`-Methode basierend auf Klassenattributen dynamisch zu erstellen. Dieser Ansatz macht Ihren Code flexibler und einfacher zu warten, insbesondere wenn es um Klassen mit einer variablen Anzahl von Attributen geht.
