# Implementierung alternativer Konstruktoren mit Klassenmethoden

In diesem Schritt werden wir lernen, wie man einen alternativen Konstruktor mithilfe einer Klassenmethode implementiert. Dies ermöglicht es uns, `Stock`-Objekte aus CSV-Zeilen-Daten auf elegantere Weise zu erstellen.

## Was ist ein alternativer Konstruktor?

In Python ist ein alternativer Konstruktor ein nützliches Muster. Normalerweise erstellen wir Objekte mit der Standardmethode `__init__`. Ein alternativer Konstruktor bietet uns jedoch eine zusätzliche Möglichkeit, Objekte zu erstellen. Klassenmethoden eignen sich sehr gut für die Implementierung alternativer Konstruktoren, da sie auf die Klasse selbst zugreifen können.

## Implementierung der from_row()-Klassenmethode

Wir werden unserer `Stock`-Klasse eine Klassenvariable `types` und eine Klassenmethode `from_row()` hinzufügen. Dies vereinfacht den Prozess der Erstellung von `Stock`-Instanzen aus CSV-Daten.

Lassen Sie uns die Datei `stock.py` ändern, indem wir den hervorgehobenen Code hinzufügen:

```python
# stock.py

class Stock:
    types = (str, int, float)  # Type conversions to apply to CSV data

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    @classmethod
    def from_row(cls, row):
        """
        Create a Stock instance from a row of CSV data.

        Args:
            row: A list of strings [name, shares, price]

        Returns:
            A new Stock instance
        """
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

# The rest of the file remains unchanged
```

Jetzt wollen wir verstehen, was in diesem Code Schritt für Schritt passiert:

1. Wir haben eine Klassenvariable `types` definiert. Es handelt sich um ein Tupel, das die Typkonvertierungsfunktionen `(str, int, float)` enthält. Diese Funktionen werden verwendet, um die Daten aus der CSV-Zeile in die entsprechenden Typen umzuwandeln.
2. Wir haben eine Klassenmethode `from_row()` hinzugefügt. Der `@classmethod`-Decorator markiert diese Methode als Klassenmethode.
3. Der erste Parameter dieser Methode ist `cls`, was ein Verweis auf die Klasse selbst ist. In normalen Methoden verwenden wir `self`, um auf eine Instanz der Klasse zu verweisen, aber hier verwenden wir `cls`, da es sich um eine Klassenmethode handelt.
4. Die `zip()`-Funktion wird verwendet, um jede Typkonvertierungsfunktion in `types` mit dem entsprechenden Wert in der `row`-Liste zu verknüpfen.
5. Wir verwenden eine Listen-Komprehension, um jede Konvertierungsfunktion auf den entsprechenden Wert in der `row`-Liste anzuwenden. Auf diese Weise wandeln wir die String-Daten aus der CSV-Zeile in die entsprechenden Typen um.
6. Schließlich erstellen wir eine neue Instanz der `Stock`-Klasse mit den umgewandelten Werten und geben sie zurück.

## Testen des alternativen Konstruktors

Jetzt erstellen wir eine neue Datei namens `test_class_method.py`, um unsere neue Klassenmethode zu testen. Dies hilft uns zu überprüfen, ob der alternative Konstruktor wie erwartet funktioniert.

```python
# test_class_method.py
from stock import Stock

# Test the from_row() class method
row = ['AA', '100', '32.20']
s = Stock.from_row(row)

print(f"Stock: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost()}")

# Try with a different row
row2 = ['GOOG', '50', '1120.50']
s2 = Stock.from_row(row2)

print(f"\nStock: {s2.name}")
print(f"Shares: {s2.shares}")
print(f"Price: {s2.price}")
print(f"Cost: {s2.cost()}")
```

Um die Ergebnisse zu sehen, führen Sie die folgenden Befehle in Ihrem Terminal aus:

```bash
cd ~/project
python test_class_method.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Stock: AA
Shares: 100
Price: 32.2
Cost: 3220.0

Stock: GOOG
Shares: 50
Price: 1120.5
Cost: 56025.0
```

Beachten Sie, dass wir jetzt `Stock`-Instanzen direkt aus String-Daten erstellen können, ohne dass wir außerhalb der Klasse manuell Typkonvertierungen durchführen müssen. Dies macht unseren Code sauberer und stellt sicher, dass die Verantwortung für die Datenkonvertierung innerhalb der Klasse selbst behandelt wird.
