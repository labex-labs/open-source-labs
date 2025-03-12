# Erstellen einer grundlegenden MutInt - Klasse

Beginnen wir damit, eine grundlegende Klasse für unseren veränderlichen Ganzzahltyp zu erstellen. In der Programmierung ist eine Klasse wie ein Bauplan für die Erstellung von Objekten. In diesem Schritt werden wir die Grundlage für unseren neuen primitiven Datentyp legen. Ein primitiver Datentyp ist ein grundlegender Datentyp, der von einer Programmiersprache bereitgestellt wird, und hier werden wir unseren eigenen benutzerdefinierten Datentyp erstellen.

1. Öffnen Sie die WebIDE und navigieren Sie zum Verzeichnis `/home/labex/project`. Die WebIDE ist eine integrierte Entwicklungsumgebung, in der Sie Ihren Code schreiben, bearbeiten und ausführen können. Das Navigieren zu diesem Verzeichnis stellt sicher, dass alle Ihre Dateien an einem Ort organisiert sind und richtig miteinander interagieren können.

2. Öffnen Sie die Datei `mutint.py`, die für Sie im Einrichtungsschritt erstellt wurde. In dieser Datei wird die Definition unserer `MutInt` - Klasse gespeichert.

3. Fügen Sie den folgenden Code hinzu, um eine grundlegende `MutInt` - Klasse zu definieren:

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
```

Das `__slots__` - Attribut wird verwendet, um die Attribute zu definieren, die diese Klasse haben kann. Attribute sind wie Variablen, die zu einem Objekt der Klasse gehören. Durch die Verwendung von `__slots__` sagen wir Python, ein speicher - effizienteres Verfahren zur Speicherung von Attributen zu verwenden. In diesem Fall wird unsere `MutInt` - Klasse nur ein einzelnes Attribut namens `value` haben. Dies bedeutet, dass jedes Objekt der `MutInt` - Klasse nur ein Datenstück aufnehmen kann, nämlich den ganzzahligen Wert.

Die `__init__` - Methode ist der Konstruktor für unsere Klasse. Ein Konstruktor ist eine spezielle Methode, die aufgerufen wird, wenn ein Objekt der Klasse erstellt wird. Sie nimmt einen Wertparameter entgegen und speichert ihn im `value` - Attribut der Instanz. Eine Instanz ist ein einzelnes Objekt, das aus dem Klassenbauplan erstellt wird.

Lassen Sie uns unsere Klasse testen, indem wir ein Python - Skript erstellen, um sie zu verwenden:

4. Erstellen Sie eine neue Datei namens `test_mutint.py` im gleichen Verzeichnis:

```python
# test_mutint.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)
print(f"Created MutInt with value: {a.value}")

# Modify the value (demonstrating mutability)
a.value = 42
print(f"Modified value to: {a.value}")

# Try adding (this will fail)
try:
    result = a + 10
    print(f"Result of a + 10: {result}")
except TypeError as e:
    print(f"Error when adding: {e}")
```

In diesem Testskript importieren wir zunächst die `MutInt` - Klasse aus der Datei `mutint.py`. Dann erstellen wir ein Objekt der `MutInt` - Klasse mit einem Anfangswert von 3. Wir geben den Anfangswert aus, ändern ihn dann auf 42 und geben den neuen Wert aus. Schließlich versuchen wir, 10 zum `MutInt` - Objekt hinzuzufügen, was zu einem Fehler führt, da unsere Klasse die Additionsoperation noch nicht unterstützt.

5. Führen Sie das Testskript aus, indem Sie den folgenden Befehl im Terminal ausführen:

```bash
python3 /home/labex/project/test_mutint.py
```

Das Terminal ist eine Befehlszeilenoberfläche, in der Sie verschiedene Befehle ausführen können, um mit Ihrem System und Ihrem Code zu interagieren. Das Ausführen dieses Befehls führt das `test_mutint.py` - Skript aus.

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Created MutInt with value: 3
Modified value to: 42
Error when adding: unsupported operand type(s) for +: 'MutInt' and 'int'
```

Unsere `MutInt` - Klasse speichert und aktualisiert erfolgreich einen Wert. Allerdings hat sie mehrere Einschränkungen:

- Sie wird nicht schön angezeigt, wenn sie ausgegeben wird.
- Sie unterstützt keine mathematischen Operationen wie Addition.
- Sie unterstützt keine Vergleiche.
- Sie unterstützt keine Typkonvertierungen.

In den nächsten Schritten werden wir diese Einschränkungen nacheinander beseitigen, damit unsere `MutInt` - Klasse sich mehr wie ein echter primitiver Datentyp verhält.
