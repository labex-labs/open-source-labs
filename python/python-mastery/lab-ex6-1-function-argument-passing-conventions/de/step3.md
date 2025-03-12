# Verbesserung der Objektrepräsentation

Unsere `Structure`-Klasse ist nützlich für die Erstellung und den Zugriff auf Objekte. Derzeit gibt es jedoch keine gute Möglichkeit, sich selbst als Zeichenkette darzustellen. Wenn Sie ein Objekt ausgeben oder es im Python-Interpreter anzeigen lassen, möchten Sie eine klare und informative Darstellung sehen. Dies hilft Ihnen zu verstehen, was das Objekt ist und welche Werte es hat.

## Verständnis der Objektrepräsentation in Python

In Python gibt es zwei spezielle Methoden, die verwendet werden, um Objekte auf verschiedene Weise darzustellen. Diese Methoden sind wichtig, da sie es Ihnen ermöglichen, zu steuern, wie Ihre Objekte angezeigt werden.

- `__str__` - Diese Methode wird von der `str()`-Funktion und der `print()`-Funktion verwendet. Sie liefert eine menschenlesbare Darstellung des Objekts. Beispielsweise könnte die `__str__`-Methode für ein `Stock`-Objekt etwas wie "Stock: GOOG, 100 shares at $490.1" zurückgeben.
- `__repr__` - Diese Methode wird vom Python-Interpreter und der `repr()`-Funktion verwendet. Sie gibt eine technischere und eindeutige Darstellung des Objekts. Das Ziel von `__repr__` ist es, eine Zeichenkette bereitzustellen, die verwendet werden kann, um das Objekt neu zu erstellen. Beispielsweise könnte es für ein `Stock`-Objekt "Stock('GOOG', 100, 490.1)" zurückgeben.

Fügen wir eine `__repr__`-Methode zu unserer `Structure`-Klasse hinzu. Dies erleichtert das Debugging unseres Codes, da wir den Zustand unserer Objekte deutlich sehen können.

## Implementierung einer guten Repräsentation

Jetzt müssen Sie Ihre `structure.py`-Datei aktualisieren. Sie fügen die `__repr__`-Methode zur `Structure`-Klasse hinzu. Diese Methode erstellt eine Zeichenkette, die das Objekt auf eine Weise darstellt, die es ermöglicht, es neu zu erstellen.

```python
def __repr__(self):
    """
    Return a representation of the object that can be used to recreate it.
    Example: Stock('GOOG', 100, 490.1)
    """
    # Get the class name
    cls_name = type(self).__name__

    # Get all the field values
    values = [getattr(self, name) for name in self._fields]

    # Format the fields and values
    args_str = ', '.join(repr(value) for value in values)

    # Return the formatted string
    return f"{cls_name}({args_str})"
```

Hier ist, was diese Methode Schritt für Schritt macht:

1. Sie ruft den Klassennamen mit `type(self).__name__` ab. Dies ist wichtig, da es Ihnen sagt, um welche Art von Objekt es sich handelt.
2. Sie ruft alle Feldwerte aus der Instanz ab. Dies gibt Ihnen die Daten, die das Objekt enthält.
3. Sie erstellt eine Zeichenkettenrepräsentation mit dem Klassennamen und den Werten. Diese Zeichenkette kann verwendet werden, um das Objekt neu zu erstellen.

## Testen der verbesserten Repräsentation

Lassen Sie uns unsere verbesserte Implementierung testen. Erstellen Sie eine neue Datei namens `test_repr.py`. Diese Datei wird einige Instanzen unserer Klassen erstellen und ihre Repräsentationen ausgeben.

```python
# test_repr.py
from structure import Stock, Point, Date

# Create instances
s = Stock('GOOG', 100, 490.1)
p = Point(3, 4)
d = Date(2023, 11, 9)

# Print the representations
print(repr(s))
print(repr(p))
print(repr(d))

# Direct printing also uses __repr__ in the interpreter
print(s)
print(p)
print(d)
```

Um den Test auszuführen, öffnen Sie Ihr Terminal und geben Sie den folgenden Befehl ein:

```bash
python3 test_repr.py
```

Sie sollten die folgende Ausgabe sehen:

```
Stock('GOOG', 100, 490.1)
Point(3, 4)
Date(2023, 11, 9)
Stock('GOOG', 100, 490.1)
Point(3, 4)
Date(2023, 11, 9)
```

Diese Ausgabe ist viel informativer als zuvor. Wenn Sie `Stock('GOOG', 100, 490.1)` sehen, wissen Sie sofort, was das Objekt darstellt. Sie könnten sogar diese Zeichenkette kopieren und verwenden, um das Objekt in Ihrem Code neu zu erstellen.

## Der Nutzen guter Repräsentationen

Eine gute `__repr__`-Implementierung ist sehr hilfreich für das Debugging. Wenn Sie sich Objekte im Interpreter ansehen oder sie während der Programmausführung protokollieren, erleichtert eine klare Repräsentation die schnelle Identifizierung von Problemen. Sie können den genauen Zustand des Objekts sehen und verstehen, was möglicherweise schief geht.
